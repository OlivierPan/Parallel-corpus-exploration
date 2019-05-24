#coding:utf-8
from lxml import etree
from nltk import sent_tokenize, word_tokenize
import re
import os
import sys
sys.path.insert(0,'/users/pansa/desktop/statistique_textuelle')#This is important, insert a path
from traitement_phrase_chinoise import Phrase_chi_info#and this one too
from phrase_fran import Phraseinfo

with open("/Users/pansa/Desktop/statistique_textuelle/corpus_parrale.xml","r") as file:
    content=file.read()
root=etree.XML(content)
doc=etree.ElementTree(root)

x_fran=0
x_chin=0

def cut_sent(para):#中文分句方法
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

def mergedic(first,second):#this fonction changes only the first element, the value of the first will grow as adding
    for key,value in second.items():
        if key in first:
            first[key] += value
        else:
            first[key] = value
    return first

dico_all_francais={}
dico_all_chinois={}
for i in range(0,10):
	dico_article_francais={}
	dico_article_chinois={}
#-----------Partie des phrases francaise----------------------
	article_fran=str(root.xpath("string(//articlefran[@id='"+str(i)+"'])")).strip()
	phrase_list_francais=sent_tokenize(article_fran)

	for phrase in phrase_list_francais:
		toto=Phraseinfo(phrase)
		toto.get_pos()
		mergedic(dico_article_francais,toto.posdic)
	print("for all the article, the amount of pos-tag:",sorted(dico_article_francais.items(),key=lambda d:d[1], reverse = True))
	mergedic(dico_all_francais,dico_article_francais)

#------Partie des phrases chinoises--------------------------
	article_chinois=str(root.xpath("string(//articlechin[@id='"+str(i)+"'])")).strip()
	phrase_list_chinois=cut_sent(article_chinois)

	for phrase in phrase_list_chinois:
		toto=Phrase_chi_info(phrase)
		toto.poschaine()
		mergedic(dico_article_chinois,toto.posdic)
	print("for the whole chinese article, the amount of pos-tag",sorted(dico_article_chinois.items(),key=lambda d:d[1], reverse = True))
	mergedic(dico_all_chinois,dico_article_chinois)

print("all in all, french pos-tag----------",sorted(dico_all_francais.items(),key=lambda d:d[1], reverse = True))
print("all in all, chinese pos-tag----------",sorted(dico_all_chinois.items(),key=lambda d:d[1], reverse = True))

	