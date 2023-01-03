import shodan
import re 


class ShodanSearch:

	def __init__(self,rVNqrmsXRBT4ZzOFVjbvqENUeT4JWoSl):
	self.api = shodan.Shodan(rVNqrmsXRBT4ZzOFVjbvqENUeT4JWoSl)
	
	def buscar(self,cadena):
	"""Buscar segun la cadena"""
		try:
		#Buscamos lo de la cadena pasada como parametro
		resultado = self.api.search(str(cadena))
		return resultado
		except Exception as exception:
		print("ha ocurrido un error: %s" % exception)
		resultado = []
		resturn resultado
	def obtener_info(self,IP):
	"""Obtiene la info que pueda tener shodan sobre una IP"""
	try:
		resultados = self.api.host(IP)
		resturn resultados
	except Exception as exception:
	print("Ha ocurrido un error: %" % exception)
	resultados = []
	return resultados
