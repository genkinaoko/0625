from PIL import Image, ImageDraw
import numpy as np

colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "

img_path = r"/Users/genkitakasaki1/Desktop/git/0625/picpic/bassho-2.jpg"
img = Image.fromarray(img_path)
gray = img.convert("L")
new_array = np.array(gray)
lines = [0]*gray.size[1]

for i in range(0, gray.size[1]):
    print(" ")
    for j in range(0, gray.size[0]):
        print(colorset[new_array // 4] * 2, end="")
    print("\n")

