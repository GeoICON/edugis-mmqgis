# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_hub_distance_form.ui'
#
# Created: Sun Feb  1 18:43:48 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mmqgis_hub_distance_form(object):
    def setupUi(self, mmqgis_hub_distance_form):
        mmqgis_hub_distance_form.setObjectName(_fromUtf8("mmqgis_hub_distance_form"))
        mmqgis_hub_distance_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_hub_distance_form.setEnabled(True)
        mmqgis_hub_distance_form.resize(373, 309)
        mmqgis_hub_distance_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_hub_distance_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 270, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label.setGeometry(QtCore.QRect(10, 210, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 171, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_hub_distance_form)
        self.filename.setGeometry(QtCore.QRect(10, 230, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_hub_distance_form)
        self.browse.setGeometry(QtCore.QRect(280, 230, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.hubslayerbox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.hubslayerbox.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.hubslayerbox.setObjectName(_fromUtf8("hubslayerbox"))
        self.sourcelayerbox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.sourcelayerbox.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayerbox.setObjectName(_fromUtf8("sourcelayerbox"))
        self.label_4 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 161, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.nameattributebox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.nameattributebox.setGeometry(QtCore.QRect(10, 130, 351, 27))
        self.nameattributebox.setObjectName(_fromUtf8("nameattributebox"))
        self.label_5 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.outputtype = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.outputtype.setGeometry(QtCore.QRect(10, 180, 161, 27))
        self.outputtype.setObjectName(_fromUtf8("outputtype"))
        self.label_6 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 171, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.measurement = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.measurement.setGeometry(QtCore.QRect(200, 180, 161, 27))
        self.measurement.setObjectName(_fromUtf8("measurement"))
        self.label_7 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_7.setGeometry(QtCore.QRect(200, 160, 161, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(mmqgis_hub_distance_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_hub_distance_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_hub_distance_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_hub_distance_form)

    def retranslateUi(self, mmqgis_hub_distance_form):
        mmqgis_hub_distance_form.setWindowTitle(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Distance to Nearest Hub", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Destination Hubs Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.filename.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "distances.shp", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Source Points Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Hub Layer Name Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Output Shape Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("mmqgis_hub_distance_form", "Measurement Unit", None, QtGui.QApplication.UnicodeUTF8))

