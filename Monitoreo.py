from flask import Flask,render_template
import pysnmp
import paramiko, getpass, time
import snmpi
import pexpect
import os
import threading
import matplotlib.pyplot as plt
import datetime
import time
import shutil
from static import graficas
import webbrowser
import webpy
import pysnmp
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import logging
from os import remove
from os import path
import shutil

puntosx=[]
puntosy=[]
rectas=[]

class Worker(threading.Thread):
	import pysnmp
	from pysnmp.entity import engine, config
	from pysnmp.carrier.asyncore.dgram import udp
	from pysnmp.entity.rfc3413 import ntfrcv
	estado = 20.0
	def getEstado(self):
		return self.estado
	def cbFun(self,snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
		result = {}
		for name, val in varBinds:   
			tmp = str(val)
			#print(tmp)
			if tmp == "Interface GigabitEthernet2/0, changed state to up":
				self.estado = "UP"
				print("Estado de la interfaz: "+tmp)
				result['Tiempo'] = datetime.datetime.utcnow().isoformat()
				
				result['Estado'] = self.estado
				with open('/home/enriquelopez/Descargas/Flask/P5/resultados.txt','a') as f:
					f.write(str(result))
					f.write('\n')
				webpy.paginaweb2()
			if tmp == "administratively down":
				self.estado = "DOWN"
				print("Estado de la interfaz: "+tmp)
				result['Tiempo'] = datetime.datetime.utcnow().isoformat()
				
				result['Estado'] = self.estado
				with open('/home/enriquelopez/Descargas/Flask/P5/resultados.txt', 'a') as f:
					f.write(str(result))
					f.write('\n')
				webpy.paginaweb2()
		
	def run(self):
		snmpEngine = engine.SnmpEngine()
		TrapAgentAddress = '192.168.0.10';
		Port = 162;
		config.addTransport(snmpEngine, udp.domainName + (1,), udp.UdpTransport().openServerMode((TrapAgentAddress, Port)))
		config.addV1System(snmpEngine, 'cadena', 'cadena')
		ntfrcv.NotificationReceiver(snmpEngine, self.cbFun)
		snmpEngine.transportDispatcher.jobStarted(1)
		try:
			snmpEngine.transportDispatcher.runDispatcher()
		except:
			snmpEngine.transportDispatcher.closeDispatcher()
			raise


app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def s():
	return "monitoreo"

@app.route('/monitoreo')
def route():

	# Interface OID
	fa0_0_in_oct = '1.3.6.1.2.1.2.2.1.10.4'
	host = '192.168.1.1'
	community = 'cadena'
	suma=0
	
	global rectas 
	cont=1
	bandera=True
	
	hilo = Worker()
	hilo.start()
		
		
	while True:#cont < 10:
		if(cont==1):
			result = int(snmpi.snmp_query(host, community, fa0_0_in_oct))
			
		else:
			aux = result
			result = int(snmpi.snmp_query(host, community, fa0_0_in_oct))
			#print(result)
			paquetes =  result - aux
			if paquetes <300 :
				if bandera:
					rectas.append(cont*5)
					bandera = False
			else:
				if bandera == False:
					rectas.append(cont*5)
					bandera = True
			
			global puntosx
			global puntosy 
			  
			
			puntosy.append(paquetes)
			puntosx.append(cont*5)
		cont = cont+1
		
		
		print(puntosx)
		print(puntosy)
		if cont>2:
			graficas.grafica(puntosx,puntosy,rectas)
		time.sleep(5)
		
	return "Monitoreo Finalizado"
	
@app.route('/visualizar')
def visualizar():

	GRA = os.path.join(app.config['UPLOAD_FOLDER'],'grafica.jpg')
	return render_template("index.html", user_image=GRA)

@app.route('/reiniciar')
def reiniciar():
	if path.exists("/home/enriquelopez/Descargas/Flask/P5/resultados.txt"):
		print("Existe RES")
		remove("/home/enriquelopez/Descargas/Flask/P5/resultados.txt")
		shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/resultados1.txt', '/home/enriquelopez/Descargas/Flask/P5/resultados.txt')

	if path.exists("/home/enriquelopez/Descargas/Flask/P5/templates/index.html"):
		print("Existe HTML")
		remove('/home/enriquelopez/Descargas/Flask/P5/templates/index.html')
		shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/templates/index1.html', '/home/enriquelopez/Descargas/Flask/P5/templates/index.html')     
	
	if path.exists("/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg"):
		remove('/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg')
		shutil.copy2('/home/enriquelopez/Descargas/Flask/P5/static/grafica1.jpg', '/home/enriquelopez/Descargas/Flask/P5/static/grafica.jpg')        
	
	global puntosx
	global puntosy  
	global rectas    
				
	puntosy=[]
	puntosx=[]
	rectas=[]
	graficas.clear()
	return "Reinicio"

@app.route('/monitoreo2')
def monitoreo2():

	hilo = Monitoreos()
	hilo.start()
	

	GRA = os.path.join(app.config['UPLOAD_FOLDER'],'grafica.jpg')
	return render_template("index.html", user_image=GRA)
	

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



