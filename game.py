import random
from game_objects import Hero, Wall, Ground, Rock, Diamond
import json
import os


class Config(object):
    PATH = 'options.json'
    DEFAULTS = {
        'username': 'Unknown',
        'board_width': 20,
        'board_height': 15,
        'rock_count': 30,
        'diamond_count': 15
    }

    @classmethod
    def get(cls):
        properties = cls.DEFAULTS.copy()
        try:
            with open(cls.PATH, 'r') as f:
                properties.update(json.load(f))
        except FileNotFoundError:
            pass
        return cls(properties)

    def __init__(self, properties):
        self.properties = properties

    def save(self):
        with open(self.PATH, 'w') as f:
            json.dump(self.properties, f)

    def destroy(self):
        os.remove(self.PATH)


class Grid(object):

    @classmethod
    def random(cls, width, height, rock_count, diamond_count):
        grid = cls(width, height)

        for x in range(width):
            for y in range(height):
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    grid.cells[x][y] = Wall(grid, x, y)
                else:
                    grid.cells[x][y] = Ground(grid, x, y)
        grid.cells[1][1] = Hero(grid, 1, 1)

        cell_indexes = [
            (x, y)
            for x in range(1, width - 1)
            for y in range(1, height - 1)
        ]

        cell_indexes.remove((1, 1))

        for _ in range(rock_count):
            x, y = cell_indexes.pop(random.randint(0, len(cell_indexes) - 1))
            grid.cells[x][y] = Rock(grid, x, y)

        for _ in range(diamond_count):
            x, y = cell_indexes.pop(random.randint(0, len(cell_indexes) - 1))
            grid.cells[x][y] = Diamond(grid, x, y)

        return grid

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[None] * self.height for _ in range(self.width)]


class GameState(object):
    def __init__(self, grid, hero, board):
        self.grid = grid
        self.board = board
        self.player_displacement = None
        self.hero = hero
        self.camera_x = 1
        self.camera_y = 1
        self.score = 0

    def game_over(self):
        self.board.started = False

    def update(self):
        if self.player_displacement:
            move_x = self.player_displacement[0]
            move_y = self.player_displacement[1]
            self.player_displacement = None
            self.hero.move(move_x, move_y)
            if self.camera_requiers_update():
                self.camera_x += move_x
                self.camera_y += move_y

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if self.grid.cells[x][y] and not self.grid.cells[x][y].updated:
                    self.grid.cells[x][y].update()

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if self.grid.cells[x][y]:
                    self.grid.cells[x][y].updated = False

    def camera_requiers_update(self):
        return abs(self.hero.x - self.camera_x) > 4 or abs(self.hero.y - self.camera_y) > 4
