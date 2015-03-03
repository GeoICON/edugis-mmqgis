# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_buffers_form.ui'
#
# Created: Wed Mar 04 06:20:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mmqgis_buffers_form(object):
    def setupUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setObjectName(_fromUtf8("mmqgis_buffers_form"))
        mmqgis_buffers_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_buffers_form.setEnabled(True)
        mmqgis_buffers_form.resize(382, 339)
        mmqgis_buffers_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_buffers_form)
        self.buttonBox.setGeometry(QtCore.QRect(9, 300, 361, 31))
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(_fromUtf8("height: 32px;\n"
""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_buffers_form)
        self.label.setGeometry(QtCore.QRect(10, 220, 271, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_buffers_form)
        self.filename.setGeometry(QtCore.QRect(10, 240, 271, 31))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_buffers_form)
        self.browse.setGeometry(QtCore.QRect(290, 240, 80, 31))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_buffers_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 351, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.buffershape = QtGui.QComboBox(mmqgis_buffers_form)
        self.buffershape.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.buffershape.setObjectName(_fromUtf8("buffershape"))
        self.label_6 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 171, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.radius = QtGui.QLineEdit(mmqgis_buffers_form)
        self.radius.setGeometry(QtCore.QRect(10, 90, 171, 31))
        self.radius.setObjectName(_fromUtf8("radius"))
        self.label_8 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 171, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.radiusunit = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusunit.setGeometry(QtCore.QRect(200, 90, 171, 31))
        self.radiusunit.setObjectName(_fromUtf8("radiusunit"))
        self.label_9 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_9.setGeometry(QtCore.QRect(200, 70, 171, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_7.setGeometry(QtCore.QRect(200, 130, 171, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radiusattribute = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusattribute.setGeometry(QtCore.QRect(200, 150, 171, 31))
        self.radiusattribute.setObjectName(_fromUtf8("radiusattribute"))
        self.selectedonly = QtGui.QCheckBox(mmqgis_buffers_form)
        self.selectedonly.setGeometry(QtCore.QRect(10, 190, 361, 20))
        self.selectedonly.setObjectName(_fromUtf8("selectedonly"))

        self.retranslateUi(mmqgis_buffers_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_buffers_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_buffers_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_buffers_form)

    def retranslateUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setWindowTitle(_translate("mmqgis_buffers_form", "Create Buffers", None))
        self.label.setText(_translate("mmqgis_buffers_form", "Output Shapefile", None))
        self.filename.setText(_translate("mmqgis_buffers_form", "temp.shp", None))
        self.browse.setText(_translate("mmqgis_buffers_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_buffers_form", "Source Layer", None))
        self.label_6.setText(_translate("mmqgis_buffers_form", "Buffer Shape", None))
        self.label_8.setText(_translate("mmqgis_buffers_form", "Radius", None))
        self.label_9.setText(_translate("mmqgis_buffers_form", "Measurement Unit", None))
        self.label_7.setText(_translate("mmqgis_buffers_form", "Radius Attribute", None))
        self.selectedonly.setText(_translate("mmqgis_buffers_form", "Selected Features Only", None))

