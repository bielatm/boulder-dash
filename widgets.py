from PyQt4 import QtGui, QtCore
from game import Config


class OptionsWindow(QtGui.QWidget):

    def __init__(self):
        super(OptionsWindow, self).__init__()

        self.initUI()

    def initUI(self):
        username = QtGui.QLabel('Username')
        self.usernameEdit = QtGui.QLineEdit()
        self.usernameEdit.setText("Unknown")
        board_width = QtGui.QLabel('Width of board')
        self.board_width = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        board_height = QtGui.QLabel('Height of board')
        self.board_height = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        rock_count = QtGui.QLabel('Number of rocks')
        self.rock_count = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        diamond_count = QtGui.QLabel('Number of diamonds')
        self.diamond_count = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        lcd_width = QtGui.QLCDNumber(self)
        lcd_height = QtGui.QLCDNumber(self)
        lcd_rocks = QtGui.QLCDNumber(self)
        lcd_diamonds = QtGui.QLCDNumber(self)

        default = QtGui.QPushButton('Default options')
        save = QtGui.QPushButton('Save')

        save.clicked.connect(self.write_to_file)
        save.clicked.connect(self.close)
        default.clicked.connect(self.write_default_options)
        default.clicked.connect(self.close)

        hbox_username = QtGui.QHBoxLayout()
        hbox_username.addWidget(username)
        hbox_username.addWidget(self.usernameEdit)

        hbox_width = QtGui.QHBoxLayout()
        hbox_width.addWidget(board_width)
        hbox_width.addWidget(lcd_width)

        hbox_height = QtGui.QHBoxLayout()
        hbox_height.addWidget(board_height)
        hbox_height.addWidget(lcd_height)

        hbox_rocks = QtGui.QHBoxLayout()
        hbox_rocks.addWidget(rock_count)
        hbox_rocks.addWidget(lcd_rocks)

        hbox_diamonds = QtGui.QHBoxLayout()
        hbox_diamonds.addWidget(diamond_count)
        hbox_diamonds.addWidget(lcd_diamonds)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox_username)
        vbox.addLayout(hbox_width)
        vbox.addWidget(self.board_width)
        vbox.addLayout(hbox_height)
        vbox.addWidget(self.board_height)
        vbox.addLayout(hbox_rocks)
        vbox.addWidget(self.rock_count)
        vbox.addLayout(hbox_diamonds)
        vbox.addWidget(self.diamond_count)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(default)
        hbox.addWidget(save)

        vbox.addLayout(hbox)

        self.board_width.valueChanged.connect(lcd_width.display)
        self.board_height.valueChanged.connect(lcd_height.display)
        self.rock_count.valueChanged.connect(lcd_rocks.display)
        self.diamond_count.valueChanged.connect(lcd_diamonds.display)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle('Options')
        self.show()

    def write_to_file(self):
        config = Config.get()

        config.properties.update({
            'username': self.usernameEdit.text(),
            'board_width': self.board_width.value(),
            'board_height': self.board_height.value(),
            'rock_count': self.rock_count.value(),
            'diamond_count': self.diamond_count.value()
        })

        config.save()

    def write_default_options(self):
        Config.get().destroy()


class HelpWindow(QtGui.QWidget):

    def __init__(self):
        super(HelpWindow, self).__init__()
        self.initUI()

    def initUI(self):
        with open('about.html') as f:
            text = f.read()
        label = QtGui.QLabel(self)
        label.setText(text)

        self.setGeometry(250, 100, 800, 600)
        self.setWindowTitle('Help')
        self.show()


class FormWidget(QtGui.QWidget):
    def __init__(self, parent, image_repository):
        super(FormWidget, self).__init__(parent)
        self.image_repository = image_repository
        self.initUI()

    def initUI(self):
        self.pic = QtGui.QLabel(self)
        self.new_game_button = QtGui.QPushButton("New Game")
        self.quit_button = QtGui.QPushButton("Quit")

        self.pic.setPixmap(self.image_repository.get_pixmap('boulder_dash', 500, 500, QtCore.Qt.KeepAspectRatio))
        self.pic.setScaledContents(True)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)

        vbox = QtGui.QVBoxLayout(self)

        vbox.addWidget(self.pic)
        vbox.addWidget(self.new_game_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.show()
