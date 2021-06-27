from PIL import Image, ImageDraw, ImageFont
import os
import cv2

def Try(filepath):
    ttfontname = "/Library/Fonts/exljbris - MuseoSans-500.ttf"
    fontsize = 36
    img = Image.open(filepath)
    w, h = img.size
    aa = Image.new(mode = "RGBA", size = (w, h), color = (255,255,255))
    colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
    font = ImageFont.truetype(font=ttfontname, size=fontsize)
    pix = img.load()
    draw = ImageDraw.Draw(aa)
    for y in range(0, h, fontsize):
        for x in range(0, w, fontsize):
            draw.text(colorset[x // 4] * 2, text=char, fill="#000000", font=font)
            if x >= w - fontsize:
                print(char*2, end="\n")
            else:
                print(char*2, end=""
            

imgpath = "/Users/genkitakasaki1/Desktop/git/0625/picpic/bassho-2.jpg"

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
output = ""

for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colorset[dark // 4] * 2

