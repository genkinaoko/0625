from PIL import Image, ImageDraw, ImageFont
import os

class Image2ascii():
    def __init__(self, filename):
        self.filename = filename
        self.input_image = Image.open(filename)
        self.w, self.h = self.input_image.size
    def set_size(self,w,h):
        self.w, self.h = w, h

    def set_output_image(self):
        self.output_image = Image.new(mode='RGBA', size=(self.w,self.h), color=(255,255,255)) # check variations

    def set_font(self, font="C:\\Windows\\Fonts\\msgothic.ttc", fontsize=23, encoding='utf-8'):
        self.font = font
        self.fontsize = fontsize
        self.encoding = encoding
        self.font = ImageFont.truetype(font=self.font, size=self.fontsize, encoding=self.encoding)

    def set_draw(self):
        self.draw = ImageDraw.Draw(self.output_image)

    def set_text_in_output_image(self, ascii='W#%*+;:,.  ', color='color'):
        self.color=color
        self.input_pix = self.input_image.load()
        for y in range(0, self.h, self.fontsize):
            for x in range(0, self.w, self.fontsize):
                r,g,b = self.input_pix[x,y]
                gray = r*0.2126 + g*0.7152 + b*0.0722
                character = ascii[int(gray//25)]
                if self.color == 'color':
                    self.draw.text((x,y),character,font=self.font,fill=(r,g,b))
                elif self.color == 'monotone':
                    self.draw.text((x,y), character,font=self.font,fill='#000000')
                else:
                    print('the variable color takes color or monotone')
                    break
                if x >= self.w-self.fontsize:
                    print(character, end='\n')
                else:
                    print(character, end='')
                    
    def save_output_image(self):
        filename = os.path.basename(self.filename)
        if self.color == 'monotone':
            self.output_image.save(os.path.splitext(filename)[0]+'_Ascii'+''.join(self.font.getname()).replace(' ', '')+str(self.fontsize)+'.png')
        elif self.color == 'color':
            self.output_image.save(os.path.splitext(filename)[0]+'_AsciiColor'+''.join(self.font.getname()).replace(' ', '')+str(self.fontsize)+'.png')
        else:
            print('the variable color takes color or monotone')
    def show(self):
        self.output_image.show()        



image2ascii = Image2ascii(r"C:\OneDriveNext\OneDrive - Nagasaki University\takapath\pic\ironman.jpg")
image2ascii.set_size(1061, 1500)
image2ascii.set_output_image()
image2ascii.set_font(fontsize=23)
image2ascii.set_draw()
image2ascii.set_text_in_output_image(ascii='W#%*+;:,.  ',color='monotone')
image2ascii.save_output_image()
image2ascii.show()