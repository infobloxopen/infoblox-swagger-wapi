#!/usr/bin/python
import sys

print(sys.argv[1])


l = ["dns.json", "dhcp.json", "ipam.json",  "grid.json" , "dtc.json",  "rpz.json" , "parental_control.json" , "discovery.json" , "microsoft.json" , "outbound.json" ,  "users.json" , "threat_analytics.json" , "miscellaneous.json","vlan.json"]

for i in l:
	f = open(i,"r")
	contents = f.readlines()
	f.close()
	#print(type(contents[0]))
	contents[0] = contents[0][:1]+"\"servers\":[{\"url\":\"https://"+sys.argv[1]+"\"}],"+contents[0][1:]
	f = open(i,"w")
	contents = "".join(contents)
	f.write(contents)
	f.close()

print("copy complete")


