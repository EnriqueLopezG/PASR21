from flask import Flask
import paramiko, getpass, time
import pexpect
app = Flask(__name__)

@app.route('/R4/enrutar/<enrutamiento>')
def route(enrutamiento):
	devices = {'R4': {'prompt': 'R4#', 'ip': '10.0.1.254'}}
	username = 'admin'
	password = 'admin'

	if enrutamiento == 'estatico':
		comandos=open("R4estatico.txt","r")
	elif enrutamiento =='rip':
		comandos=open("R4rip.txt","r")
	elif enrutamiento =='ospf':
		comandos=open("R4ospf.txt","r")
	elif enrutamiento =='global':
		comandos=open("r4com.txt","r")
	else:
		return "Ingrese un enrutamiendo Valido"
	 
	
	 
	

	for device in devices.keys(): 
		device_prompt = devices[device]['prompt']
		child = pexpect.spawn('telnet ' + devices[device]['ip'])
		child.expect('Username:')
		child.sendline(username)
		child.expect('Password:')
		child.sendline(password)
		child.expect(device_prompt)
		
		for linea in comandos:
			print(linea)
			child.sendline(linea)
		
		#child.sendline('show version | i V')
		#child.expect(device_prompt)
		print(child.before)
	#    print(str(child))
	#    print(child.after)
		child.sendline('exit')
		comandos.close()

	return 'Configuracion %s realiazada'% enrutamiento

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




