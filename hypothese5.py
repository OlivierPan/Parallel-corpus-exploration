#coding:utf-8
from lxml import etree
#from nltk import sent_tokenize, word_tokenize
import re
import os
import sys
import subprocess
#sys.path.insert(0,'/users/pansa/desktop/statistique_textuelle')#This is important, insert a path
#from traitement_phrase_chinoise import Phrase_chi_info#and this one too
#from phrase_fran import Phraseinfo
import thulac
fenci=thulac.thulac(seg_only=True)

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

def get_lemma(phrase):# for french
    with open("tobedeletelemma.txt","w") as file:

        file.write(phrase)
    output=subprocess.check_output("/Users/pansa/Desktop/treetagger/tree-tagger-french tobedeletelemma.txt",shell=True)#这个结果是需要CD 到treetagger的盘中
    temp=str(output,'utf-8')
    temp=temp.strip()
  # take the third element of each list, that can do the work
    token_pos_lemma=temp.split("\n")
    lemma_chaine=[]
    for element in token_pos_lemma:
      lemma=element.split("\t")[2]
      lemma_chaine.append(lemma)
    lemmadic={}
    lemma_list_sans_doublons=list(set(lemma_chaine))
    for lemma in lemma_list_sans_doublons:
    	lemmadic[lemma]=lemma_chaine.count(lemma)
    os.remove("tobedeletelemma.txt")
    return lemmadic

def get_mot(article):
    mots=fenci.cut(article,text=True)
    mot_list=mots.split(" ")
    mot_list_sans_doublons=list(set(mot_list))
    lemmadic={}
    for mot in mot_list_sans_doublons:
        lemmadic[mot]=mot_list.count(mot)
    return lemmadic

all_lemma_francais={}
all_lemma_chinois={}
for i in range(0,10):
#-----------Partie des phrases francaise----------------------
	article_fran=str(root.xpath("string(//articlefran[@id='"+str(i)+"'])")).strip()
	articledic=get_lemma(article_fran)

	print("for all the article, lemma:",sorted(articledic.items(),key=lambda d:d[1], reverse = True),end="\n\n\n")
	mergedic(all_lemma_francais,articledic)

#------Partie des phrases chinoises--------------------------
	article_chinois=str(root.xpath("string(//articlechin[@id='"+str(i)+"'])")).strip()
	articlechinoisdic=get_mot(article_chinois)
	print("for the whole chinese article, the amount of pos-tag",sorted(articlechinoisdic.items(),key=lambda d:d[1], reverse = True),end="\n\n\n")
	mergedic(all_lemma_chinois,articlechinoisdic)

print("all in all, french lemma----------",sorted(all_lemma_francais.items(),key=lambda d:d[1], reverse = True),end="\n\n\n")
print("all in all, chinese lemma----------",sorted(all_lemma_chinois.items(),key=lambda d:d[1], reverse = True),end="\n\n\n")

	