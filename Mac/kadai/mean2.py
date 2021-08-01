# -*- coding: utf-8 -*-
from skimage import io

def main():
    # CSVファイルを取得
    img = io.imread(r"/Users/genkitakasaki1/Desktop/git/0625/picpic/lena.jpg")
    io.imshow(img)
    
if __name__ == "__main__":
    main()