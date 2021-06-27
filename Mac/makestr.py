from PIL import Image, ImageDraw, ImageFont

# 使うフォント，サイズ，描くテキストの設定
ttfontname = "/Library/Fonts/exljbris - MuseoSans-500.ttf"
fontsize = 36
#text = "TakasAKiGHenki"

text2 = open('/Users/genkitakasaki1/Desktop/git/0625/Mac/result/out4.txt', 'r')
data = text2.read()

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (5000000, 5000000)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
img  = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(img)

# 用意した画像に文字列を描く
font = ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(data,font=font)
textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
draw.text(textTopLeft, data, fill=textRGB, font=font)

img.save("/Users/genkitakasaki1/Desktop/git/0625/Mac/result/image2.png")
text2.close()