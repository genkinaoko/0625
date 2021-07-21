import sys
from PIL import Image, ImageFont, ImageDraw

#aa = r"/Users/genkitakasaki1/Desktop/git/0625/picpic/m.txt"
with open(r"C:\genkinaoko\git\0625\Win\result\out.txt") as f:
    aa = f.read()
    
lines = aa.split("\n")

font = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 17)
w,h = max(font.getsize(line) * 2 for line in lines)

imag = Image.new("RGB", (w, h*len(lines)), "#ffffff")
draw = ImageDraw.Draw(imag)

for i,line in enumerate(lines):
    draw.text((0, i*h), line, font=font, fill="#000000")

# 表示
imag.save(r"C:\genkinaoko\git\0625\Win\result\out.png")