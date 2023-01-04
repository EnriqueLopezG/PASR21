from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

cmdGen = cmdgen.CommandGenerator()



def snmp_query(host, community, oid):
		errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
		    cmdgen.CommunityData(community),
		    cmdgen.UdpTransportTarget((host, 161)),
		    oid
		)
		
		# Revisamos errores e imprimimos resultados
		if errorIndication:
		    print(errorIndication)
		else:
		    if errorStatus:
		        print('%s at %s' % (
		            errorStatus.prettyPrint(),
		            errorIndex and varBinds[int(errorIndex)-1] or '?'
		            )
		        )
		    else:
		        for name, val in varBinds:
		            return(str(val))
