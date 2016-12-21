#class MyWindowClass(QtGui.QMainWindow, form_class):
	#def __init__(self, parent=None):
		#QtGui.QMainWindow.__init__(self, parent)
		#self.publi.clicked.connect(self.publi_clicked)
	#def publi_clicked(self):
	def publicidad():
		# Insertar texto en QLabel
		ver.setText("hola")
		# Insertar archivo desde url
		vista.load(QUrl('https://github.com/enrriquemicro/banner/blob/master/banner2.png?raw=true'))
