###################################################################################################
#                                      Copyright 2020                                             #
#                       Author: Vedant Sethia <vsethia@infoblox.com>                              #
#    For any issues/suggestions please write to Krishna Vasudevan <kvasudevan@infoblox.com>       #
###################################################################################################

#Automation script for for creating a JSON Open-API Specification file for Infoblox REST APIs

#libraries
import requests
import json

#function for calling the REST API
def get_wapi_call(ip,username,password,wapi_object):
	requests.packages.urllib3.disable_warnings()
	base_url = "https://{}/wapi/{}/".format(ip,wapi_version)
	url = base_url + wapi_object
	response = requests.request("GET", url, auth=(username,password), verify = False)
	js = json.loads(response.text)	
	return js
	
#definition for GET
def create_get_definition(doc, obj, tag, parameters,dict_val):

	#get definition
	dict_val["get"] = {"tags":[tag]}

	parameters_list = []
	#parameters
	parameters_list.append({"name":"_return_fields","in":"query","required":False,"description":"Enter the field names followed by comma","schema": {"type":"string"}})
	parameters_list.append({"name":"_return_fields+","in":"query","required":False,"description":"Enter the field names followed by comma, this returns the required fields along with the default fields","schema": {"type":"string"}})
	parameters_list.append({"name":"_max_results","in":"query","required":False,"description":"Enter the number of results to be fetched","schema": {"type":"integer","minimum":1}})
	parameters_list.append({"name":"_return_as_object","in":"query","required":False,"description":"Select 1 if result is required as a object","schema": {"type":"integer","enum":[0,1],"default":0}})
	parameters_list.append({"name":"_paging","in":"query","required":False,"description":"Select 1 if paging is required. If SET, _max_results and _return_as_object must be entered.","schema": {"type":"integer","enum":[0,1],"default":0}})
	parameters_list.append({"name":" _page_id","in":"query","required":False,"description":"Enter the page ID for fetching next page","schema": {"type":"string"}})


	for i in parameters:
		if('s' in i["supports"]):
			parameters_list.append({"name":i["name"],"in":"query","required":False,"description":"Enter the value of the field","schema": {"type":"string"}})

	dict_val["get"]["parameters"] = parameters_list
	
	#response
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses ={"200":{"description": "OK", "content": {"application/json": { "schema": {"$ref" : "#/components/schemas/"+name}}}}}
	dict_val["get"]["responses"] = responses

	#security
	dict_val["get"]["security"] = [{"basicAuth" : []}]


#definition for GET by reference
def create_get_by_reference_definition(doc,obj,tag,parameters,dict_val):
	#get definition
	dict_val["get"] = {"tags":[tag]}

	parameters_list = []
	#parameters
	parameters_list.append({"name":""+tag+"_reference","in":"path","required":True,"description":"Enter the reference for "+tag,"schema": {"type":"string", "example": "resourceID:resourceName"}})
	parameters_list.append({"name":"_return_fields","in":"query","required":False,"description":"Enter the field names followed by comma","schema": {"type":"string"}})
	parameters_list.append({"name":"_return_fields+","in":"query","required":False,"description":"Enter the field names followed by comma, this returns the required fields along with the default fields","schema": {"type":"string"}})
	parameters_list.append({"name":"_return_as_object","in":"query","required":False,"description":"Select 1 if result is required as a object","schema": {"type":"integer","enum":[0,1],"default":0}})
	dict_val["get"]["parameters"] = parameters_list

	#response
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses ={"200":{"description": "OK", "content": {"application/json": { "schema": {"$ref" : "#/components/schemas/"+name}}}}}
	dict_val["get"]["responses"] = responses

	#security
	dict_val["get"]["security"] = [{"basicAuth" : []}]



#definition for POST
def create_post_definition(doc,obj,tag,parameters,dict_val):
	#post definition
	dict_val["post"] = {"tags":[tag]}

	#parameters
	parameters_list = [{"name":"_return_fields","in":"query","required":False,"description":"Enter the field names followed by comma","schema": {"type":"string"}}]
	dict_val["post"]["parameters"] = parameters_list

	#requestBody
	properties_dict = {}
	for i in parameters:
		if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
			continue		
		elif('w' in str(i["supports"])):
			properties_dict[i["name"]] = {}
			properties_dict[i["name"]]["type"] = "string"
			if(i["type"][0] == "enum"):
				properties_dict[i["name"]]["example"] = str(i["enum_values"])
			elif(i["is_array"] == True):	
				if("schema" in i.keys()):
					temp = []
					temp.append({})
					for j in i['schema']['fields']:
						a = j['name']
						b = j['type'][0]
						temp[0][a] = b
					properties_dict[i["name"]]["example"] = str(temp)
				else:
					properties_dict[i["name"]]["example"] = str(i["type"][0])
			else:
				properties_dict[i["name"]]["example"] = str(i["type"][0])
	dict_val["post"]["requestBody"] = {"description":"Enter the request body here","required":True,"content":{"application/json": {"schema": {"type":"object","properties": properties_dict}}}}
	
	#response
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses ={"201":{"description": "OK", "content": {"application/json": { "schema": {"$ref" : "#/components/schemas/"+name}}}}}
	dict_val["post"]["responses"] = responses

	#security
	dict_val["post"]["security"] = [{"basicAuth" : []}]




#definition for PUT
def create_put_definition(doc,obj,tag,parameters,dict_val):
	#put definition
	dict_val["put"] = {"description":"Update the "+tag+" resource","tags":[tag]}

	#parameters
	parameters_list = []
	parameters_list.append({"name":""+tag+"_reference","in":"path","required":True,"description":"Enter the reference for "+tag,"schema": {"type":"string", "example": "resourceID:resourceName"}})
	parameters_list.append({"name":"_return_fields","in":"query","required":False,"description":"Enter the field names followed by comma","schema": {"type":"string"}})
	dict_val["put"]["parameters"] = parameters_list

	#requestBody
	properties_dict = {}
	for i in parameters:
		if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
			continue		
		elif('u' in str(i["supports"])):
			properties_dict[i["name"]] = {}
			properties_dict[i["name"]]["type"] = "string"
			if(i["type"][0] == "enum"):
				properties_dict[i["name"]]["example"] = str(i["enum_values"])			
			elif(i["is_array"] == True):	
				if("schema" in i.keys()):
					temp = []
					temp.append({})
					for j in i['schema']['fields']:
						a = j['name']
						b = j['type'][0]
						temp[0][a] = b
					properties_dict[i["name"]]["example"] = str(temp)
				else:
					properties_dict[i["name"]]["example"] = str(i["type"][0])
			else:
				properties_dict[i["name"]]["example"] = str(i["type"][0])
	dict_val["put"]["requestBody"] = {"description":"Enter the request body here","required":True,"content":{"application/json": {"schema": {"type":"object","properties": properties_dict}}}}


	#response
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses ={"200":{"description": "OK", "content": {"application/json": { "schema": {"$ref" : "#/components/schemas/"+name}}}}}
	dict_val["put"]["responses"] = responses

	#security
	dict_val["put"]["security"] = [{"basicAuth" : []}]




#definition for DELETE
def create_delete_definition(doc, obj, tag,dict_val):
	#delete definition
	dict_val["delete"] = {"description":"Delete the "+tag+" resource","tags":[tag]}

	#parameters
	parameters_list = []
	parameters_list.append({"name":""+tag+"_reference","in":"path","required":True,"description":"Enter the reference for "+tag,"schema": {"type":"string", "example": "resourceID:resourceName"}})
	dict_val["delete"]["parameters"] = parameters_list


	#response
	responses = {"200":{"description": "OK", "content": {"application/json": { "schema": {"type":"object", "properties" :{ "$ref" : {"type":"string","description":"Reference of the deleted string"}}}}}}}
	dict_val["delete"]["responses"] = responses

	#security
	dict_val["delete"]["security"] = [{"basicAuth" : []}]


#definition for Function calls
def create_post_function_definition(doc,obj,tag,parameters,dict_val):
	name = []
	for i in parameters:
		name.append(i["name"])

	#Function call definition
	dict_val["post"] = {"description":"Function calls","tags":[tag]}	

	#parameters
	parameters_list = []
	parameters_list.append({"name":""+tag+"_reference","in":"path","required":True,"description":"Enter the reference for "+tag,"schema": {"type":"string", "example": "resourceID:resourceName"}})
	parameters_list.append({"name":"_function","in":"query","required":True,"description":"Select the function","schema": {"type":"string", "enum": name}})
	dict_val["post"]["parameters"] = parameters_list

	#requestBody
	dict_val["post"]["requestBody"] = {"description":"Enter the request body here","required":True,"content":{"application/json": {"schema": {"type":"object","properties": {}}}}}

	#response
	name = tag
	if(':' in name):
		name = name.replace(':','_')

	prop1 = {}
	prop2 = {}
	for i in parameters:
		if (i["schema"]["input_fields"]):
			temp = {}
			for j in i["schema"]["input_fields"]:
				if(j["type"][0] == "enum"):
					temp[j["name"]] = j["enum_values"]
				else:
					temp[j["name"]] = j["type"][0]
			prop2[i["name"]] = {"type": "string", "example": temp}
	if(prop2 == ""):
		responses = {"200":{"description": "OK", "content": {"application/json": { "schema": {"type":"object", "properties" : prop1}}}}}
	else:
		responses = {"200":{"description": "OK", "content": {"application/json": { "schema": {"type":"object", "properties" : prop2}}}}}
	dict_val["post"]["responses"] = responses	

	#security
	dict_val["post"]["security"] = [{"basicAuth" : []}]




#creates the schema for all the objects
def create_schema_reference(doc,parameters_dict,schema_dict):
	for key in parameters_dict:
		head = key
		if(":" in head):
			head = head.replace(":","_")


		temp_dict = {}
		#creating schema with swagger data type
		valid = ['array', 'boolean', 'integer', 'number', 'object', 'string','uint','bool','enum']
		for i in parameters_dict[key]:
			if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
				continue
			else:
				temp_dict[i["name"]] = {}
				if(i['type'][0] in valid):
					if(i['type'][0] == "uint"):
						temp_dict[i["name"]]["type"] = "integer"
						temp_dict[i["name"]]["example"] = "integer"
					elif(i['type'][0] == "bool"):
						temp_dict[i["name"]]["type"] = "boolean"
						temp_dict[i["name"]]["example"] = "boolean"
					elif(i['type'][0] == "enum"):
						temp_dict[i["name"]]["type"] = "string"
						temp_dict[i["name"]]["enum"] = i["enum_values"]
					else:
						temp_dict[i["name"]]["type"] = i["type"][0]
				else:
					temp_dict[i["name"]]["type"] = "string"
					temp_dict[i["name"]]["enum"] = [i["type"][0]]				

				#escape code for quotes in documentation
				temp = list(i['doc'])	
				for j in range(0,len(temp)):
					if(temp[j] == "\""):
						temp[j] = ""
				des = ""
				for j in temp:
					des = des + j
						
				temp_dict[i["name"]]["description"] = des
		schema_dict[head] = {"type" : "object","properties" : temp_dict}


#creates the introduction section for WAPI Swagger definition
def create_introduction(doc,ip,main_dict):
	main_dict["openapi"] = "3.0.0"
	main_dict["info"] = {"description":"Sample WAPI Documentation","version":""+wapi_version+"","title":"Infoblox WAPI"}
	main_dict["info"]["license"] = {"name":"Infoblox License","url":"https://www.infoblox.com/"}
	main_dict["info"]["contact"] = {"name":"Krishna","email":"kvasudevan@infoblox.com"}
	#main_dict["servers"] = []

	#for i in ip:
	#	main_dict["servers"].append({"url":"https://"+i})


#creates the paths section for WAPI Swagger definition
def create_path(doc,ip,main_dict):
	main_dict["paths"] = {}
	schema = get_wapi_call(ip[0],'admin','infoblox','?_schema')
	list_objects = schema['supported_objects']      #list of all supported objects as a list 

	res = {"rpz": ["allrpzrecords", "orderedresponsepolicyzones", "record:rpz:a", "record:rpz:aaaa", "record:rpz:aaaa:ipaddress", "record:rpz:a:ipaddress", "record:rpz:cname", "record:rpz:cname:clientipaddress", "record:rpz:cname:clientipaddressdn", "record:rpz:cname:ipaddress", "record:rpz:cname:ipaddressdn", "record:rpz:mx", "record:rpz:naptr", "record:rpz:ptr", "record:rpz:srv", "record:rpz:txt", "outbound:cloudclient", "taxii"]
	,"dns": ["grid:dns", "member:dns", "allrecords", "bulkhost", "record:host", "record:a", "record:aaaa", "record:alias", "record:caa", "record:cname", "record:dhcid", "record:dname", "record:dnskey", "record:ds", "record:dtclbdn", "record:host_ipv4addr", "record:host_ipv6addr", "record:mx", "record:naptr", "record:ns", "record:nsec", "record:nsec3", "record:nsec3param", "record:ptr", "record:rrsig", "record:srv", "record:tlsa", "record:txt", "record:unknown", "recordnamepolicy", "ruleset", "sharedrecord:a", "sharedrecord:aaaa", "sharedrecord:cname", "sharedrecord:mx", "sharedrecord:srv", "sharedrecord:txt", "sharedrecordgroup", "view", "zone_auth", "zone_auth_discrepancy", "zone_delegated", "zone_forward" , "zone_rp", "zone_stub", "nsgroup", "nsgroup:delegation", "nsgroup:forwardingmember", "nsgroup:stubmember", "nsgroup:forwardstubserver", "ddns:principalcluster", "ddns:principalcluster:group", "dns64group", "hostnamerewritepolicy", "bulkhostnametemplate", "scavengingtask", "view"]
	,"parental_control": ["parentalcontrol:avp", "parentalcontrol:blockingpolicy", "parentalcontrol:ipspacediscriminator", "parentalcontrol:subscriber", "parentalcontrol:subscriberrecord", "parentalcontrol:subscribersite"]
	,"dtc": ["dtc", "dtc:allrecords" , "dtc:certificate", "dtc:lbdn, dtc:monitor", "dtc:monitor:http", "dtc:monitor:icmp", "dtc:monitor:pdp", "dtc:monitor:sip", "dtc:monitor:snmp",  "dtc:monitor:tcp", "dtc:object", "dtc:pool", "dtc:record:a", "dtc:record:aaaa", "dtc:record:cname", "dtc:record:naptr", "dtc:record:srv", "dtc:server", "dtc:topology", "dtc:topology:label", "dtc:topology:rule"]
	,"discovery": ["discovery", "discovery:device", "discovery:devicecomponent", "discovery:deviceinterface", "discovery:deviceneighbor", "discovery:devicesupportbundle", "discovery:diagnostictask", "discovery:gridproperties", "discovery:memberproperties", "discovery:status", "discovery:vrf", "discoverytask", "network_discovery"]
	,"dhcp": ["grid:dhcpproperties", "member:dhcpproperties", "dhcp:statistics", "dhcpfailover", "dhcpoptiondefinition", "dhcpoptionspace", "filterfingerprint", "filtermac", "filternac", "filteroption" , "filterrelayagent", "fingerprint", "fixedaddress", "fixedaddresstemplate", "ipv6dhcpoptiondefinition", "ipv6dhcpoptionspace", "ipv6fixedaddress", "ipv6fixedaddresstemplate", "ipv6network", "ipv6networkcontainer", "ipv6networktemplate", "ipv6range", "ipv6rangetemplate", "ipv6sharednetwork", "lease", "macfilteraddress", "network", "networkcontainer", "networktemplate", "networkview", "orderedranges", "range", "rangetemplate", "roaminghost", "sharednetwork" ]
	,"ipam": ["ipam:statistics", "ipv4address", "ipv6address", "superhost", "superhostchild"]
	,"grid": ["grid", "grid:cloudapi", "grid:cloudapi:cloudstatistics", "grid:cloudapi:tenant", "grid:cloudapi:vm", "grid:cloudapi:vmaddress", "grid:dashboard", "grid:filedistribution", "grid:license_pool", "grid:license_pool_container", "grid:maxminddbinfo", "grid:member:cloudapi", "grid:servicerestart:group", "grid:servicerestart:group:order", "grid:servicerestart:request", "grid:servicerestart:request:changedobject", "grid:servicerestart:status", "grid:threatanalytics", "grid:threatprotection", "grid:x509certificate", "license:gridwide", "mastergrid", "cacertificate", "capacityreport", "csvimporttask", "db_objects", "dbsnapshot", "deleted_objects", "member", "member:filedistribution", "member:license", "member:parentalcontrol", "member:threatanalytics", "member:threatprotection", "namedacl", "natgroup", "restartservicestatus", "rir", "rir:organization", "tftpfiledir", "upgradegroup", "upgradeschedule", "upgradestatus", "vdiscoverytask"]
	,"microsoft": ["msserver", "msserver:adsites:domain", "msserver:adsites:site", "msserver:dhcp", "msserver:dns", "mssuperscope"]
	,"outbound": ["allendpoints", "ciscoise:endpoint", "dxl:endpoint", "notification:rest:endpoint", "notification:rest:template", "notification:rule", "pxgrid:endpoint", "syslog:endpoint"]
	,"users": ["ad_auth_service", "admingroup", "adminrole", "adminuser", "approvalworkflow", "authpolicy", "ldap_auth_service", "localuser:authservice", "bfdtemplate", "certificate:authservice", "ftpuser", "networkuser", "permission", "radius:authservice", "saml:authservice", "snmpuser", "tacacsplus:authservice", "userprofile"]
	,"threat_analytics": ["threatanalytics:moduleset", "threatanalytics:whitelist", "threatinsight:cloudclient", "threatprotection:grid:rule", "threatprotection:profile", "threatprotection:profile:rule", "threatprotection:rule", "threatprotection:rulecategory", "threatprotection:ruleset", "threatprotection:ruletemplate", "threatprotection:statistics" ]
	,"miscellaneous": ["extensibleattributedef", "fileop", "hsm:allgroups", "hsm:safenetgroup", "hsm:thalesgroup", "kerberoskey", "awsrte53taskgroup", "awsuser", "captiveportal", "scheduledtask", "search", "smartfolder:children", "smartfolder:global", "smartfolder:personal"]
	,"vlan": ["vlan", "vlanrange", "vlanview"]}
	temp = sorted(res[object_name])

	global parameters_dict
	parameters_dict = {}
	
	#for i in list_objects:
	for i in temp:
		if(i in list_objects):
			obj = get_wapi_call(ip[0],'admin','infoblox',i+'?_schema_version=2&_schema&_get_doc=1')

			tag = obj['type']
			parameters = obj['fields']

			parameters_dict[tag] = parameters
			values_a = {}
			values_b = {}

			if obj['restrictions']:
				if("read" not in obj["restrictions"]):
					create_get_definition(doc,i,tag,parameters,values_a)


				if("create" not in obj["restrictions"]):
					create_post_definition(doc,i,tag,parameters,values_a)

				func_param = []
				for j in parameters:
					if("wapi_primitive" in j.keys()):
						if(j["wapi_primitive"] == "funccall"):
							func_param.append(j)
						else:
							continue
					else:
						continue

				if("read" not in obj["restrictions"]):
					create_get_by_reference_definition(doc,i,tag,parameters,values_b)
				if func_param:
					create_post_function_definition(doc,i,tag,func_param,values_b)
				if("update" not in obj["restrictions"]):
					create_put_definition(doc,i,tag,parameters,values_b)
				if("delete" not in obj["restrictions"]):
					create_delete_definition(doc,i,tag,values_b)
			else:	
				create_get_definition(doc,i,tag,parameters,values_a)
				create_post_definition(doc,i,tag,parameters,values_a)
				func_param = []
				for j in parameters:
					if("wapi_primitive" in j.keys()):
						if(j["wapi_primitive"] == "funccall"):
							func_param.append(j)
						else:
							continue
					else:
						continue

				create_get_by_reference_definition(doc,i,tag,parameters,values_b)
				if func_param:
					create_post_function_definition(doc,i,tag,func_param,values_b)
				
				create_put_definition(doc,i,tag,parameters,values_b)
				create_delete_definition(doc,i,tag,values_b)

			if(not values_a == False):
				main_dict["paths"]["/wapi/{}/{}".format(wapi_version,i)] = values_a
			if(not values_b == False):
				main_dict["paths"]["/wapi/"+wapi_version+"/"+tag+"/{"+tag+"_reference}"] = values_b
			
		else:
			continue	

#creates the components section for WAPI Swagger definition (security and schema)
def create_components(doc,main_dict):
	main_dict["components"] = {"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic"}}}
	schema_dict = {}
	create_schema_reference(doc,parameters_dict,schema_dict)
	main_dict["components"]["schemas"] = schema_dict


#main function
def main():
	ip = ['127.0.0.1'] #enter the IP of GM here
	ver = ["v2.7","v2.8","v2.9","v2.10","v2.11","v2.11.1","v2.12"]
	l=["dns","dhcp","discovery","dtc","grid","ipam","microsoft","outbound","users","threat_analytics","miscellaneous","vlan","rpz","parental_control"]
	global wapi_version
	global object_name
	for object_name in l:
		for wapi_version in ver:
			doc = open("{}/{}.json".format(wapi_version,object_name),"w")
			main_dict = {}

			create_introduction(doc,ip,main_dict)
			create_path(doc,ip,main_dict)
			create_components(doc,main_dict)

			doc.write(json.dumps(main_dict, indent=2))
			doc.close()
			print(""+wapi_version+" Done..!!")
		print(""+object_name+" Done..!!")
	print("Complete")

if __name__ == "__main__":
	main()


"""
urls: [{url: "dhcp.json", name: "DHCP"},{url: "discovery.json" , name: "Discovery"},{url: "dns.json", name: "DNS"},{url: "dtc.json", name: "DNS Traffic Control"},{url: "grid.json" , name: "Grid"},{url: "ipam.json", name: "IPAM"},{url: "microsoft.json" , name: "Microsoft"},{url: "miscellaneous.json" , name: "Miscellaneous"},{url: "outbound.json" , name: "Outbound"},{url: "parental_control.json" , name: "Parental Control"},{url: "rpz.json", name: "Response Policy Zones"},{url: "threat_analytics.json" , name: "Threat Analytics"},{url: "users.json" , name: "Users"},{url: "vlan.json" , name: "VLAN"}]

l = ["dns.json" , "dhcp.json", "ipam.json",  "grid.json" , "dtc.json",  "rpz.json" , "parental_control.json" , "discovery.json" , "microsoft.json" , outbound.json" ,  "users.json" , threat_analytics.json" , miscellaneous.json", "vlan.json"]

"""
