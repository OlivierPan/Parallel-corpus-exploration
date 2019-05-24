from lxml import etree
from nltk import sent_tokenize, word_tokenize
with open("/Users/pansa/Desktop/statistique_textuelle/corpus_parrale.xml","r") as file:
    content=file.read()
root=etree.XML(content)
doc=etree.ElementTree(root)
x=0
for i in range(0,10):

	article_fran=str(root.xpath("string(//articlefran[@id='"+str(i)+"'])")).strip()
	longueur_fran=len(word_tokenize(article_fran))

	article_chin=str(root.xpath("string(//articlechin[@id='"+str(i)+"'])")).strip()
	longueur_chin=len(article_chin)

	print("longueur_chin",longueur_chin)
	print("longueur_fran",longueur_fran)
	print("longueur article chinois - longueur article francais = " + str(longueur_chin-longueur_fran),end="\n\n")
	x+=longueur_chin-longueur_fran
print(x)

"""
longueur_chin 306
longueur_fran 259
longueur article chinois - longueur article francais = 47

longueur_chin 1258
longueur_fran 1075
longueur article chinois - longueur article francais = 183

longueur_chin 4746
longueur_fran 3407
longueur article chinois - longueur article francais = 1339

longueur_chin 843
longueur_fran 889
longueur article chinois - longueur article francais = -46

longueur_chin 583
longueur_fran 576
longueur article chinois - longueur article francais = 7

longueur_chin 490
longueur_fran 333
longueur article chinois - longueur article francais = 157

longueur_chin 532
longueur_fran 368
longueur article chinois - longueur article francais = 164

longueur_chin 1333
longueur_fran 1026
longueur article chinois - longueur article francais = 307

longueur_chin 536
longueur_fran 388
longueur article chinois - longueur article francais = 148

longueur_chin 1339
longueur_fran 1002
longueur article chinois - longueur article francais = 337

2643

"""