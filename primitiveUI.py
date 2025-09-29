try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance

except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os

import importlib
from . import primitiveUtil as pritil
importlib.reload(pritil)

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'icons'))

class PrimitiveCreator(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(315,200)
		self.setWindowTitle('Primitive Creator')

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.primitive_listWidget = QtWidgets.QListWidget()
		self.primitive_listWidget.setIconSize(QtCore.QSize(60,60))
		self.primitive_listWidget.setSpacing(5)
		self.primitive_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
		self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)
		self.primitive_listWidget.setStyleSheet(
				'''background-color: #898989'''
			)

		self.main_layout.addWidget(self.primitive_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)

		self.name_label = QtWidgets.QLabel('NAME :')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('CREATE')
		self.create_button.clicked.connect(self.dorenameobj)	
		self.cancel_button = QtWidgets.QPushButton('CANCEL')
		self.cancel_button.clicked.connect(self.close)	
		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)

		self.create_button.setStyleSheet(
				'''background-color: #40826D'''
			)

		self.cancel_button.setStyleSheet(
				'''background-color: #824044'''
			)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['cone', 'sphere', 'torus','cube']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
			self.primitive_listWidget.addItem(item)

	def dorenameobj(self):
		name = self.name_lineEdit.text()
		item =  self.primitive_listWidget.currentItem()
		if item:  
			prim_name = item.text()
		pritil.createobj(name,prim_name)


def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreator(parent=ptr)
	ui.show()
