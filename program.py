import tkinter
import random

#キー入力
key = ""
koff = False

def key_down(e):
    global key,koff
    key = e.keysym
    koff = False

def key_up(e):
    global key
    key = ""

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

idx = 0
score = 0
candy = 0

player_x = 0
player_y = 0

enemy_x = 0
enemy_y = 0
enemy_d = 0#敵の向き

map_data = []

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

def set_chara_pos():
    global player_x,player_y
    global enemy_x,enemy_y,enemy_d
    player_x = 90
    player_y = 90
    enemy_x = 630
    enemy_y = 450

def draw_txt(txt,x,y,siz,col):#文字の描画
    fnt = ("Times New Roman",siz,"bold")
    canvas.create_text(x+2,y+2,text=txt,fill="black",font=fnt,tag="SCREEN")
    canvas.create_text(x,y,text=txt,fill=col,font=fnt,tag="SCREEN")


def draw_screen():#ステージの描画
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]],tag="SCREEN")
    canvas.create_image(player_x,player_y,image=img_player,tag="SCREEN")
    canvas.create_image(enemy_x,enemy_y,image=img_enemy,tag="SCREEN")
    draw_txt("SCORE"+str(score),200,30,30,"white")

#キャラクターの移動方向に壁があるか調べる
def check_wall(cx,cy,di,dot):
    check = False
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1:
            check = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1:
            check = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:
            check = True   
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:
            check = True
        mx = int((cy+29)/60)
        if map_data[my][mx] <= 1:
            check = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:
            check = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:
            check = True

    return check

#プレイヤーを動かす
def move_player():
    global player_x,player_y,score,candy

    if key == "w":
        if check_wall(player_x,player_y,DIR_UP,20) == False:
            player_y = player_y - 20
    if key == "s":
        if check_wall(player_x,player_y,DIR_DOWN,20) == False:
            player_y = player_y + 20
    if key == "a":
        if check_wall(player_x,player_y,DIR_LEFT,20) == False:
            player_x = player_x - 20
    if key == "d":
        if check_wall(player_x,player_y,DIR_RIGHT,20) == False :
            player_x = player_x + 20
    if key == "e":
        if check_wall(player_x,player_y,DIR_UP,20) == False and check_wall(player_x,player_y,DIR_RIGHT,20) == False :
            player_y = player_y - 20
            player_x = player_x + 20
    if key == "q":
        if check_wall(player_x,player_y,DIR_UP,20) == False and check_wall(player_x,player_y,DIR_LEFT,20) == False :
            player_y = player_y - 20
            player_x = player_x - 20
    if key == "x":
        if check_wall(player_x,player_y,DIR_DOWN,20) == False and check_wall(player_x,player_y,DIR_RIGHT,20) == False :
            player_y = player_y + 20
            player_x = player_x + 20
    if key == "z":
        if check_wall(player_x,player_y,DIR_DOWN,20) == False and check_wall(player_x,player_y,DIR_LEFT,20) == False :
            player_y = player_y + 20
            player_x = player_x - 20 

    if key == "space":
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y - 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
        player_y = player_y + 1
    mx = int(player_x/60)
    my = int(player_y/60)
    if map_data[my][mx] == 3:
        score = score + 100
        map_data[my][mx] = 2
        candy = candy - 1

def move_enemy():
    global idx,enemy_x,enemy_y,enemy_d
    speed = 10
    if enemy_x%60 == 30 and enemy_y%60 == 30:
        enemy_d = random.randint(0,6)
        if enemy_d >= 4:
            if player_y < enemy_y:
                enemy_d = DIR_UP
            if player_y > enemy_y:
                enemy_d = DIR_DOWN
            if player_x < enemy_x:
                enemy_d = DIR_LEFT
            if player_x > enemy_x:
                enemy_d = DIR_RIGHT 
    if enemy_d == DIR_UP:
        if check_wall(enemy_x,enemy_y,enemy_d,speed) == False:
            enemy_y = enemy_y - speed
    if enemy_d == DIR_DOWN:
        if check_wall(enemy_x,enemy_y,enemy_d,speed) == False:
            enemy_y = enemy_y + speed
    if enemy_d == DIR_LEFT:
        if check_wall(enemy_x,enemy_y,enemy_d,speed) == False:
            enemy_x = enemy_x - speed
    if enemy_d == DIR_RIGHT:
        if check_wall(enemy_x,enemy_y,enemy_d,speed) == False:
            enemy_x = enemy_x + speed
    if abs(enemy_x-player_x) <= 40 and abs(enemy_y-player_y)<=40:
        idx = 2
            
def main():
    global key,koff,idx,score
    draw_screen()
    if idx  == 0:
        canvas.create_image(360,200,tag="SCREEN")
        draw_txt("Press SPACE!",360,380,30,"yellow")
        if key == "space":
            score = 0
            set_stage()
            set_chara_pos()
            idx = 1

    if idx == 1:
        move_player()
        move_enemy()
        if candy == 0:
            idx = 3

    if idx == 2:
        draw_txt("GAME OVER",360,250,40,"red")
        draw_txt("Press SPACE!",360,380,30,"yellow")
        if key == "space":
            idx = 0
            

    if idx == 3:
        draw_txt("STAGE CLEAR",360,270,40,"pink")
        draw_txt("Press SPACE!",360,380,30,"yellow")
        if key == "space":
            idx = 0
    root.after(100,main)

    
root = tkinter.Tk()
img_bg = [
    tkinter.PhotoImage(file="chip00.png"),
    tkinter.PhotoImage(file="chip01.png"),
    tkinter.PhotoImage(file="chip02.png"),
    tkinter.PhotoImage(file="chip03.png")
]
img_player = tkinter.PhotoImage(file="pen03.png")
img_enemy = tkinter.PhotoImage(file="red03.png")
root.title("トップビューアクション")

root.resizable(False,False)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
set_stage()
set_chara_pos()
main()
root.mainloop()
    
