from PIL import Image, ImageDraw, ImageFont

text2 = open(r'C:\genkinaoko\git\0625\Win\result\out2.txt', 'r')
data = text2.read()

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (5000000, 5000000)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
img  = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(img)

# 用意した画像に文字列を描く
font = ImageFont.truetype(r"C:\Windows\Fonts\msgothic.ttc", 12)
textWidth, textHeight = draw.textsize(data,font=font)
textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
draw.text(textTopLeft, data, fill=textRGB, font=font)

img.save(r"C:\genkinaoko\git\0625\Win\result\out.png")
text2.close()