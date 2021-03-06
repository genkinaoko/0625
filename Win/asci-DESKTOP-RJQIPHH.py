import cv2

colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "

imgpath = r"C:\OneDriveNext\OneDrive - Nagasaki University\takapath\pic\seta2.jpg"
img = cv2.imread(imgpath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
output = ""

for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colorset[dark // 4] * 2

with open(r"C:\genkinaoko\git\0625\Win\result\out.txt", mode="w") as f:
    f.write(output)