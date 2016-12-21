class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.publi.clicked.connect(self.publi_clicked)
	def publi_clicked(self):
		# Insertar texto en QLabel
		self.ver.setText("hola")
		# Insertar archivo desde url
		self.vista.load(QUrl('https://github.com/enrriquemicro/banner/blob/master/banner2.png?raw=true'))
