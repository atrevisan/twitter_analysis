# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_fetch_tweets.ui'
#
# Created: Fri Dec 12 10:12:07 2014
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

class Ui_widgetFetchTweets(object):
    def setupUi(self, widgetFetchTweets):
        widgetFetchTweets.setObjectName(_fromUtf8("widgetFetchTweets"))
        widgetFetchTweets.resize(800, 500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(widgetFetchTweets)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEditQuerry = QtGui.QLineEdit(widgetFetchTweets)
        self.lineEditQuerry.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEditQuerry.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditQuerry.setObjectName(_fromUtf8("lineEditQuerry"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lineEditQuerry)
        self.pushButtonSearch = QtGui.QPushButton(widgetFetchTweets)
        self.pushButtonSearch.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonSearch.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("mg.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonSearch.setIcon(icon)
        self.pushButtonSearch.setObjectName(_fromUtf8("pushButtonSearch"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButtonSearch)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem)
        self.lineEditTweetsCount = QtGui.QLineEdit(widgetFetchTweets)
        self.lineEditTweetsCount.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEditTweetsCount.setObjectName(_fromUtf8("lineEditTweetsCount"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.lineEditTweetsCount)
        self.pushButtonStopSearching = QtGui.QPushButton(widgetFetchTweets)
        self.pushButtonStopSearching.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonStopSearching.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonStopSearching.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonStopSearching.setIcon(icon1)
        self.pushButtonStopSearching.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonStopSearching.setObjectName(_fromUtf8("pushButtonStopSearching"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.pushButtonStopSearching)
        self.label = QtGui.QLabel(widgetFetchTweets)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditOutputFile = QtGui.QLineEdit(widgetFetchTweets)
        self.lineEditOutputFile.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditOutputFile.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditOutputFile.setObjectName(_fromUtf8("lineEditOutputFile"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditOutputFile)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(widgetFetchTweets)
        QtCore.QMetaObject.connectSlotsByName(widgetFetchTweets)

    def retranslateUi(self, widgetFetchTweets):
        widgetFetchTweets.setWindowTitle(_translate("widgetFetchTweets", "Fetch Tweets", None))
        self.label.setText(_translate("widgetFetchTweets", "Output file:", None))
