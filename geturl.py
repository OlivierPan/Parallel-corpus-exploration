#coding:utf-8

import requests
import lxml
import re
import datetime
from lxml import etree

urlpages=["https://cn.ambafrance.org/-Le-President-de-la-Republique%E6%B3%95%E5%85%B0%E8%A5%BF%E5%85%B1%E5%92%8C%E5%9B%BD%E6%80%BB%E7%BB%9F-#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Le-President-de-la-Republique%E6%B3%95%E5%85%B0%E8%A5%BF%E5%85%B1%E5%92%8C%E5%9B%BD%E6%80%BB%E7%BB%9F-?debut_artsRubDirect=10#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Le-President-de-la-Republique%E6%B3%95%E5%85%B0%E8%A5%BF%E5%85%B1%E5%92%8C%E5%9B%BD%E6%80%BB%E7%BB%9F-?debut_artsRubDirect=20#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Assemblee-generale-des-Nations-Unies-2016-",
"https://cn.ambafrance.org/-Assemblee-generale-des-Nations-Unies-2016-?debut_artsRubDirect=10#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Assemblee-generale-des-Nations-Unies-2016-?debut_artsRubDirect=20#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Assemblee-generale-des-Nations-Unies-2016-?debut_artsRubDirect=30#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=10#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=20#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=30#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=40#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=50#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=60#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=70#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=80#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=90#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=100#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=110#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=120#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=130#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=140#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=150#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=160#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=170#pagination_artsRubDirect",
"https://cn.ambafrance.org/-Actualite-europeenne-?debut_artsRubDirect=180#pagination_artsRubDirect"
]

def find_url_valide(url):
	r=requests.get(url)
	select=etree.HTML(r.text)
#alien=select.xpath("string(//a[@class='link-type-01']/@href)")
	kkk=select.findall(".//a[@class='link-type-01']")
	topic=[]
	for k in kkk:
		topic.append((k.xpath("string(./@href)")))

	urlcomplete=[]
	for toto in topic:
		urlcomplete.append(str("https://cn.ambafrance.org/"+toto))
	#print(urlcomplete)
	#print(len(urlcomplete))
	urlvalide=[]

	for url in urlcomplete:
		r=requests.get(url)
		sel=etree.HTML(r.text)
		if sel.xpath(("string(//a[@class='tradlang']/@href)")):
			if url not in urlvalide:
				urlvalide.append(url)
	return urlvalide

urllist=[]
for url in urlpages:
	urllist.extend(find_url_valide(url))
print(urllist)
