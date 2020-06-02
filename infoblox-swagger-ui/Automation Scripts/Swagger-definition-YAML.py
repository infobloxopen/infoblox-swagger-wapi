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

	"""
		for i in parameters:
			if('s' in i["supports"]):
				doc.write("\t\t\t\t- name: "+i["name"]+"\n")
				doc.write("\t\t\t\t\tin: query\n")
				doc.write("\t\t\t\t\trequired: false\n")
				doc.write("\t\t\t\t\tdescription: Enter the value of the field\n")
				doc.write("\t\t\t\t\tschema:\n")
				doc.write("\t\t\t\t\t\ttype: string\n")
	"""

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



def create_introduction(doc,ip):
	doc.write("openapi: 3.0.0\n")
	info = ["info:\n", "\tdescription: \"Sample WAPI Documentation\"\n","\tversion: \"1.0.1\"\n", "\ttitle: \"Infoblox WAPI\"\n\n"]
	doc.writelines(info)
	license = ["\tlicense:\n","\t\tname: Infoblox License\n", "\t\turl: https://www.infoblox.com/\n\n"]
	doc.writelines(license)
	contact = ["\tcontact:\n","\t\tname: \"Vedant\"\n", "\t\temail: \"vsethia@infoblox.com\"\n\n"]
	doc.writelines(contact)
	doc.write("servers:\n\t- url: \'https://{}\' \n\t- url: \'https://10.196.205.40\' \n\n".format(ip))


def create_path(doc,ip):
	doc.write("paths:\n")
	schema = get_wapi_call(ip,'admin','infoblox','?_schema')
	list_objects = schema['supported_objects']      #list of all supported objects as a list 

	temp = ["zone_auth","record:a","record:ptr","record:host"]
	temp = ["grid","member"]
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


def create_components(doc):
	doc.write("components:\n")
	security = ["\tsecuritySchemes:\n","\t\tbasicAuth:\n","\t\t\ttype: http\n","\t\t\tscheme: basic\n"]
	doc.writelines(security)
	create_schema_reference(doc,parameters_dict)



def main():
	ip = '10.196.205.43'
	doc = open("swagger.yaml","w")

	create_introduction(doc,ip)
	create_path(doc,ip)
	create_components(doc)

	print("Documentation created..!! ")

if __name__ == "__main__":
	main()

