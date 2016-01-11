from PyQt4 import QtGui


class ImageRepository(object):
    def __init__(self):
        self.pixmaps = {}
        self.icons = {}

    def get_pixmap(self, name, *scaled_args):
        if name not in self.pixmaps:
            path = 'images/{0}.png'.format(name)
            self.pixmaps[name] = QtGui.QPixmap(path).scaled(*scaled_args)
        return self.pixmaps[name]

    def get_icon(self, name):
        if name not in self.icons:
            path = 'images/{0}.png'.format(name)
            self.icons[name] = QtGui.QIcon(path)
        return self.icons[name]
