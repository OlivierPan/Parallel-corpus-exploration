#coding:utf-8
# This code must be placed inside the treetagger folder
import os
import re
import sys
sys.path.insert(0,'/users/pansa/desktop/statistique_textuelle')#This is important, insert a path
from traitement_phrase_chinoise import Phrase_chi_info#and this one too
from lxml import etree
from phrase_fran import Phraseinfo


tree=etree.parse("/Users/pansa/Desktop/statistique_textuelle/corpus_parrale.xml")
etree.tostring(tree.getroot())
# The first line in the XML document must be deleted to continuer parsing
with open("/Users/pansa/Desktop/statistique_textuelle/corpus_parrale.xml","r") as file:
    content=file.read()
root=etree.XML(content)
doc=etree.ElementTree(root)
article_zero=str(root.xpath("string(//articlefran[@id='0'])")).strip()

firsttry=Phraseinfo(article_zero)
print(firsttry.phrase)
print(firsttry.longueur)
firsttry.get_pos()
print(firsttry.pos_chaine)
print(firsttry.posdic)
