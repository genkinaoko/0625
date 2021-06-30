import sys
from PIL import Image, ImageFont, ImageDraw

#aa = r"/Users/genkitakasaki1/Desktop/git/0625/picpic/m.txt"
with open("/Users/genkitakasaki1/Desktop/git/0625/Mac/result/del.txt") as f:
    aa = f.read()
    
lines = aa.split("\n")

font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 11)
w,h = max(font.getsize(line) for line in lines)

imag = Image.new("RGB", (w, h*len(lines)), "#ffffff")
draw = ImageDraw.Draw(imag)

for i,line in enumerate(lines):
    draw.text((0, i*h), line, font=font, fill="#000000")

# 表示
imag.save("/Users/genkitakasaki1/Desktop/git/0625/Mac/result/next2.png")