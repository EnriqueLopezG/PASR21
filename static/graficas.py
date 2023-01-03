import matplotlib.pyplot as plt



def grafica(x,y,rectas):

	print("Haciendo grafica")
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.xlabel('Tiempo')
	plt.ylabel('No. Paquetes')
	plt.ylim([0, 1000])
	
	for n in rectas:
		plt.vlines(x=n, ymin=0, ymax=1000)
	
	plt.savefig("static/grafica.jpg", bbox_inches='tight')
	plt.close()
	
def clear():
	plt.clf()
