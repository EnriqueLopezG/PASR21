from os import remove
from os import path
import shutil
if path.exists("/home/enriquelopez/Descargas/Flask/P5/resultados.txt"):
	print("Existe RES")
	remove("/home/enriquelopez/Descargas/Flask/P5/resultados.txt")
	shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/resultados1.txt', '/home/enriquelopez/Descargas/Flask/P5/resultados.txt')

if path.exists("/home/enriquelopez/Descargas/Flask/P5/templates/index.html"):
	print("Existe HTML")
	remove('/home/enriquelopez/Descargas/Flask/P5/templates/index.html')
	shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/templates/index1.html', '/home/enriquelopez/Descargas/Flask/P5/templates/index.html')

if path.exists("/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg"):
		print("Existe IMG")
		remove('/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg')
		shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/static/grafica1.jpg', '/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg')    
