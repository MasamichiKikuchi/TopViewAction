import pygame
import sys

img_bg = pygame.image.load("chip00.png"),
    #pygame.image.load (file="chip01.png"),
    #pygame.image.load (file="chip02.png"),
    #pygame.image.load (file="chip03.png")


def set_stage():#ステージのデータをセットする
    global map_data,candy
    map_data = [
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,3,2,2,2,2,2,2,2,2,3,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,3,2,2,2,2,2,2,2,2,3,0],
    [0,1,1,1,1,1,1,1,1,1,1,0]
    ]
    candy = 4

def draw_screen(bg):#ステージの描画
    bg.fill( 0, 0, 0)
    for y in range(9):
        for x in range(12):
            X = (x+5)*16
            Y = (y+5)*16
            if map_data[x][y] == 0:
                bg.bilt(img_bg,[X][Y])


def main():
    pygame.init()
    pygame.display.set_caption("トップビューアクション")
    screen = pygame.display.set_mode((800,600))
    set_stage()
    draw_screen(screen)

if __name__ == '__main__':
    main()
