import requests
from bs4 import BeautifulSoup
#import urllib.request
import json
from PIL import Image, ImageDraw, ImageFont
from tilings import generate_hexagons, generate_squares, generate_triangles
from collections import namedtuple
import random
import datetime



#rgb(41, 128, 185)
#rgb(52, 152, 219)
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines

Color = namedtuple('Color', ['red', 'green', 'blue'])

def random_colors(color1, color2):
    """
    Generate random colors between ``color1`` and ``color2``.
    Both arguments should be instances of ``Color``.
    """
    # Get the difference along each axis
    d_red   = color1.red - color2.red
    d_green = color1.green - color2.green
    d_blue  = color1.blue - color2.blue

    while True:
        # What proportion of the line to move along
        proportion = random.uniform(0, 1)

        yield Color(
            red=color1.red - int(d_red * proportion),
            green=color1.green - int(d_green * proportion),
            blue=color1.blue - int(d_blue * proportion)
        )

def create_post(imagem, titulo, autor, postagem):
    # Create a blank 500x500 pixel image
    im = Image.new(mode='RGB', size=(1080, 1080))
    im2 = Image.new(mode='RGB', size=(1080, 250))

    # Generate random flat colors
    flat_colors_1 = [(26, 188, 156), (46, 204, 113), (52, 152, 219), (155, 89, 182), (241, 196, 15), (230, 126, 34), (231, 76, 60)]
    flat_colors_2 = [(22, 160, 133), (39, 174, 96), (41, 128, 185), (142, 68, 173), (243, 156, 18), (211, 84, 0), (192, 57, 43)]
    cor= random.randint(0,6)
    # Generate the shapes and colors, and draw them on the canvas
    forma = [generate_squares(1080, 1080),generate_hexagons(1080, 1080),generate_triangles(1080, 1080)]
    shapes = forma[random.randint(0,2)]
    colors = random_colors(Color(flat_colors_1[cor][0],flat_colors_1[cor][1], flat_colors_1[cor][2]), Color(flat_colors_2[cor][0],flat_colors_2[cor][1], flat_colors_2[cor][2] ) )
    for shape, color in zip(shapes, colors):
        ImageDraw.Draw(im).polygon(shape, fill=color)

    for shape, color in zip(shapes, colors):
        ImageDraw.Draw(im2).polygon(shape, fill=color)

    img = im
    #img.show()
    #img = Image.open('background/1-background.png')
    #img = ImageText((1080, 1080), background=(255, 255, 255)
    logo = Image.open(imagem)
    fator = 1080/logo.size[0]
    new_h = int(fator * logo.size[0])
    new_w = int(fator * logo.size[1])
    print (new_h, new_w)
    logo = logo.resize((new_h, new_w))
    img = img.resize((1080,1080))
    image_copy = img.copy()
    image_copy2 = img.copy()
    position = ((img.width - logo.width), int((img.height - logo.height)/2))
    image_copy.paste(logo, position)

    #draw = ImageDraw.Draw(image_copy)

    #Novo quadrado para o Titulo
    box = (0, 850, 1080, 1080)
    cropped_image = image_copy2.crop(box)
    positions = (0, 850)
    image_copy.paste(cropped_image, positions)

    #Novo quadrado para autor e data
    box = (0, 850, 1080, 1080)
    cropped_image = image_copy2.crop(box)
    positions = (0, 0)
    image_copy.paste(cropped_image, positions)
    draw = ImageDraw.Draw(image_copy)


    # if(postagem == 1):
    #     draw.ellipse(((850, 20, 870, 40)), fill=(255,255,255,0), width=100)
    #     draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    # elif(postagem == 2):
    #     draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((880, 20, 900, 40)), fill=(255,255,255,0), width=100)
    #     draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    # elif(postagem == 3):
    #     draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((910, 20, 930, 40)), fill=(255,255,255,0), width=100)
    #     draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    # elif(postagem == 4):
    #     draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((940, 20, 960, 40)), fill=(255,255,255,0), width=100)
    #     draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    # elif(postagem == 5):
    #     draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
    #     draw.ellipse(((970, 20, 990, 40)), fill=(255,255,255,0), width=100)
    #llx, lly = 0, img.size[1] / (5/4)

    # Add one to upper point because second point is just outside the drawn
    # rectangle.
    #size = img.size[1]
    #urx, ury = llx + size *2, lly + size + 1
    #draw.rectangle(((llx, lly), (urx, ury)), fill=(41,128,185,200))

    #font_titulo = ImageFont.truetype("arial.ttf", 50)
    font_titulo = ImageFont.truetype("arial.ttf", 50)
    font_autor = ImageFont.truetype("arial.ttf", 45)
    texto = titulo
    author = 'Publicado por '+ autor
    edicao = datetime.date.today().strftime('%d-%m-%Y')
    draw.text((70, 60), edicao, font=font_autor)
    #print((position[1]-180))
    #print((position[1]-100))


    lines = text_wrap(texto, font_titulo, 1000)
    line_height = font_titulo.getsize('hg')[1]

    x = 55
    y = 860
    #print (len(lines))
    for line in lines:
        # draw the line on the image
        draw.text((x, y), line, font=font_titulo)

        # update the y position so that we can use it for next line
        y = y + line_height

    draw.text(((70), 140), author, font=font_autor)


    image_copy.save('Images/post-' + postagem + '.jpg')

def create_stories(imagem, titulo, autor, postagem):
    # Create a blank 500x500 pixel image
    im = Image.new(mode='RGB', size=(1080, 1920))


    # Generate random flat colors
    flat_colors_1 = [(26, 188, 156), (46, 204, 113), (52, 152, 219), (155, 89, 182), (241, 196, 15), (230, 126, 34), (231, 76, 60)]
    flat_colors_2 = [(22, 160, 133), (39, 174, 96), (41, 128, 185), (142, 68, 173), (243, 156, 18), (211, 84, 0), (192, 57, 43)]
    cor= random.randint(0,6)
    # Generate the shapes and colors, and draw them on the canvas
    forma = [generate_squares(1080, 1920),generate_hexagons(1080, 1920),generate_triangles(1080, 1920)]
    shapes = forma[random.randint(0,2)]
    colors = random_colors(Color(flat_colors_1[cor][0],flat_colors_1[cor][1], flat_colors_1[cor][2]), Color(flat_colors_2[cor][0],flat_colors_2[cor][1], flat_colors_2[cor][2] ) )
    for shape, color in zip(shapes, colors):
        ImageDraw.Draw(im).polygon(shape, fill=color)



    img = im


    logo = Image.open(imagem)
    fator = 2300/logo.size[0]
    new_h = int(fator * logo.size[0])
    new_w = int(fator * logo.size[1])
    print (new_h, new_w)
    logo = logo.resize((new_h, new_w))
    img = img.resize((1080,1920))
    image_copy = img.copy()
    #position = ((img.width - logo.width), int((img.height - logo.height)/2))
    position = ((img.width - logo.width), int(1920-new_w))
    image_copy.paste(logo, position)

    #draw = ImageDraw.Draw(image_copy)

    #Novo quadrado para o Titulo
    #box = (0, 800, 1080, 1920)
    #cropped_image = image_copy.crop(box)
    #positions = (0, 800)
    #image_copy.paste(cropped_image, positions)

    #Novo quadrado para autor e data
    #box = (0, 1000, 1080, 1920)
    #cropped_image = image_copy.crop(box)
    #positions = (0, 0)
    #image_copy.paste(cropped_image, positions)
    draw = ImageDraw.Draw(image_copy)


    if(postagem == 1):
        draw.ellipse(((850, 20, 870, 40)), fill=(255,255,255,0), width=100)
        draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    elif(postagem == 2):
        draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((880, 20, 900, 40)), fill=(255,255,255,0), width=100)
        draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    elif(postagem == 3):
        draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((910, 20, 930, 40)), fill=(255,255,255,0), width=100)
        draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    elif(postagem == 4):
        draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((940, 20, 960, 40)), fill=(255,255,255,0), width=100)
        draw.ellipse(((970, 20, 990, 40)), outline =(255,255,255,0), width=2)
    elif(postagem == 5):
        draw.ellipse(((850, 20, 870, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((880, 20, 900, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((910, 20, 930, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((940, 20, 960, 40)), outline =(255,255,255,0), width=2)
        draw.ellipse(((970, 20, 990, 40)), fill=(255,255,255,0), width=100)
    #llx, lly = 0, img.size[1] / (5/4)

    # Add one to upper point because second point is just outside the drawn
    # rectangle.
    #size = img.size[1]
    #urx, ury = llx + size *2, lly + size + 1
    #draw.rectangle(((llx, lly), (urx, ury)), fill=(41,128,185,200))

    font_titulo = ImageFont.truetype("arial.ttf", 60)
    font_autor = ImageFont.truetype("arial.ttf", 55)
    texto = titulo
    author = 'Publicado por '+ autor
    edicao = datetime.date.today().strftime('%d-%m-%Y')
    draw.text((70, 90), edicao, font=font_autor)


    lines = text_wrap(texto, font_titulo, 1000)
    line_height = font_titulo.getsize('hg')[1]

    x = 55
    y = 300
    #print (len(lines))
    for line in lines:
        # draw the line on the image
        draw.text((x, y), line, font=font_titulo)

        # update the y position so that we can use it for next line
        y = y + line_height

    draw.text(((70), 170), author, font=font_autor)


    image_copy.save('Images/stories-' + postagem + '.jpg')
    #image_copy.show()
#create_post('Images/imagem-1.jpg','5 hábitos que estão bloqueando a sua cura interior', 'Aleteia', '2')