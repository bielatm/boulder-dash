from PyQt4 import QtGui, QtCore
from game import Grid, GameState
from game import Config


class Board(QtGui.QFrame):

    status_bar = QtCore.pyqtSignal(str)

    def __init__(self, parent, image_repository):
        super(Board, self).__init__(parent)
        self.started = True
        self.paused = False
        self.image_repository = image_repository
        self.config = Config.get()
        self.size = 50
        self.grid = Grid.random(self.config.properties['board_width'], self.config.properties['board_height'],
                                self.config.properties['rock_count'], self.config.properties['diamond_count'])
        self.game_state = GameState(self.grid, self.grid.cells[1][1], self)
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                self.grid.cells[x][y].game_state = self.game_state
        self.initUI()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(100)

    def initUI(self):
        pal = QtGui.QPalette(self.palette())
        pal.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.show()

    def update_game(self):
        if not self.paused:
            self.game_state.update()
            if self.started and self.game_state.score < self.config.properties['diamond_count']:
                self.status_bar.emit("Score: " + str(self.game_state.score) +
                                     "/" + str(self.config.properties['diamond_count']))
            elif self.started and self.game_state.score == self.config.properties['diamond_count']:
                self.status_bar.emit("You win!!!")
                self.timer.stop()
            else:
                self.status_bar.emit("Game over")
                self.timer.stop()
            self.update()
        else:
            self.status_bar.emit("Paused")

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if self.grid.cells[x][y]:
                    pixmap = self.image_repository.get_pixmap(self.grid.cells[x][y].PIXMAP,
                                                              self.size, self.size)
                    qp.drawPixmap((x - self.game_state.camera_x + 9) * self.size,
                                  (y - self.game_state.camera_y + 7) * self.size, pixmap)
        pixmap = self.image_repository.get_pixmap('gameHero', self.size, self.size)
        qp.drawPixmap((self.game_state.hero.x - self.game_state.camera_x + 9) * self.size,
                      (self.game_state.hero.y - self.game_state.camera_y + 7) * self.size, pixmap)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_P:
            self.paused = not self.paused

        if not self.paused:
            try:
                self.game_state.player_displacement = {
                    QtCore.Qt.Key_Left: (-1, 0),
                    QtCore.Qt.Key_Right: (1, 0),
                    QtCore.Qt.Key_Down: (0, 1),
                    QtCore.Qt.Key_Up: (0, -1)
                }[event.key()]
            except:
                pass
