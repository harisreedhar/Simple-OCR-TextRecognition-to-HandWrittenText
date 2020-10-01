import os
import random
import textwrap
import pytesseract
from PIL import Image, ImageDraw, ImageFont

# convert image to text
def imageToText(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text

# get random canvas image
def getRandomCanvas(path):
    random_file = random.choice(os.listdir(path))
    bg_img = Image.open(os.path.join(path, random_file))
    return bg_img

# get white canvas image
def getWhiteCanvas(size):
    bg_image = Image.new('RGBA',size,'white')
    return bg_image

# write text to canvas
def drawTextToImage(text, image, fontSize, offset):
    font = ImageFont.truetype("data/font/Snake.ttf", fontSize)
    #w, h = font.getsize(text)
    draw = ImageDraw.Draw(image)
    draw.text(offset, text, font=font, fill="black")

# text wrap
def wrapText(text, size):
    wrapper = textwrap.TextWrapper(width=size)
    return wrapper.fill(text=text)

text = imageToText('input/sample.jpg')
canvas_img = getRandomCanvas("data/backgrounds/")
#text = wrapText(text, 60)
drawTextToImage(text, canvas_img, 36, (30,40))
canvas_img.save(os.path.join(os.getcwd(),"output.png"))
#canvas_img.show()
