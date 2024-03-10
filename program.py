import tkinter

#キー入力
key = ""
koff = False

def key_down(e):
    global key,koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

player_x = 90
player_y = 90

map_data = [
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,2,2,2,2,2,2,2,2,2,0],
    [0,1,1,1,1,1,1,1,1,1,1,0]
]


#ステージの描画
def draw_screen():
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]],tag="SCREEN")
    canvas.create_image(player_x,player_y,image=img_player,tag="SCREEN")

#キャラクターの移動方向に壁があるか調べる
def check_wall(cx,cy,di):
    check = False
    if di == DIR_UP:
        mx = int(cx/60)
        my = int((cy-60)/60)
        if map_data[my][mx] <= 1:
            check = True
    if di == DIR_DOWN:
        mx = int(cx/60)
        my = int((cy+60)/60)
        if map_data[my][mx] <= 1:
            check = True
    if di == DIR_LEFT:
        mx = int((cx-60)/60)
        my = int(cy/60)
        if map_data[my][mx] <= 1:
            check = True
    if di == DIR_RIGHT:
        mx = int((cx+60)/60)
        my = int(cy/60)
        if map_data[my][mx] <= 1:
            check = True                
    return check

#プレイヤーを動かす
def move_player():
    global player_x,player_y
    if key == "Up":
        if check_wall(player_x,player_y,DIR_UP) == False:
            player_y = player_y - 60
    if key == "Down":
        if check_wall(player_x,player_y,DIR_DOWN) == False:
            player_y = player_y + 60
    if key == "Left":
        if check_wall(player_x,player_y,DIR_LEFT) == False:
            player_x = player_x - 60
    if key == "Right":
        if check_wall(player_x,player_y,DIR_RIGHT) == False:
            player_x = player_x + 60

def main():
    global key,koff
    draw_screen()
    move_player()
    if koff == True:
        key = ""
        koff = False
    root.after(100,main)

    
root = tkinter.Tk()
img_bg = [
    tkinter.PhotoImage(file="chip00.png"),
    tkinter.PhotoImage(file="chip01.png"),
    tkinter.PhotoImage(file="chip02.png"),
    tkinter.PhotoImage(file="chip03.png")
]
img_player = tkinter.PhotoImage(file="pen03.png")
root.title("トップビューアクション")
root.resizable(False,False)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
main()
root.mainloop()
    
