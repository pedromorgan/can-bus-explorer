

try:
    from PySide2 import QtCore, QtWidgets, QtGui
    from PySide2.QtCore import Qt
    from PySide2.QtCore import Signal as pyqtSignal


except:

    from PyQt5 import QtCore, QtWidgets, QtGui
    from PyQt5.QtCore import Qt
    from PyQt5.QtCore import pyqtSignal
    # from PyQt5.QtCore import pyqtProperty as Property
else:

    raise ImportError("Can find qt engine")