# -*- coding:utf-8 -*-
import pygame
from pygame.locals import*
import sys

def main():
    pygame.init() #初期化
    screen = pygame.display.set_mode((300,400)) # 400*400の画面
    #screen = pygame.display.set_mode((400,400),FULLSCREEN) #フルスクリーン (解除時は大きさ400*300の画面)
    pygame.display.set_caption("Screen") #タイトルバーに表示する名前

    while(1):
        screen.fill((198,198,198)) #画面を黒色(#000000)に塗る
        pygame.display.update() #画面を更新

        #イベント処理
        for event in pygame.event.get():
            if event.type == QUIT: #閉じるボタンが押されたら終了
                pygame.quit() #Pygameの終了(画面閉じられる)
                sys.exit()

if __name__ =="__main__":
    main()