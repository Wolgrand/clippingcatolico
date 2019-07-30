#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Arquivo para ler os links RSS, Fazer o Download das Imagens, Criar os Posts do IG e Publicar no IG
import atoma, requests
import json
import datetime
from robots.spider import spider_AciDigital, spider_aleteia, spider_VaticanNews
from tinydb import TinyDB, Query, where
import random

def RssRead():
  #Criar base dados JSON - db.json
  db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False, encoding='utf-8')
  titulo_postagem = Query()

  #Ler o feed Aleteia
  feed_name = "Aleteia"
  url = "https://pt.aleteia.org/feed/"
  response = requests.get(url)
  feed = atoma.parse_rss_bytes(response.content)

  #Salvar os itens do feed Aleteia na base de dados json
  for post in feed.items:

      data_postagem = post.pub_date.strftime('%d/%m/%Y')
      data_hoje = datetime.date.today().strftime('%d/%m/%Y')
      if(data_hoje == post.pub_date.strftime('%d/%m/%Y')):
          date = post.pub_date.strftime('%d/%m/%Y')
          if(db.contains(titulo_postagem.titulo == post.title)==False):
              db.insert({
                  'source': 'Aleteia',
                  'date': date,
                  'titulo': post.title,
                  'descrição': post.description,
                  'link': post.link,
                  'categorias': post.categories,
                  'postado': 'não',
                  })

  print('RSS Aleteia lido com sucesso!')
  #Ler o feed VaticanNews
  feed_name = "Vatican News"
  url = "https://www.vaticannews.va/pt.rss.xml"
  response = requests.get(url)
  feed = atoma.parse_rss_bytes(response.content)


  #Salvar os itens do feed VaticanNews na base de dados json
  for post in feed.items:
      data_postagem = post.pub_date.strftime('%d/%m/%Y')
      data_hoje = datetime.date.today().strftime('%d/%m/%Y')
      if(data_hoje == post.pub_date.strftime('%d/%m/%Y')):
          date = post.pub_date.strftime('%d/%m/%Y')
          if(db.contains(titulo_postagem.titulo == post.title)== False):
              db.insert({
                  'source': 'VaticanNews',
                  'date': date,
                  'titulo': post.title,
                  'descrição': post.description,
                  'link': post.link,
                  'categorias': post.categories,
                  'postado': 'não',
                  })

  print('RSS VaticanNews lido com sucesso!')
  #Ler o feed Aci Digital
  feed_name = "Aci Digital"
  url = "https://www.acidigital.com/rss/rss.php"
  response = requests.get(url)
  feed = atoma.parse_rss_bytes(response.content)


  #Salvar os itens do feed AciDigital na base de dados json
  for post in feed.items:
      data_postagem = post.pub_date.strftime('%d/%m/%Y')
      data_hoje = datetime.date.today().strftime('%d/%m/%Y')
      if(data_hoje == post.pub_date.strftime('%d/%m/%Y')):
          date = post.pub_date.strftime('%d/%m/%Y')
          if(db.contains(titulo_postagem.titulo == post.title)== False):
              db.insert({
                  'source': 'AciDigital',
                  'date': date,
                  'titulo': post.title,
                  'descrição': post.description,
                  'link': post.link,
                  'categorias': post.categories,
                  'postado': 'não',
                  })

  print('RSS Acidigital lido com sucesso!')