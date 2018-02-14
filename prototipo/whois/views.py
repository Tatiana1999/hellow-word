# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Enlaces
from django.http import HttpResponse
from .forms import Search
from  string import replace
import os
import csv
import whois
import webbrowser
import urllib
from urlparse import urlparse
from urlparse import parse_qs
from lxml.html import fromstring
from requests import get
from models import Enlaces
datal = []

def Inicio_urls(request): #Traer los objetos
	enlaces = Enlaces.objects.all()
	context = {
		"enlaces" : enlaces,
	}
	return render(request,"base.html", context)

def inicio(request): #Remplaza url

	enlaces = Enlaces.objects.all()
	data1 =[]
	info = ""
	data = []

	for instance in enlaces:
		new_data = str(instance).replace("https","")
		new_data = new_data.replace("http","")
		new_data = new_data.replace("www.","")
		new_data = new_data.replace("://","")
		data1.append(new_data.replace("",""))

	for url in data1:
		info = url.split("/")
		info = info[0]
		data.append(info)

		context = {

			"id" : instance,
			"url" : enlaces,
			"data" : data,
			"data2" : enlaces,
			"data1": data1,
	}
	return render(request,"base.html", context)#Diccionario vacio

def whois(request,url,):#Proceso whois
	i = 0
	valor = ""
	data = []
	info = ""

	comand = "whois " + url #Extraccion de informacion
	process = os.popen(comand)
	result = str(process.read())

 	info = result.split(">>>")#Corta informacion
	info = info[0]
	data.append(info)


	for i in data: #Organizar los datos
		new_data = i.split("\n")
		new_data.append(info)
		print new_data



	context = {

		"new_data" : new_data,
	}
	return render(request,"whois.html", context)

def wget(request,dato,):#Proceso wget

	comand = "wget -e robots=off -p -k " + dato + " -P /home/tatiana/Escritorio"#Extraccion del Html
	process = os.popen(comand)
	result2 = str(process.read())

	context = {
		"result2" : result2,
	}
	return render(request,"descarga.html", context)

def search(request):#Formulario para buscar
 	 palabra = ""
	 data_link = ""
	 new = ""
 	 mensaje = "NADA"
	 datal = []
	 form = Search(request.POST or None)
	 if form.is_valid():
		form_data = form.cleaned_data
		PalabraClave = form_data.get("SearchLink")#Se recupera el dato
 	 	palabra = PalabraClave


		if palabra is None:
			print "No hay palabra"
		else:
			data_inicio = "https://www.google.com.co/search?q="
			data_final = "&num=100&cad=h&cad=h"
 			data_link = data_inicio + palabra + data_final
			var = data_link
			raw = get(var).text
			page = fromstring(raw)
 			for result in page.cssselect(".r a"):
				url = result.get("href")
				if url.startswith("/url?"):
		   			data = url.replace("/url?q=","")
		   			data_res = data.split("&sa")
		   			data_res = data_res[0]
		   			datal.append(data_res)


	 context = {
		"form" : form,
		"palabra": palabra,
		"datal" : datal,

 	 }
	 links_base(datal)
	 return render(request,"search.html",context)


def links_base(datal):
		for i in datal:
			modelo = Enlaces(url=i)
			modelo.save()
