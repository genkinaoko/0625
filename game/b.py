# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (300, 400) #画面サイズ
    (x,y) = (150, 200) #プレイヤー画像の初期配置(画面中央)
    pygame.init() #pygameの初期化
    pygame.display.set_mode((w,h), 0,32) #画面設定
    screen = pygame.display.get_surface()

    #背景画像 (bg.jpg)の取得
    img_path = r"/Users/genkitakasaki1/Desktop/git/0625/game/board.png"
    bg = pygame.image.load(img_path).convert_alpha()
    rect_bg = bg.get_rect()

    while(1):
        pygame.display.update() #画面更新
        pygame.time.wait(100) #更新画面間隔
        screen.fill((0, 0, 0, 0)) #画面の背景色
        screen.blit(bg, rect_bg) #背景画像の描画

        #終了用イベント処理
        for event in pygame.event.get():
            #閉じるボタンが押されたとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ =="__main__":
        main() 