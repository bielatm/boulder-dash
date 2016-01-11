class GameObject(object):
    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
        self.game_state = None
        self.updated = False

    def move(self, x, y):
        self.grid.cells[self.x][self.y] = None
        self.x += x
        self.y += y
        self.grid.cells[self.x][self.y] = self

    def update(self):
        self.updated = True


class FallingGameObject(GameObject):
    def __init__(self, *args, **kwargs):
        super(FallingGameObject, self).__init__(*args, **kwargs)
        self.is_falling = False

    def update(self):
        super(FallingGameObject, self).update()
        if not self.grid.cells[self.x][self.y + 1]:
            self.move(0, 1)
            self.is_falling = True
        elif type(self.grid.cells[self.x][self.y + 1]) == Hero and self.is_falling:
            self.game_state.game_over()
            self.is_falling = False
        elif type(self.grid.cells[self.x][self.y + 1]) == Rock:
            if not self.grid.cells[self.x - 1][self.y] and not self.grid.cells[self.x - 1][self.y + 1]:
                self.move(-1, 0)
            elif not self.grid.cells[self.x + 1][self.y] and not self.grid.cells[self.x + 1][self.y + 1]:
                self.move(1, 0)
        else:
            self.is_falling = False


class Hero(GameObject):
    PIXMAP = 'gameHero'

    def move(self, x, y):
        if type(self.grid.cells[self.x + x][self.y + y]) == Diamond:
            self.game_state.score += 1
        elif type(self.grid.cells[self.x + x][self.y + y]) == Rock:
            if self.grid.cells[self.x + 2*x][self.y] is None:
                self.grid.cells[self.x + x][self.y].move(x, 0)
            else:
                return
        elif type(self.grid.cells[self.x + x][self.y + y]) == Wall:
            return
        super(Hero, self).move(x, y)


class Wall(GameObject):
    PIXMAP = 'wall'


class Ground(GameObject):
    PIXMAP = 'ground'


class Rock(FallingGameObject):
    PIXMAP = 'rock'


class Diamond(FallingGameObject):
    PIXMAP = 'diamond'
