#coding:utf-8
from nltk import word_tokenize, sent_tokenize
import subprocess
import os

class Phraseinfo():
  def __init__(self,phrase):
    self.phrase=phrase
    self.longueur=len(word_tokenize(phrase))

  
  def get_pos(self):
    with open('tobedelete.txt','w') as file:
                        file.write(self.phrase)
    output=subprocess.check_output("/Users/pansa/Desktop/treetagger/tree-tagger-french tobedelete.txt",shell=True)#这个结果是需要CD 到treetagger的盘中
    temp=str(output,'utf-8')
    temp=temp.strip()
  # take the third element of each list, that can do the work
    token_pos_lemma=temp.split("\n")
    pos_chaine=[]
    for element in token_pos_lemma:
      pos=element.split("\t")[1]
      pos_chaine.append(pos)
    #print(pos_chaine)
    posdic={}
    pos_list_sans_doublons=list(set(pos_chaine))
    for pos in pos_list_sans_doublons:
      posdic[pos]=pos_chaine.count(pos)
    #print(posdic)
    os.remove('tobedelete.txt')
    self.pos_chaine=pos_chaine
    self.posdic=posdic

    
# est-ce que c'est mieux d'utiliser jupyter notebook 
