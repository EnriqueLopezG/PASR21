from flask import Flask,render_template

import os
import webbrowser
import Monitoreo

from os import remove
from os import path



app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def paginaPrincipal():
	return render_template("main.html")

@app.route('/test')
def test():

    #webbrowser.open("/templates/index.html", new=2, autoraise=True)
    webbrowser.open_new_tab("https://google.com")
    return "Prueba finalizada"


@app.route('/monitoreo/<elemento>/<interfaz>/<numerorepeticiones>')
def route(elemento,interfaz,numerorepeticiones):

    webbrowser.open("/templates/index.html", new=2, autoraise=True)
    Monitoreo.Monitoreo()
    GRA = os.path.join(app.config['UPLOAD_FOLDER'], 'grafica.jpg')
    return "Monitoreo Finalizado"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



