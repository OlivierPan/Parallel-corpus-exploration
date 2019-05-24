from lxml import etree
from nltk import sent_tokenize, word_tokenize
import re
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


for i in range(0,10):

	article_fran=str(root.xpath("string(//articlefran[@id='"+str(i)+"'])")).strip()
	longueur_fran=len(word_tokenize(article_fran))
	phrase_list_francais=sent_tokenize(article_fran)
	#print(phrase_list_francais)
	print("le nombre de phrase dans l'article francais =",len(phrase_list_francais))
	print("En moyenne, chaque phrase française a combien de tokens", longueur_fran/len(phrase_list_francais))


	article_chin=str(root.xpath("string(//articlechin[@id='"+str(i)+"'])")).strip()
	longueur_chin=len(article_chin)
	#phrase_list_chinois=cut_sent(article_chin)
	phrase_list_chinois=[x for x in cut_sent(article_chin) if x!=""]

	#print("longueur_chin",longueur_chin)
	#print("longueur_fran",longueur_fran)
	#print("longueur article chinois - longueur article francais = " + str(longueur_chin-longueur_fran),end="\n\n")
	#x+=longueur_chin-longueur_fran
	print("le nombre de phrase dans l'article chinois =",len(phrase_list_chinois))
	print("En moyenne, chaque phrase chinoise a combien de tokens", longueur_chin/len(phrase_list_chinois))
	#print(phrase_list_chinois,end="\n\n\n")
	x_chin+=longueur_chin/len(phrase_list_chinois)
	x_fran+=longueur_fran/len(phrase_list_francais)
#print(x)

print("la moyenne de token dans une phrase chinoises",x_chin/10)
print("la moyenne de tokens dans une phrase francaise",x_fran/10)

"""
le nombre de phrase dans l'article francais = 8
En moyenne, chaque phrase française a combien de tokens 32.375
le nombre de phrase dans l'article chinois = 8
En moyenne, chaque phrase chinoise a combien de tokens 38.25
le nombre de phrase dans l'article francais = 26
En moyenne, chaque phrase française a combien de tokens 41.34615384615385
le nombre de phrase dans l'article chinois = 30
En moyenne, chaque phrase chinoise a combien de tokens 41.93333333333333
le nombre de phrase dans l'article francais = 84
En moyenne, chaque phrase française a combien de tokens 40.55952380952381
le nombre de phrase dans l'article chinois = 93
En moyenne, chaque phrase chinoise a combien de tokens 51.03225806451613
le nombre de phrase dans l'article francais = 22
En moyenne, chaque phrase française a combien de tokens 40.40909090909091
le nombre de phrase dans l'article chinois = 18
En moyenne, chaque phrase chinoise a combien de tokens 46.833333333333336
le nombre de phrase dans l'article francais = 13
En moyenne, chaque phrase française a combien de tokens 44.30769230769231
le nombre de phrase dans l'article chinois = 9
En moyenne, chaque phrase chinoise a combien de tokens 64.77777777777777
le nombre de phrase dans l'article francais = 7
En moyenne, chaque phrase française a combien de tokens 47.57142857142857
le nombre de phrase dans l'article chinois = 7
En moyenne, chaque phrase chinoise a combien de tokens 70.0
le nombre de phrase dans l'article francais = 11
En moyenne, chaque phrase française a combien de tokens 33.45454545454545
le nombre de phrase dans l'article chinois = 9
En moyenne, chaque phrase chinoise a combien de tokens 59.111111111111114
le nombre de phrase dans l'article francais = 29
En moyenne, chaque phrase française a combien de tokens 35.37931034482759
le nombre de phrase dans l'article chinois = 35
En moyenne, chaque phrase chinoise a combien de tokens 38.08571428571429
le nombre de phrase dans l'article francais = 9
En moyenne, chaque phrase française a combien de tokens 43.111111111111114
le nombre de phrase dans l'article chinois = 9
En moyenne, chaque phrase chinoise a combien de tokens 59.55555555555556
le nombre de phrase dans l'article francais = 33
En moyenne, chaque phrase française a combien de tokens 30.363636363636363
le nombre de phrase dans l'article chinois = 37
En moyenne, chaque phrase chinoise a combien de tokens 36.189189189189186
la moyenne de token dans une phrase chinoises 50.57682726505307
la moyenne de tokens dans une phrase francaise 38.887749271800985
"""