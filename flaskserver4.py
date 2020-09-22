from flask import Flask, Response
from flask_cors import CORS, cross_origin
from xml.etree import ElementTree as ET
import xmltodict
import json
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import logging

app = Flask(__name__)


@app.route('/getCapabilities')
@cross_origin()
def getCapabilities():
	result = ""
	tree = ET.parse("wadl/wadl_capabilities.xml")
	root = tree.getroot()
	path = "data/description.json"
	data = readfromjson(path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	for elem in root.iter('method'):
		if(elem.attrib['id']=="getCapabilities"):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))
	paths = []
	#for resource in root.iter('resource'):
	#	path = resource.get('path')
	#	if path.endswith('.json'):
	#		data = readfromjson(path)
	#		info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	#		root2 = ET.fromstring(info)
	#		result2 = ET.tostring(root2, encoding='unicode', method='xml')
	#		resource.insert(0,root2)
	#		ET.dump(resource)
	result = ET.tostring(root, encoding='utf8', method='xml')

	return Response(result, mimetype='text/xml')

#@app.route('/getDescription')
#@cross_origin()
#def getDescription():
#	result = ""
#	path = "description3.json"
#	data = readfromjson(path)
#	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
#	return Response(info, mimetype='text/xml')

@app.route('/getData')
@cross_origin()
def getData():
	result = ""
	tree = ET.parse("wadl/wadl_capabilities.xml")
	root = tree.getroot()
	path = "data/data.json"
	data = readfromjson(path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	for elem in root.iter('method'):
		if(elem.attrib['id']=="getData"):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))

	result = ET.tostring(root, encoding='utf8', method='xml')

	return Response(result, mimetype='text/xml')


@app.route('/getTools')
@cross_origin()
def getTools():
	tree = ET.parse("wadl/wadl_capabilities.xml")
	root = tree.getroot()
	path = "data/tools.json"
	data = readfromjson(path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	for elem in root.iter('method'):
		if(elem.attrib['id']=="getTools"):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))

	result = ET.tostring(root, encoding='utf8', method='xml')
	return Response(result, mimetype='text/xml')

@app.route('/getServices')
@cross_origin()
def getServices():
	tree = ET.parse("wadl/wadl_capabilities.xml")
	root = tree.getroot()
	path = "data/services.json"
	data = readfromjson(path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	for elem in root.iter('method'):
		if(elem.attrib['id']=="getServices"):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))

	result = ET.tostring(root, encoding='utf8', method='xml')
	return Response(result, mimetype='text/xml')

@app.route('/getInteraction')
@cross_origin()
def getInteracton():
	tree = ET.parse("wadl/wadl_capabilities.xml")
	root = tree.getroot()
	path = "data/interaction.json"
	data = readfromjson(path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()
	for elem in root.iter('method'):
		if(elem.attrib['id']=="getInteraction"):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))

	result = ET.tostring(root, encoding='utf8', method='xml')
	return Response(result, mimetype='text/xml')

if __name__ == '__main__':
	#app.run(host='10.200.5.38', port=5004)
	app.run(host='0.0.0.0', port=5004, ssl_context=('cert.pem', 'key.pem'))

