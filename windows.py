from PyQt4 import QtGui, QtCore
from widgets import OptionsWindow, HelpWindow, FormWidget
from frames import Board


class MainWindow(QtGui.QMainWindow):

    def __init__(self, image_repository):
        super(MainWindow, self).__init__()
        self.image_repository = image_repository
        self.initUI()

    def initUI(self):
        optionAction = QtGui.QAction('&Options', self)
        optionAction.triggered.connect(self.show_options_window)

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        self.connect(exitAction, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        helpAction = QtGui.QAction('&About', self)
        helpAction.setShortcut('F1')
        helpAction.triggered.connect(self.show_help_window)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu('&Help')
        fileMenu.addAction(optionAction)
        fileMenu.addAction(exitAction)
        helpMenu.addAction(helpAction)

        self.central_widget = QtGui.QStackedWidget(self)
        self.setCentralWidget(self.central_widget)
        self.form_widget = FormWidget(self, self.image_repository)
        self.central_widget.addWidget(self.form_widget)

        self.form_widget.new_game_button.clicked.connect(self.play_window)
        self.form_widget.quit_button.clicked.connect(self.close)

        self.statusbar = self.statusBar()

        self.setGeometry(200, 50, 900, 700)
        self.setWindowTitle('Boulder Dash')
        self.setWindowIcon(self.image_repository.get_icon('boulder_dash_icon'))
        self.show()

    def show_help_window(self):
        self.helpWindow = HelpWindow()

    def show_options_window(self):
        self.optionsWindow = OptionsWindow()

    def form_window(self):
        self.central_widget.setCurrentWidget(self.form_widget)

    def play_window(self):
        self.play_widget = Board(self, self.image_repository)
        self.play_widget.status_bar[str].connect(self.statusbar.showMessage)
        self.central_widget.addWidget(self.play_widget)
        self.central_widget.setCurrentWidget(self.play_widget)

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
