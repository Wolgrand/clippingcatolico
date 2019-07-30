import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import html.parser


def spider_aleteia(url,ordem):
    URL = url
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, 'html.parser')

    imagem_post = soup.find('img', attrs={'class': 'post-thumb'})['data-lazy-src'].split('?')
    
    # Save the file
    imagem_download = urllib.request.urlopen(imagem_post[0])
    localFile = open('Images/imagem-' + str(ordem) + '.jpg', 'wb')
    localFile.write(imagem_download.read())
    localFile.close()

def spider_VaticanNews(url,ordem):
    URL = url
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, 'html.parser')

    
    imagem_post = soup.find('img', attrs={'class': 'cq-dd-image'})['data-original']
    if(imagem_post == None):
        imagem_post = soup.find('img', attrs={'class': 'embed-gallery__img'})['src']

    # Save the file
    imagem_download = urllib.request.urlopen('https://www.vaticannews.va'+imagem_post)
    localFile = open('Images/imagem-' + str(ordem) + '.jpg', 'wb')
    localFile.write(imagem_download.read())
    localFile.close()

def spider_AciDigital(url,ordem):
    URL = url
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, 'html.parser')

    imagem_post = soup.find('img', attrs={'class': 'main_image'})['src']
    if(imagem_post == None):
        imagem_post = soup.find('div', attrs={'class': 'ytp-cued-thumbnail-overlay-image'})['src']
    

    # Save the file
    imagem_download = urllib.request.urlopen('https://www.acidigital.com'+imagem_post)
    localFile = open('Images/imagem-' + str(ordem) + '.jpg', 'wb')
    localFile.write(imagem_download.read())
    localFile.close()
#spider_aleteia('https://pt.aleteia.org/2019/05/26/alcancando-a-tranquilidade-de-espirito-a-presenca-constante/',1)