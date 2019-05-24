#coding:utf-8
#this is for french phrase

from nltk import word_tokenize, sent_tokenize
import subprocess
import datetime
import os

corpus="""D’abord merci de m’accueillir, de nous accueillir avec la ministre des armées et la secrétaire d’Etat à l’égalité entre les femmes et les hommes et à la lutte contre les discriminations. Deux femmes du gouvernement, d’un gouvernement paritaire français et merci pour votre accueil qui me touche beaucoup et la chaleur de celui-ci.
Au fond vous me dites : c’est la première fois qu’un chef d’Etat étranger vient et passe du temps avec vous, c’est peut-être parce qu’on n’avait pas totalement compris ce qui était en train de se passer.
Parce que d’abord les femmes partout en Afrique sont en train de prendre le pouvoir ; et ensuite parce que l’avenir africain se construira par et à travers les femmes et l’autonomisation des femmes.
C’est exactement la chanson que Yasmine vient de nous chanter à l’instant, des femmes ministres, présidentes, avocates. Moi, cela fait la sixième fois que je viens dans le Sahel, c’est la première fois au Tchad et c’est vrai que depuis le discours que j’ai tenu il y a un peu plus d’un an à Ouagadougou, j’ai mis le sujet justement de l’autonomisation des jeunes filles, des femmes au coeur de cette politique, de cette stratégie.
Alors au début de mandat, j’ai choqué beaucoup de gens, je vous rassure, surtout les gens en Europe en disant : il y a une bombe démographique en Afrique, on ne peut pas ne pas la regarder, il y a une bombe démographique parce que le taux de natalité - tel qu’on le voit aujourd’hui - n’est pas soutenable, parce que l’Afrique est en train de progresser à un rythme démographique que les économies ne pourront pas absorber, parce que cela va créer des tas de déséquilibres.
Et qu’est-ce qu’il y a derrière ce taux ? On peut se le dire en vérité : une déscolarisation des jeunes filles, des mariages forcés et au fond il y a une fécondité choisie, il y a des choix de vie qui sont faits par certaines femmes ; et, à l’inverse, il y en a beaucoup qui sont subis.
Et au coeur de la stratégie à laquelle je crois très profondément, il y a cette autonomisation des jeunes filles, des femmes et il y a ces visages, ces portraits de femmes qui sont au fond ces portraits de la liberté, de l’intelligence et de la réussite.
Il y a ce livre qui a été fait par l’ambassade, "Portraits de femmes tchadiennes", et je crois qu’il y en a beaucoup qui sont dans la salle d’ailleurs et qui ont ces visages avec cette diversité de parcours.
Mais il y a aussi une réalité des chiffres qui est très cruelle. Il y a un taux d’alphabétisation des femmes de 22%, quand celui des hommes est à 54% ; il y a un taux de mariages avant 18 ans qui reste aux alentours de 70%, dans un pays où le président Déby et son épouse se sont profondément engagés, où il a eu le courage de passer des lois contre le mariage forcé. Et donc on doit quand même regarder cela en face.
Alors moi, je ne suis pas venu vous faire de grands discours, mais je suis venu simplement vous dire : je suis convaincu qu’une des clés de notre destin commun, il est dans la réussite de cette autonomisation des jeunes filles et des femmes.
Il est dans le fait de mettre le maximum de jeunes filles à l’école, de leur permettre de réussir et de choisir leur vie.
Moi, je n’ai pas à dire à une jeune fille tchadienne ce qu’elle doit faire, mais je ferai tout ce que je peux pour m’assurer qu’une jeune fille tchadienne puisse aller à l’école pour choisir sa vie et savoir ce qui est bon pour elle.
C’est de s’assurer que les lois sont respectées et qu’il n’y ait pas de mariage forcé, qu’elle puisse avoir une vie de jeune fille, d’adolescente normale et ensuite choisir aussi son mari et pas le subir.
Et c’est s’assurer ensuite que la santé est assurée pour les mamans et les enfants, pour toutes les femmes, parce que cela fait partie de cette émancipation indispensable.
Et c’est de s’assurer aussi qu’il y ait un véritable entrepreneuriat féminin qui est au coeur de cette stratégie d’émancipation, d’autonomisation.
Sur ces sujets, je reviendrai tout à l’heure sur ce que je veux que la France fasse à vos côtés, au côté du Tchad et de la société civile, mais moi je veux surtout vous entendre, parce que ce n’est pas à moi de vous faire un discours, moi président français, sur ce que doit être notre politique et votre vie.
Et donc je vous demanderai une chose, je crois comprendre que c’est plutôt votre tempérament, mais c’est de parler librement, de me dire ce que vous voulez faire, ce dont vous avez besoin, ce qui ne fonctionne pas aujourd’hui, ce qui rend votre vie plus dure et ce en quoi on peut aider pour changer cela.
Donc je ne serai pas plus long, moi je veux vous entendre maintenant et qu’on débatte très librement. Mais s’il vous plaît, pas de tabous. Alors maintenant à vous de jouer.
(Source : site Internet de la présidence de la République)"""

content=sent_tokenize(corpus)

for phrase in content:
	with open('tobedelete.txt','w') as file:
		file.write(phrase)
	output=subprocess.check_output("/Users/pansa/Desktop/treetagger/tree-tagger-french tobedelete.txt",shell=True)#这个结果是需要CD 到treetagger的盘中
	temp=str(output,'utf-8')
	temp=temp.strip()
	# take the third element of each list, that can do the work
	token_pos_lemma=temp.split("\n")
	pos_chaine=[]
	for element in token_pos_lemma:
		pos=element.split("\t")[1]
		pos_chaine.append(pos)
	print(pos_chaine)
	posdic={}
	pos_list_sans_doublons=list(set(pos_chaine))
	for pos in pos_list_sans_doublons:
		posdic[pos]=pos_chaine.count(pos)
	print(posdic)
	os.remove('tobedelete.txt')
	



starttime=datetime.datetime.now()
endtime=datetime.datetime.now()
print('script working time = '+str(endtime-starttime))