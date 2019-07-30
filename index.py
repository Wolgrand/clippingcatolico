#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Arquivo para ler os links RSS, Fazer o Download das Imagens, Criar os Posts do IG e Publicar no IG
from robots.rssRead import RssRead
import atoma, requests
import json
import datetime
from robots.Imagem import *
from robots.Instagram import postar_fotos
from robots.stories import upload_stories
from robots.spider import *
import random
from tinydb import TinyDB, Query, where


RssRead()

#Criar base dados JSON - db.json
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False, encoding='utf-8')
#Procurar na base de dados JSON os itens que ainda não foram postados
nao_foi_postado = db.search(Query().postado == 'não')
#Ordenar os os itens de maneira aleatória
random.shuffle(nao_foi_postado)
nao_foi_postado = sorted(nao_foi_postado, key = lambda k:k['date'], reverse = True)
index = 1
print(nao_foi_postado)

#Criação do texto para o instagram, primeira parte
captionText = str('Clipping Católico ' + datetime.date.today().strftime('%d-%m-%Y'))

#Variavéis que irão conter o caminhos para as imagens
media = []


#Iterar pelos itens não postados
for post in nao_foi_postado:
    #Retornar apenas os 10 primeiros itens
    if(index<=5):
        if(post['source']=='Aleteia'):
            #caso dê algum erro com este item o robô pula para o próximo
            try:
                media_post = {}
                spider_aleteia(post['link'], index)
                titles = db.search(Query().titulo == post['titulo'])
                for title in titles:
                    title['postado'] = 'sim'
                db.write_back(titles)
                print('Criando postagem Aleteia...')
                create_post(str('Images/imagem-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                print('Postagem Aleteia Criada')
                #create_stories(str('Images/stories-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                #upload_stories('Images/stories-'+str(index)+'.jpg')
                media_post['type'] = 'photo'
                media_post['file'] = 'Images/post-'+str(index)+'.jpg'
                media.append(media_post)
                captionText = captionText + str('\u2063\n' + "-------" + '\u2063\n' + str(index) +'-Postado por ' + post['source'] + '\u2063\n'+" " + '\u2063\n' + post['titulo'] + '\u2063\n' +" " + '\u2063\n'+'Link: ' + post['link'] + '\u2063\n')
                index = index + 1
            except:
                print('Erro ao ler '+ post['link'])
                index = index
        elif(post['source']=='VaticanNews'):
            try:
                media_post = {}
                spider_VaticanNews(post['link'], index)
                titles = db.search(Query().titulo == post['titulo'])
                for title in titles:
                    title['postado'] = 'sim'
                db.write_back(titles)
                create_post(str('Images/imagem-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                print('Criando postagem VaticanNews...')
                #create_stories(str('Images/stories-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                #upload_stories('Images/stories-'+str(index)+'.jpg')
                media_post['type'] = 'photo'
                media_post['file'] = 'Images/post-'+str(index)+'.jpg'
                media.append(media_post)
                captionText = captionText + str('\u2063\n' + "-------" + '\u2063\n' + str(index) +'-Postado por ' + post['source'] + '\u2063\n'+" " + '\u2063\n' + post['titulo'] + '\u2063\n' +" " + '\u2063\n'+'Link: ' + post['link'] + '\u2063\n')
                index = index + 1
            except:
                print('Erro ao ler '+ post['link'])
                index = index
        elif(post['source']=='AciDigital'):
            try:
                media_post = {}
                spider_AciDigital(post['link'], index)
                titles = db.search(Query().titulo == post['titulo'])
                for title in titles:
                    title['postado'] = 'sim'
                db.write_back(titles)
                create_post(str('Images/imagem-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                print('Criando postagem AciDigital...')
                #create_stories(str('Images/stories-' + str(index) + '.jpg'), post['titulo'], post['source'], str(index))
                #upload_stories('Images/stories-'+str(index)+'.jpg')
                media_post['type'] = 'photo'
                media_post['file'] = 'Images/post-'+str(index)+'.jpg'
                media.append(media_post)
                captionText = captionText + str('\u2063\n' + "-------" + '\u2063\n' + str(index) +'-Postado por ' + post['source'] + '\u2063\n'+" " + '\u2063\n' + post['titulo'] + '\u2063\n' +" " + '\u2063\n'+'Link: ' + post['link'] + '\u2063\n')
                index = index + 1
            except:
                print('Erro ao ler '+ post['link'])
                index = index
        
captionText = captionText + str('\u2063\n' +"-----" + '\u2063\n' +'#noticias #fe #papa #clipping #igreja #catolicos #igrejacatolica')


print(media)
if(index>=2):
    postar_fotos(media, captionText)