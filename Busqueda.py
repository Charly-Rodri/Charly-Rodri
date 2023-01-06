import shodan

SHODAN_API_KEY = "Poner la api aki"

api = shodan.Shodan(SHODAN_API_KEY)

try:

	#Busqueda con shodan
	result = api.search('apache')
	
	#Mostramos los resultados
	print 'Resultados encontrados:%s' % results['total']
	for result in results['marches']:
		print 'IP: %s' % result['ip:str']
		print result['data']
		print ''
except shodan.APIError, e:
	print 'Error: %s' % e
