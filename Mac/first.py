import cv2

colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "

imgpath = r"/Users/genkitakasaki1/Desktop/git/0625/picpic/seta2.jpg"
img = cv2.imread(imgpath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
output = ""

for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colorset[dark // 4] * 2

with open(r"/Users/genkitakasaki1/Desktop/git/0625/Mac/result/outt.txt", mode="w") as f:
    f.write(output)