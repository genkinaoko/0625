from PIL import Image,ImageDraw,ImageFont

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    fontname = r"/System/Library/Fonts/Menlo.ttc"
    fontsize = 11
    with open(r"/Users/genkitakasaki1/Desktop/git/0625/Mac/result/outt.txt") as f:
        text = f.read()   
    #text = "example@gmail.com"
    
    colorText = "black"
    #colorOutline = "red"
    colorBackground = "white"


    font = ImageFont.truetype(fontname, fontsize)
    width, height = getSize(text, font)
    img = Image.new('RGB', (width*2, height*2), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((2, height/2), text, fill=colorText, font=font)
    #d.rectangle((0, 0, width+3, height+3), outline=colorOutline)
    
    img.save(r"/Users/genkitakasaki1/Desktop/git/0625/Mac/result/next2.png")