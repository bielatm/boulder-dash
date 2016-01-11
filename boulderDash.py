#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui
from image_repository import ImageRepository
from windows import MainWindow


def main():
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    image_repository = ImageRepository()
    ex = MainWindow(image_repository)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
