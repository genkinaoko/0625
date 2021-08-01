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
    bg = pygame.image.load(r"/Users/genkitakasaki1/Desktop/git/0625/game/board.png").convert_alpha()
    rect_bg = bg.get_rect()

    #王の画像(king.png)の取得
    king = pygame.image.load(r"/Users/genkitakasaki1/Desktop/git/0625/game/king.png").convert_alpha()
    rect_king = king.get_rect()
    rect_king.center = (150,350) #王の初期配置

    #金の画像(gold.png)の取得
    gold = pygame.image.load(r"/Users/genkitakasaki1/Desktop/git/0625/game/gold.png").convert_alpha()
    rect_gold = gold.get_rect()
    rect_gold.center = (50,350) #金の初期配置

    #銀の画像(silver.png)の取得
    silver = pygame.image.load(r"/Users/genkitakasaki1/Desktop/git/0625/game/silver.png").convert_alpha()
    rect_silver = silver.get_rect()
    rect_silver.center =(250,350) #銀の初期配置

    #歩の画像(pawn.png)の取得
    pawn = pygame.image.load(r"/Users/genkitakasaki1/Desktop/git/0625/game/pawn.png").convert_alpha()
    rect_pawn = pawn.get_rect()
    rect_pawn.center =(150,250)

    while(1):

        #キーイベント処理(キャラクタ画像の移動)
        pressed_key = pygame.key.get_pressed()
        #「←」キーが押されたらx座標を-5に移動
        if pressed_key[K_LEFT]:
            rect_king.move_ip(-5,0)
        #「→」キーが押されたらx座標を+5移動
        if pressed_key[K_RIGHT]:
            rect_king.move_ip(5,0)
        #「↑」キーが押されたらy座標を-5移動
        if pressed_key[K_UP]:
            rect_king.move_ip(0,-5)
        #「↓」キーが押されたらy座標を-5移動
        if pressed_key[K_DOWN]:
            rect_king.move_ip(0,5)

        pygame.display.update() #画面更新
        pygame.time.wait(100) #更新画面間隔
        screen.fill((0, 0, 0, 0)) #画面の背景色
        screen.blit(bg, rect_bg) #背景画像の描画
        screen.blit(king, rect_king) #王の画像の描画
        screen.blit(gold, rect_gold) #金の画像の描画
        screen.blit(silver, rect_silver) #銀の画像の描画
        screen.blit(pawn, rect_pawn) #歩の画像の描画

        #終了用イベント処理
        for event in pygame.event.get():
            #閉じるボタンが押されたとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ =="__main__":
        main()