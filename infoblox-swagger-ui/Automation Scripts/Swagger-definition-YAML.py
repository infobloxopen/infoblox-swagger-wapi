###################################################################################################
#                                      Copyright 2020                                             #
#                       Author: Vedant Sethia <vsethia@infoblox.com>                              #
#    For any issues/suggestions please write to vsethia@infoblox.com, kvasudevan@infoblox.com     #
###################################################################################################

#Automation script for for creating a YAML Open-API Specification file for Infoblox REST APIs

#libraries
import requests
import json

#function for calling the REST API
def get_wapi_call(ip,username,password,wapi_object):
	requests.packages.urllib3.disable_warnings()
	base_url = "https://{}/wapi/v2.10/".format(ip)
	url = base_url + wapi_object
	response = requests.request("GET", url, auth=(username,password), verify = False)
	js = json.loads(response.text)	
	return js
	
#defination for GET
def create_get_defination(doc, obj, tag, parameters):

	#get defination
	doc.write("\t\tget:\n")
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))
	

	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: _return_fields\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")


	doc.write("\t\t\t\t- name: _return_fields+\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma, this returns the required fields along wiht the default fields\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	

	doc.write("\t\t\t\t- name: _max_results\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the number of results to be fetched\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: integer\n")
	doc.write("\t\t\t\t\t\tminimum: 1\n")

	doc.write("\t\t\t\t- name: _return_as_object\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Select 1 if result is required as a object\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: integer\n")
	doc.write("\t\t\t\t\t\tenum: [0,1]\n")
	doc.write("\t\t\t\t\t\tdefault: 0\n")

	doc.write("\t\t\t\t- name: _paging\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Select 1 if paging is required. If SET, _max_results and _return_as_object must be entered.\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: integer\n")
	doc.write("\t\t\t\t\t\tenum: [0,1]\n")
	doc.write("\t\t\t\t\t\tdefault: 0\n")	

	doc.write("\t\t\t\t- name: _page_id\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the page ID for fetching next page\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")

	for i in parameters:
		if('s' in i["supports"]):
			doc.write("\t\t\t\t- name: "+i["name"]+"\n")
			doc.write("\t\t\t\t\tin: query\n")
			doc.write("\t\t\t\t\trequired: false\n")
			doc.write("\t\t\t\t\tdescription: Enter the value of the field\n")
			doc.write("\t\t\t\t\tschema:\n")
			doc.write("\t\t\t\t\t\ttype: string\n")

	#response
	doc.write("\n\t\t\tresponses:\n")
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses = ["\t\t\t\t\'200\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\t$ref: \"#/components/schemas/"+name+"\"\n"]
	doc.writelines(responses)

	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")


#defination for GET by reference
def create_get_by_reference_defination(doc,obj,tag,parameters):
	#get defination
	doc.write("\t\tget:\n")
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))
	

	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: \""+tag+"_reference\"\n")
	doc.write("\t\t\t\t\tin: path\n")
	doc.write("\t\t\t\t\trequired: true\n")
	doc.write("\t\t\t\t\tdescription: \"Enter the reference for {}\"\n".format(tag))
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\texample: \"resourceID:resourceName\"\n")

	doc.write("\t\t\t\t- name: _return_fields\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")

	doc.write("\t\t\t\t- name: _return_fields+\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma, this returns the required fields along with the default fields\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")	

	doc.write("\t\t\t\t- name: _return_as_object\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Select 1 if result is required as a object\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: integer\n")
	doc.write("\t\t\t\t\t\tenum: [0,1]\n")
	doc.write("\t\t\t\t\t\tdefault: 0\n")

	#response
	doc.write("\n\t\t\tresponses:\n")
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses = ["\t\t\t\t\'200\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\t$ref: \"#/components/schemas/"+name+"\"\n"]
	doc.writelines(responses)

	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")


#defination for POST
def create_post_defination(doc,obj,tag,parameters):
	#post defination
	doc.write("\t\tpost:\n")
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))


	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: _return_fields\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")	

	#requestBody
	doc.write("\t\t\trequestBody:\n")
	doc.write("\t\t\t\tdescription: Enter the request here\n")
	doc.write("\t\t\t\trequired: true\n")
	doc.write("\t\t\t\tcontent:\n")
	doc.write("\t\t\t\t\tapplication/json:\n")
	doc.write("\t\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\t\ttype: object\n")
	doc.write("\t\t\t\t\t\t\tproperties:\n")

	for i in parameters:
		if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
			continue		
		elif('w' in str(i["supports"])):
			doc.write("\t\t\t\t\t\t\t\t"+i["name"]+":\n")
			doc.write("\t\t\t\t\t\t\t\t\ttype: string\n")
			if(i["type"][0] == "enum"):
				doc.write("\t\t\t\t\t\t\t\t\texample: "+str(i["enum_values"])+"\n")
			elif(i["is_array"] == True):	
				if("schema" in i.keys()):
					temp = []
					temp.append({})
					for j in i['schema']['fields']:
						a = j['name']
						b = j['type'][0]
						temp[0][a] = b
					doc.write("\t\t\t\t\t\t\t\t\texample: "+str(temp)+"\n")
				else:
					doc.write("\t\t\t\t\t\t\t\t\texample: [\""+i["type"][0]+"\"]\n")
			else:
				doc.write("\t\t\t\t\t\t\t\t\texample: \""+i["type"][0]+"\"\n")

	#response
	doc.write("\n\t\t\tresponses:\n")
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses = ["\t\t\t\t\'201\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\t$ref: \"#/components/schemas/"+name+"\"\n"]
	doc.writelines(responses)

	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")



#defination for PUT
def create_put_defination(doc,obj,tag,parameters):
	#put defination
	doc.write("\t\tput:\n")
	doc.write("\t\t\tdescription: Update the {} resource\n".format(tag))
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))

	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: \""+tag+"_reference\"\n")
	doc.write("\t\t\t\t\tin: path\n")
	doc.write("\t\t\t\t\trequired: true\n")
	doc.write("\t\t\t\t\tdescription: \"Enter the reference for {}\"\n".format(tag))
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\texample: \"resourceID:resourceName\"\n")	

	doc.write("\t\t\t\t- name: _return_fields\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: false\n")
	doc.write("\t\t\t\t\tdescription: Enter the field names followed by comma\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")	

	#requestBody
	doc.write("\t\t\trequestBody:\n")
	doc.write("\t\t\t\tdescription: Enter the request here\n")
	doc.write("\t\t\t\trequired: true\n")
	doc.write("\t\t\t\tcontent:\n")
	doc.write("\t\t\t\t\tapplication/json:\n")
	doc.write("\t\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\t\ttype: object\n")
	doc.write("\t\t\t\t\t\t\tproperties:\n")

	for i in parameters:
		if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
			continue		
		elif('u' in str(i["supports"])):
			doc.write("\t\t\t\t\t\t\t\t"+i["name"]+":\n")
			doc.write("\t\t\t\t\t\t\t\t\ttype: string\n")
			if(i["type"][0] == "enum"):
				doc.write("\t\t\t\t\t\t\t\t\texample: "+str(i["enum_values"])+"\n")			
			elif(i["is_array"] == True):	
				if("schema" in i.keys()):
					temp = []
					temp.append({})
					for j in i['schema']['fields']:
						a = j['name']
						b = j['type'][0]
						temp[0][a] = b
					doc.write("\t\t\t\t\t\t\t\t\texample: "+str(temp)+"\n")
				else:
					doc.write("\t\t\t\t\t\t\t\t\texample: [\""+i["type"][0]+"\"]\n")
			else:
				doc.write("\t\t\t\t\t\t\t\t\texample: \""+i["type"][0]+"\"\n")

	#response
	doc.write("\n\t\t\tresponses:\n")
	name = tag
	if(':' in name):
		name = name.replace(':','_')
	responses = ["\t\t\t\t\'200\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\t$ref: \"#/components/schemas/"+name+"\"\n"]
	doc.writelines(responses)

	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")




#defination for DELETE
def create_delete_defination(doc, obj, tag):
	#delete defination
	doc.write("\t\tdelete:\n")
	doc.write("\t\t\tdescription: Delete the {} resource\n".format(tag))
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))

	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: \""+tag+"_reference\"\n")
	doc.write("\t\t\t\t\tin: path\n")
	doc.write("\t\t\t\t\trequired: true\n")
	doc.write("\t\t\t\t\tdescription: \"Enter the reference for {}\"\n".format(tag))
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\texample: \"resourceID:resourceName\"\n")

	#response
	doc.write("\t\t\tresponses:\n")
	doc.write("\t\t\t\t'200':\n")
	doc.write("\t\t\t\t\tdescription: \"OK\"\n")
	doc.write("\t\t\t\t\tcontent:\n")
	doc.write("\t\t\t\t\t\tapplication/json:\n")
	doc.write("\t\t\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\t\t\ttype: object\n")
	doc.write("\t\t\t\t\t\t\t\tproperties:\n")
	doc.write("\t\t\t\t\t\t\t\t\t_ref:\n")
	doc.write("\t\t\t\t\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\t\t\t\t\tdescription: \"Reference of the deleted object\"\n")

	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")


#definition for Function calls
def create_post_function_defination(doc,obj,tag,parameters):
	name = []
	for i in parameters:
		name.append(i["name"])


	doc.write("\t\tpost:\n")
	doc.write("\t\t\tdescription: Function calls\n")
	doc.write("\t\t\ttags: \n \t\t\t\t- {}\n".format(tag))	

	#parameters
	doc.write("\t\t\tparameters:\n")
	doc.write("\t\t\t\t- name: \""+tag+"_reference\"\n")
	doc.write("\t\t\t\t\tin: path\n")
	doc.write("\t\t\t\t\trequired: true\n")
	doc.write("\t\t\t\t\tdescription: \"Enter the reference for {}\"\n".format(tag))
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\texample: \"resourceID:resourceName\"\n")

	doc.write("\t\t\t\t- name: _function\n")
	doc.write("\t\t\t\t\tin: query\n")
	doc.write("\t\t\t\t\trequired: true\n")
	doc.write("\t\t\t\t\tdescription: Select the function\n")
	doc.write("\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\ttype: string\n")
	doc.write("\t\t\t\t\t\tenum: "+str(name)+"\n")	

	#requestBody
	doc.write("\t\t\trequestBody:\n")
	doc.write("\t\t\t\tdescription: Enter the request body here\n")
	doc.write("\t\t\t\trequired: true\n")
	doc.write("\t\t\t\tcontent:\n")
	doc.write("\t\t\t\t\tapplication/json:\n")
	doc.write("\t\t\t\t\t\tschema:\n")
	doc.write("\t\t\t\t\t\t\ttype: object\n")
	doc.write("\t\t\t\t\t\t\tproperties: {}\n")


	#response
	doc.write("\n\t\t\tresponses:\n")
	name = tag
	if(':' in name):
		name = name.replace(':','_')

	prop1 = {}
	prop2 = ""
	for i in parameters:
		if (i["schema"]["input_fields"]):
			temp = {}
			for j in i["schema"]["input_fields"]:
				if(j["type"][0] == "enum"):
					temp[j["name"]] = j["enum_values"]
				else:
					temp[j["name"]] = j["type"][0]
			temp = str(temp)
			prop2 = prop2+"\n\t\t\t\t\t\t\t\t\t"+str(i["name"])+":\n\t\t\t\t\t\t\t\t\t\ttype: string\n"+"\n\t\t\t\t\t\t\t\t\t\texample: "+temp+"\n"
	if(prop2 == ""):
		responses = ["\t\t\t\t\'200\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\ttype: object\n","\t\t\t\t\t\t\t\tproperties: "+str(prop1)+"\n" ]
	else:
		responses = ["\t\t\t\t\'200\':\n", "\t\t\t\t\tdescription: \"OK\"\n", "\t\t\t\t\tcontent:\n" , "\t\t\t\t\t\tapplication/json:\n", "\t\t\t\t\t\t\tschema:\n", "\t\t\t\t\t\t\t\ttype: object\n","\t\t\t\t\t\t\t\tproperties: "+str(prop2)+"\n" ]
	doc.writelines(responses)


	#security
	doc.write("\t\t\tsecurity:\n \t\t\t\t- basicAuth: []\n\n")




#creates the schema for all the objects
def create_schema_reference(doc,parameters_dict):
	doc.write("\tschemas:\n")
	for key in parameters_dict:
		head = key
		if(":" in head):
			head = head.replace(":","_")
		doc.write("\t\t"+head+":\n")
		doc.write("\t\t\ttype: object\n")
		doc.write("\t\t\tproperties:\n")
		#creating schema with swagger data type
		valid = ['array', 'boolean', 'integer', 'number', 'object', 'string','uint','bool','enum']
		for i in parameters_dict[key]:
			if(("wapi_primitive" in i.keys()) and (i["wapi_primitive"] == "funccall")):
				continue
			else:
				doc.write("\t\t\t\t{}:\n".format(i['name']))
				if(i['type'][0] in valid):
					if(i['type'][0] == "uint"):
						doc.write("\t\t\t\t\ttype: \"integer\"\n")
						doc.write("\t\t\t\t\texample: \"integer\"\n")
					elif(i['type'][0] == "bool"):
						doc.write("\t\t\t\t\ttype: \"boolean\"\n")
						doc.write("\t\t\t\t\texample: \"boolean\"\n")
					elif(i['type'][0] == "enum"):
						doc.write("\t\t\t\t\ttype: \"string\"\n")
						doc.write("\t\t\t\t\tenum: [\"{}\"]\n".format(i['enum_values']))
					else:
						doc.write("\t\t\t\t\ttype: {}\n".format(i['type'][0]))
				else:
					doc.write("\t\t\t\t\ttype: string\n")
					doc.write("\t\t\t\t\tenum: [\"{}\"]\n".format(i['type'][0]))
				

				#escape code for quotes in documentation
				temp = list(i['doc'])	
				for j in range(0,len(temp)):
					if(temp[j] == "\""):
						temp[j] = ""
				des = ""
				for j in temp:
					des = des + j
						
				doc.write("\t\t\t\t\tdescription: \"{}\"\n".format(des))



#creates the introduction section for WAPI Swagger definition
def create_introduction(doc,ip):
	doc.write("openapi: 3.0.0\n")
	info = ["info:\n", "\tdescription: \"Sample WAPI Documentation\"\n","\tversion: \"1.0.1\"\n", "\ttitle: \"Infoblox WAPI\"\n\n"]
	doc.writelines(info)
	license = ["\tlicense:\n","\t\tname: Infoblox License\n", "\t\turl: https://www.infoblox.com/\n\n"]
	doc.writelines(license)
	contact = ["\tcontact:\n","\t\tname: \"Vedant\"\n", "\t\temail: \"vsethia@infoblox.com\"\n\n"]
	doc.writelines(contact)
	doc.write("servers:\n\t- url: \'https://{}\' \n\t- url: \'https://10.196.205.40\' \n\n".format(ip))


#creates the paths section for WAPI Swagger definition
def create_path(doc,ip):
	doc.write("paths:\n")
	schema = get_wapi_call(ip,'admin','infoblox','?_schema')
	list_objects = schema['supported_objects']      #list of all supported objects as a list 

	temp = []
	rpz = ["allrpzrecords", "orderedresponsepolicyzones", "record:rpz:a", "record:rpz:aaaa", "record:rpz:aaaa:ipaddress", "record:rpz:a:ipaddress", "record:rpz:cname", "record:rpz:cname:clientipaddress", "record:rpz:cname:clientipaddressdn", "record:rpz:cname:ipaddress", "record:rpz:cname:ipaddressdn", "record:rpz:mx", "record:rpz:naptr", "record:rpz:ptr", "record:rpz:srv", "record:rpz:txt", "outbound:cloudclient", "taxii"]
	dns = ["grid:dns", "member:dns", "allrecords", "bulkhost", "record:host", "record:a", "record:aaaa", "record:alias", "record:caa", "record:cname", "record:dhcid", "record:dname", "record:dnskey", "record:ds", "record:dtclbdn", "record:host_ipv4addr", "record:host_ipv6addr", "record:mx", "record:naptr", "record:ns", "record:nsec", "record:nsec3", "record:nsec3param", "record:ptr", "record:rrsig", "record:srv", "record:tlsa", "record:txt", "record:unknown", "recordnamepolicy", "ruleset", "sharedrecord:a", "sharedrecord:aaaa", "sharedrecord:cname", "sharedrecord:mx", "sharedrecord:srv", "sharedrecord:txt", "sharedrecordgroup", "view", "zone_auth", "zone_auth_discrepancy", "zone_delegated", "zone_forward" , "zone_rp", "zone_stub", "nsgroup", "nsgroup:delegation", "nsgroup:forwardingmember", "nsgroup:stubmember", "nsgroup:forwardstubserver", "ddns:principalcluster", "ddns:principalcluster:group", "dns64group", "hostnamerewritepolicy", "bulkhostnametemplate", "scavengingtask", "view"]
	parental_control = ["parentalcontrol:avp", "parentalcontrol:blockingpolicy", "parentalcontrol:ipspacediscriminator", "parentalcontrol:subscriber", "parentalcontrol:subscriberrecord", "parentalcontrol:subscribersite"]
	dtc = ["dtc", "dtc:allrecords" , "dtc:certificate", "dtc:lbdn, dtc:monitor", "dtc:monitor:http", "dtc:monitor:icmp", "dtc:monitor:pdp", "dtc:monitor:sip", "dtc:monitor:snmp",  "dtc:monitor:tcp", "dtc:object", "dtc:pool", "dtc:record:a", "dtc:record:aaaa", "dtc:record:cname", "dtc:record:naptr", "dtc:record:srv", "dtc:server", "dtc:topology", "dtc:topology:label", "dtc:topology:rule"]
	discovery = ["discovery", "discovery:device", "discovery:devicecomponent", "discovery:deviceinterface", "discovery:deviceneighbor", "discovery:devicesupportbundle", "discovery:diagnostictask", "discovery:gridproperties", "discovery:memberproperties", "discovery:status", "discovery:vrf", "discoverytask", "network_discovery"]
	dhcp = ["grid:dhcpproperties", "member:dhcpproperties", "dhcp:statistics", "dhcpfailover", "dhcpoptiondefinition", "dhcpoptionspace", "filterfingerprint", "filtermac", "filternac", "filteroption" , "filterrelayagent", "fingerprint", "fixedaddress", "fixedaddresstemplate", "ipv6dhcpoptiondefinition", "ipv6dhcpoptionspace", "ipv6fixedaddress", "ipv6fixedaddresstemplate", "ipv6network", "ipv6networkcontainer", "ipv6networktemplate", "ipv6range", "ipv6rangetemplate", "ipv6sharednetwork", "lease", "macfilteraddress", "network", "networkcontainer", "networktemplate", "networkview", "orderedranges", "range", "rangetemplate", "roaminghost", "sharednetwork" ]
	ipam = ["ipam:statistics", "ipv4address", "ipv6address", "superhost", "superhostchild"]
	grid = ["grid", "grid:cloudapi", "grid:cloudapi:cloudstatistics", "grid:cloudapi:tenant", "grid:cloudapi:vm", "grid:cloudapi:vmaddress", "grid:dashboard", "grid:filedistribution", "grid:license_pool", "grid:license_pool_container", "grid:maxminddbinfo", "grid:member:cloudapi", "grid:servicerestart:group", "grid:servicerestart:group:order", "grid:servicerestart:request", "grid:servicerestart:request:changedobject", "grid:servicerestart:status", "grid:threatanalytics", "grid:threatprotection", "grid:x509certificate", "license:gridwide", "mastergrid", "cacertificate", "capacityreport", "csvimporttask", "db_objects", "dbsnapshot", "deleted_objects", "member", "member:filedistribution", "member:license", "member:parentalcontrol", "member:threatanalytics", "member:threatprotection", "namedacl", "natgroup", "restartservicestatus", "rir", "rir:organization", "tftpfiledir", "upgradegroup", "upgradeschedule", "upgradestatus", "vdiscoverytask"]
	microsoft = ["msserver", "msserver:adsites:domain", "msserver:adsites:site", "msserver:dhcp", "msserver:dns", "mssuperscope"]
	outbound = ["allendpoints", "ciscoise:endpoint", "dxl:endpoint", "notification:rest:endpoint", "notification:rest:template", "notification:rule", "pxgrid:endpoint", "syslog:endpoint"]
	users = ["ad_auth_service", "admingroup", "adminrole", "adminuser", "approvalworkflow", "authpolicy", "ldap_auth_service", "localuser:authservice", "bfdtemplate", "certificate:authservice", "ftpuser", "networkuser", "permission", "radius:authservice", "saml:authservice", "snmpuser", "tacacsplus:authservice", "userprofile"]
	threat_analytics = ["threatanalytics:moduleset", "threatanalytics:whitelist", "threatinsight:cloudclient", "threatprotection:grid:rule", "threatprotection:profile", "threatprotection:profile:rule", "threatprotection:rule", "threatprotection:rulecategory", "threatprotection:ruleset", "threatprotection:ruletemplate", "threatprotection:statistics" ]
	miscellaneous = ["extensibleattributedef", "fileop", "hsm:allgroups", "hsm:safenetgroup", "hsm:thalesgroup", "kerberoskey", "awsrte53taskgroup", "awsuser", "captiveportal", "scheduledtask", "search", "smartfolder:children", "smartfolder:global", "smartfolder:personal"]
	vlan = ["vlan", "vlanrange", "vlanview"]
	temp = vlan
	
	global parameters_dict
	parameters_dict = {}
	#for i in list_objects:
	for i in temp:
		obj = get_wapi_call(ip,'admin','infoblox',i+'?_schema_version=2&_schema&_get_doc=1')

		tag = obj['type']
		parameters = obj['fields']

		parameters_dict[tag] = parameters
		if obj['restrictions']:
			doc.write("\t/wapi/v2.10/{}:\n".format(i))
			create_get_defination(doc,i,tag,parameters)
			if("create" not in obj["restrictions"]):
				create_post_defination(doc,i,tag,parameters)

			func_param = []
			for j in parameters:
				if("wapi_primitive" in j.keys()):
					if(j["wapi_primitive"] == "funccall"):
						func_param.append(j)
					else:
						continue
				else:
					continue

			doc.write("\t/wapi/v2.10/"+tag+"/{"+tag+"_reference}:\n")
			create_get_by_reference_defination(doc,i,tag,parameters)
			if func_param:
				create_post_function_defination(doc,i,tag,func_param)
			if("update" not in obj["restrictions"]):
				create_put_defination(doc,i,tag,parameters)
			if("delete" not in obj["restrictions"]):
				create_delete_defination(doc,i,tag)
		else:	
			doc.write("\t/wapi/v2.10/{}:\n".format(i))
			create_get_defination(doc,i,tag,parameters)
			create_post_defination(doc,i,tag,parameters)
			func_param = []
			for j in parameters:
				if("wapi_primitive" in j.keys()):
					if(j["wapi_primitive"] == "funccall"):
						func_param.append(j)
					else:
						continue
				else:
					continue

			doc.write("\t/wapi/v2.10/"+tag+"/{"+tag+"_reference}:\n")
			create_get_by_reference_defination(doc,i,tag,parameters)
			if func_param:
				create_post_function_defination(doc,i,tag,func_param)
			
			create_put_defination(doc,i,tag,parameters)
			create_delete_defination(doc,i,tag)


#creates the components section for WAPI Swagger definition (security and schema)
def create_components(doc):
	doc.write("components:\n")
	security = ["\tsecuritySchemes:\n","\t\tbasicAuth:\n","\t\t\ttype: http\n","\t\t\tscheme: basic\n"]
	doc.writelines(security)
	create_schema_reference(doc,parameters_dict)


#main Function
def main():
	ip = '10.196.205.43'
	doc = open("swagger.yaml","w")

	create_introduction(doc,ip)
	create_path(doc,ip)
	create_components(doc)

	print("Documentation created..!! ")

if __name__ == "__main__":
	main()

