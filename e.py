import urllib
import requests
import json

def topology_info():
	print '\n<----------------------------SUMMARY------------------------------>'
	data1 = requests.get("http://10.0.2.15:8080/wm/core/controller/summary/json")	
	dat1 = data1.json()
	number_of_switches = dat1 ["# Switches"]
	number_of_hosts = dat1 ["# hosts"]
	print '# Switches Connected: ', number_of_switches
	print '# Hosts Connected: ', number_of_hosts
	print '------------------------------------------------------------------\n'
	return( number_of_switches , number_of_hosts )

def switch_info ( number_of_switches , switch_dpids ):
	data = requests.get("http://10.0.2.15:8080/wm/core/controller/switches/json")
	dat = data.json()
	k=0
	for k in range( 0 , number_of_switches):
		DPID = dat [k]["switchDPID"]
		DPID = DPID.decode()
		switch_dpids.append(DPID)
	return(switch_dpids)

def host_info(number_of_hosts , hosts):
	a = requests.get("http://10.0.2.15:8080/wm/device/")
	b = a.json()
	for k in range( 0, number_of_hosts):		
		c = str(b["devices"][k]['ipv4'])
		if c != []:			
			hosts[str(c)] = str(b["devices"][k]["attachmentPoint"])
	return(hosts)

def switch_byte( number_of_switches, switch_dpids ):
	for k in range(0, number_of_switches):
		print switch_dpids[k]
		a = requests.get("http://10.0.2.15:8080/wm/core/switch/"+switch_dpids[k]+"/flow/json")
		b = a.json()
		print '\t Packet Count:', b["flows"][0]['packet_count']
		print '\t Cookie:', b["flows"][0]['cookie']
		print '\t byte count:', b["flows"][0]['byte_count']

try:
	number_of_switches , number_of_hosts = topology_info();
	switch_dpids = list()
	hosts = dict()
	switch_dpids = switch_info ( number_of_switches, switch_dpids ) ;
	hosts = host_info ( number_of_hosts , hosts );
	switch_byte( number_of_switches, switch_dpids );

except Exception as e:
	print'Error occured', e



#to access hosts info from dict
'''

	for k in range( 1, number_of_hosts-1):
		k = str(k)
		m = "[u'10.0.0."+ k +"']"
		print hosts[m]
'''
