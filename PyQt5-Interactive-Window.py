from PyQt5 import QtWidgets, uic
import sys
import time
import uuid
import random
import threading

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('C:/Users/vwimmer/Documents/Git/PyQT Test/test.ui', self)

		self.printbutton = self.findChild(QtWidgets.QPushButton, 'printButton') # Find the button
		self.printbutton.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
		self.printbutton.setEnabled(False)

		self.clearbutton = self.findChild(QtWidgets.QPushButton, 'clearButton')
		self.clearbutton.clicked.connect(self.clearButtonPressed)

		self.updatebutton = self.findChild(QtWidgets.QPushButton, 'updateButton')
		self.updatebutton.clicked.connect(self.updateButtonPressed)

		self.progressbar = self.findChild(QtWidgets.QProgressBar, 'updateProgress')
		self.progressbar.setValue(0)

		self.input = self.findChild(QtWidgets.QLineEdit, 'textInput')

		self.show()

	def printButtonPressed(self):
		# This is executed when the button is pressed
		if (self.input.text()) != "":
			print(self.input.text())

	def clearButtonPressed(self):
		self.progressbar.setValue(0)
		self.printbutton.setEnabled(False)
		self.input.clear()

	def updateButtonPressed(self):
		for x in range(101):
			self.progressbar.setValue(x)
			time.sleep(0.001)
		self.input.setText(my_random_string(50)) 
		self.printbutton.setEnabled(True)

def my_random_string(string_length=50):
	random = str(uuid.uuid4())
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length] # Return the random string.

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
