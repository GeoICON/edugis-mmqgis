# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_spatial_join_form.ui'
#
# Created: Sun Feb  1 18:43:50 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_spatial_join_form(object):
    def setupUi(self, mmqgis_spatial_join_form):
        mmqgis_spatial_join_form.setObjectName(_fromUtf8("mmqgis_spatial_join_form"))
        mmqgis_spatial_join_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_spatial_join_form.setEnabled(True)
        mmqgis_spatial_join_form.resize(440, 324)
        mmqgis_spatial_join_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_spatial_join_form)
        self.buttonBox.setGeometry(QtCore.QRect(150, 280, 160, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label.setGeometry(QtCore.QRect(10, 220, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_spatial_join_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 240, 321, 31))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_spatial_join_form)
        self.browseoutfile.setGeometry(QtCore.QRect(350, 240, 79, 31))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.targetlayer = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.targetlayer.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.targetlayer.setObjectName(_fromUtf8("targetlayer"))
        self.label_4 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 201, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.joinlayer = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.joinlayer.setGeometry(QtCore.QRect(10, 130, 241, 31))
        self.joinlayer.setObjectName(_fromUtf8("joinlayer"))
        self.spatialop = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.spatialop.setGeometry(QtCore.QRect(10, 80, 241, 31))
        self.spatialop.setObjectName(_fromUtf8("spatialop"))
        self.spatialop.addItem(_fromUtf8(""))
        self.spatialop.addItem(_fromUtf8(""))
        self.spatialop.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 108, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.fieldop = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.fieldop.setGeometry(QtCore.QRect(10, 180, 241, 31))
        self.fieldop.setObjectName(_fromUtf8("fieldop"))
        self.label_6 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 141, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.fieldnames = QtGui.QListWidget(mmqgis_spatial_join_form)
        self.fieldnames.setGeometry(QtCore.QRect(270, 80, 161, 131))
        self.fieldnames.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldnames.setObjectName(_fromUtf8("fieldnames"))
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        self.label_7 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_7.setGeometry(QtCore.QRect(270, 60, 108, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(mmqgis_spatial_join_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_spatial_join_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_spatial_join_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_spatial_join_form)

    def retranslateUi(self, mmqgis_spatial_join_form):
        mmqgis_spatial_join_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Spatial Join", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.outfilename.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "data.csv", None, QtGui.QApplication.UnicodeUTF8))
        self.browseoutfile.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Output Shape (Target) Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.spatialop.setItemText(0, QtGui.QApplication.translate("mmqgis_spatial_join_form", "Intersects", None, QtGui.QApplication.UnicodeUTF8))
        self.spatialop.setItemText(1, QtGui.QApplication.translate("mmqgis_spatial_join_form", "Within", None, QtGui.QApplication.UnicodeUTF8))
        self.spatialop.setItemText(2, QtGui.QApplication.translate("mmqgis_spatial_join_form", "Contains", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Data (Join) Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Spatial Operation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Attribute Operation", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.fieldnames.isSortingEnabled()
        self.fieldnames.setSortingEnabled(False)
        item = self.fieldnames.item(0)
        item.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        item = self.fieldnames.item(1)
        item.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Beta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.fieldnames.item(2)
        item.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Gamma", None, QtGui.QApplication.UnicodeUTF8))
        item = self.fieldnames.item(3)
        item.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Delta", None, QtGui.QApplication.UnicodeUTF8))
        item = self.fieldnames.item(4)
        item.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Epsilon", None, QtGui.QApplication.UnicodeUTF8))
        self.fieldnames.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(QtGui.QApplication.translate("mmqgis_spatial_join_form", "Fields", None, QtGui.QApplication.UnicodeUTF8))

