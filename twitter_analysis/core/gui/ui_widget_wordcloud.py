# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_wordcloud.ui'
#
# Created: Sat Jan 10 10:50:02 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_widget_wordcloud(object):
    def setupUi(self, widget_wordcloud):
        widget_wordcloud.setObjectName(_fromUtf8("widget_wordcloud"))
        widget_wordcloud.resize(839, 709)
        self.label_wordcloud = QtGui.QLabel(widget_wordcloud)
        self.label_wordcloud.setGeometry(QtCore.QRect(20, 50, 801, 600))
        self.label_wordcloud.setStyleSheet(_fromUtf8(""))
        self.label_wordcloud.setText(_fromUtf8(""))
        self.label_wordcloud.setObjectName(_fromUtf8("label_wordcloud"))

        self.retranslateUi(widget_wordcloud)
        QtCore.QMetaObject.connectSlotsByName(widget_wordcloud)

    def retranslateUi(self, widget_wordcloud):
        widget_wordcloud.setWindowTitle(_translate("widget_wordcloud", "Form", None))

