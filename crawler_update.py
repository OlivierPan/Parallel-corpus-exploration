#coding:utf-8
# This is a advanced crawler for textometrie, could be a basic model for futur use
import requests
import lxml
import re
import datetime
from lxml import etree

urllist=['https://cn.ambafrance.org/Declaration-du-President-de-la-Republique-et-de-la', 
'https://cn.ambafrance.org/Tchad-Declaration-de-M-Emmanuel-Macron-president-de-la',
 'https://cn.ambafrance.org/Discours-du-president-de-la-Republique-a-l-occasion-de-la-37508',
  'https://cn.ambafrance.org/Un-an-apres-l-initiative-de-la-Sorbonne', 
  'https://cn.ambafrance.org/Discours-du-President-de-la-Republique-a-l-Assemblee', 
  'https://cn.ambafrance.org/Discours-du-President-de-la-Republique-a-la-conference-des',
   'https://cn.ambafrance.org/Conference-de-presse-conjointe-du-President-de-la-36656',
    'https://cn.ambafrance.org/Transcription-du-discours-du-President-de-la-Republique-au', 
    'https://cn.ambafrance.org/Discours-du-President-de-la-Republique-Emmanuel-Macron-a-la-35524', 
    'https://cn.ambafrance.org/40eme-session-du-Conseil-des-droits-de-l-Homme-Evenement', 
    'https://cn.ambafrance.org/Presidence-francaise-du-Conseil-de-securite-mars-2019', 
    'https://cn.ambafrance.org/Faire-taire-les-armes-en-Afrique-cooperation-entre-les', 
    'https://cn.ambafrance.org/Venezuela-Intervention-du-representant-permanent-de-la', 
    'https://cn.ambafrance.org/Nations-unies', 
	'https://cn.ambafrance.org/Journee-internationale-des-enfants-soldats', 
	'https://cn.ambafrance.org/Entretien-de-M-Jean-Yves-Le-Drian-avec-l-envoye-special-du',
	 'https://cn.ambafrance.org/Republique-centrafricaine-Nomination-de-M-Mankeur-N-Diaye', 
	 'https://cn.ambafrance.org/Debat-ouvert-Repondre-aux-effets-des-catastrophes',
	  'https://cn.ambafrance.org/Prise-de-fonctions-de-M-Geir-Pedersen-nouvel-envoye-special', 
	  'https://cn.ambafrance.org/Coree-du-Nord-Intervention-du-representant-permanent-de-la',
	   'https://cn.ambafrance.org/Nations-unies-Adoption-de-la-resolution-2434-renouvelant-le', 
	   'https://cn.ambafrance.org/Birmanie-Pre-rapport-de-la-mission-d-etablissement-des', 
	   'https://cn.ambafrance.org/Deces-de-Kofi-Annan-Declaration-de-Jean-Yves-Le-Drian-18',
	    'https://cn.ambafrance.org/Nations-unies-Journee-internationale-pour-l-elimination-des',
	     'https://cn.ambafrance.org/Comite-des-droits-de-l-Homme-Candidature-de-Mme-Helene', 
	     'https://cn.ambafrance.org/Nations-Unies-Nouveaux-membres-du-conseil-de-securite-des', 
	     'https://cn.ambafrance.org/Organisation-maritime-internationale-Reelection-de-la', 
	     'https://cn.ambafrance.org/Conseil-de-l-Organisation-maritime-internationale', 
	     'https://cn.ambafrance.org/Ukraine-38840', 
	     'https://cn.ambafrance.org/Declaration-de-la-haute-representante-au-nom-de-l-UE-sur-la',
	      'https://cn.ambafrance.org/Connecter-l-Europe-et-l-Asie-trouver-des-synergies-avec-l', 
	      'https://cn.ambafrance.org/Declaration-conjointe-du-21e-sommet-UE-Chine', 
	      'https://cn.ambafrance.org/Ukraine-38517', 
	      'https://cn.ambafrance.org/Conclusions-du-Conseil-europeen-Communique-de-presse-du', 
	      'https://cn.ambafrance.org/Brexit-le-Conseil-des-affaires-generales-adopte-une-serie', 
	      'https://cn.ambafrance.org/Union-europeenne-Participation-de-M-Jean-Yves-Le-Drian-au-38281', 
	      'https://cn.ambafrance.org/Union-europeenne-Signature-de-l-accord-de-siege-de-l', 
	      'https://cn.ambafrance.org/Royaume-Uni-Deplacement-de-Mme-Nathalie-Loiseau', 
	      'https://cn.ambafrance.org/Pour-une-Renaissance-europeenne',
	       'https://cn.ambafrance.org/Union-europeenne-Reunion-informelle-des-ministres-du', 'https://cn.ambafrance.org/Manifeste-franco-allemand-pour-une-politique-industrielle', 'https://cn.ambafrance.org/Venezuela-Syrie-Declaration-de-M-Jean-Yves-le-Drian', 'https://cn.ambafrance.org/Union-europeenne-Energie', 'https://cn.ambafrance.org/Traite-sur-les-forces-nucleaires-intermediaires', 'https://cn.ambafrance.org/Declaration-conjointe-sur-le-Venezuela', 'https://cn.ambafrance.org/L-UE-va-faciliter-la-mobilite-transfrontaliere-des', 'https://cn.ambafrance.org/Participation-de-M-Jean-Yves-Le-Drian-a-la-reunion', 'https://cn.ambafrance.org/Venezuela-Declaration-de-la-Haute-representante-au-nom-de-l', 'https://cn.ambafrance.org/Communication-Brexit', 'https://cn.ambafrance.org/Traite-de-cooperation-franco-allemand-d-Aix-la-Chapelle', 'https://cn.ambafrance.org/Semaine-verte-a-Berlin-Didier-Guillaume-et-son-homologue', 'https://cn.ambafrance.org/Union-europeenne-Participation-de-M-Jean-Yves-Le-Drian-au-37922', 'https://cn.ambafrance.org/Preparation-a-la-sortie-du-Royaume-Uni-de-l-Union', 'https://cn.ambafrance.org/Deplacement-de-Mme-Nathalie-Loiseau-au-Parlement-europeen', 'https://cn.ambafrance.org/Signature-d-un-nouveau-traite-de-cooperation-et-d', 'https://cn.ambafrance.org/EU-expectations-for-the-China-International-Import-Expo', 'https://cn.ambafrance.org/Relier-l-Europe-a-l-Asie-le-Conseil-europeen-adopte-des', 'https://cn.ambafrance.org/L-UE-renforce-sa-strategie-visant-a-relier-l-Europe-a-l', 'https://cn.ambafrance.org/Conseil-affaires-etrangeres-commerce-Declaration-a-la', 'https://cn.ambafrance.org/Declaration-de-Sofia-Sofia-17-mai-2018', 'https://cn.ambafrance.org/Union-europeenne-Journee-de-l-Europe-9-mai-2018', 'https://cn.ambafrance.org/La-journee-de-l-Europe-36406', 'https://cn.ambafrance.org/Traite-de-l-Elysee-55eme-anniversaire-22-janvier-2018', 'https://cn.ambafrance.org/Declaration-conjointe-a-l-occasion-du-55e-anniversaire-de', 'https://cn.ambafrance.org/Participation-de-M-Jean-Baptiste-Lemoyne-a-la-reunion-des', 'https://cn.ambafrance.org/Declaration-conjointe-du-President-de-la-Republique-avec-le', 'https://cn.ambafrance.org/Conseil-affaires-etrangeres-Le-conseil-reaffirme-l', 'https://cn.ambafrance.org/Conseil-affaires-etrangeres-Coree-du-Nord-l-UE-adopte-de', 'https://cn.ambafrance.org/Union-europeenne-Participation-de-M-Jean-Yves-Le-Drian-au', 'https://cn.ambafrance.org/Discours-du-president-de-la-Republique-Initiative-pour-l', 'https://cn.ambafrance.org/PRESIDENT-JEAN-CLAUDE-JUNCKER-Discours-sur-l-etat-de-l', 'https://cn.ambafrance.org/Nomination-d-Harlem-Desir-au-poste-de-representant-pour-la', 'https://cn.ambafrance.org/19eme-Conseil-des-ministres-franco-allemand', 'https://cn.ambafrance.org/Union-europeenne-Journee-de-l-Europe-9-mai-2017-Declaration', 'https://cn.ambafrance.org/Remarks-by-the-High-Representative-Mogherini-following-the', 'https://cn.ambafrance.org/Declaration-des-27-Chefs-d-Etats-et-de-Gouvernement-et-des']
#'https://cn.ambafrance.org/Investissements-etrangers-en-France-2018',
def requestnew(url):
	r=requests.get(url)
	select=etree.HTML(r.text)
	titre=''.join(select.xpath("//div[contains(@class,'chapo surlignable intro')]/p/text()")).strip()#list
	texte=''.join(select.xpath("string(//*[@class='texte surlignable'])")).strip()#list
	##nodupe=copy.copy(select.xpath("(//*[@class='texte surlignable'])"))
	#for element in nodupe:
	    #element.xpath("string(.)")
	urltradhalf=str(select.xpath("string(//a[@class='tradlang']/@href)")).strip()
	urltrad="https://cn.ambafrance.org/"+urltradhalf
	q=requests.get(urltrad)
	select2=etree.HTML(q.text)
	titre2=''.join(select2.xpath("//div[contains(@class,'chapo surlignable intro')]/p/text()")).strip()
	texte2=''.join(select2.xpath("string(//*[@class='texte surlignable'])")).strip()


	#paragraphe1=''.join(select.xpath("string(//*[@class='texte surlignable']/p[2])"))
	#paragraphe=''.join(select.xpath("//*[@id='main']/div/div[2]/div[3]/p[3]/text()")).strip()
	#paragraphe3=''.join(select.xpath("//*[@id='main']/div/div[2]/div[3]/p[4]/text()")).strip()
	#print(paragraphe1)
	#print(paragraphe)
	#print(paragraphe3)

	#//*[@id="main"]/div/div[2]/div[3]/p[3]
	#print(titre,end="\n\n\n")
	#print(texte,end="\n\n\n")
	#print(titre2,end="\n\n\n")
	#print(texte2,end="\n\n\n")
	return titre,texte,titre2,texte2

k=open('/users/pansa/desktop/corpus_parrale.xml','w+')
k.write("""<?xml version="1.0" encoding="UTF-8"?>""")
k.write("<corpus>")
k.write("\n")
i=0
for url in urllist:
	info=requestnew(url)
	titre1=info[0]
	texte1=info[1]
	titre2=info[2]
	texte2=info[3]
	k.write("<titlefran id='"+str(i)+"'>")
	k.write("\n")
	k.write(titre1)
	k.write("\n")
	k.write("</titlefran>")
	k.write("\n")
	k.write("<articlefran id='"+str(i)+"'>")
	k.write("\n")
	k.write(texte1)
	k.write("\n")
	k.write("</articlefran>")
	k.write("\n")
	k.write("<titlechin id='"+str(i)+"'>")
	k.write("\n")
	k.write(titre2)
	k.write("\n")
	k.write("</titlechin>")
	k.write("\n")
	k.write("<articlechin id='"+str(i)+"'>")
	k.write("\n")
	k.write(texte2)
	k.write("\n")
	k.write("</articlechin>")
	k.write("\n")
	i+=1
	print(i)


k.write("</corpus>")
k.close()

#for url in urllist:
	#requestnew(url)
