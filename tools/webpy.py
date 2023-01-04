
import webbrowser

def paginaweb():

	mensaje = """<html>
	<head><meta http-equiv="refresh" content="5"></head>
	<body><p>Hola Mundo!</p>
	<img src="/home/enriquelopez/Descargas/Flask/P5/grafica.jpg">
	<img src="grafica.jpg">
	</body>


	</html>"""

	return mensaje
	
def paginaweb2():
	#hi
	add=""
	f = open('../templates/index.html', 'w')
	add=add+"""<table class="default"><tr><th>Traps</th></tr>"""
	with open('../resultados.txt', 'r') as fichero:
		linea = fichero.readline()
		add=add+"""<tr><td>"""+linea+"""</td></tr>"""
		while linea != '':
			print(linea, end='')
			linea = fichero.readline()
			add=add+"""<tr><td>"""+linea+"""</td></tr>"""
    		
	add= add+"""</table>"""
	mensaje = """<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="refresh" content="3">
		<title>Monitoreo</title>
	</head>
	<body><center>
	<h1>Monitoreo</h1>
	<img src="{{url_for('static',filename='/grafica.jpg')}}" alt="Gráfica de la interface f 0/0">
	"""+add+"""
	</center>
	</body>
	</html>
 
>"""

	f.write(mensaje)
	f.close()

	
