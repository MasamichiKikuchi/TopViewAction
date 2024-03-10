import tkinter

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

def draw_screen():
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]])

root = tkinter.Tk()
root.title("トップビューアクション")
root.resizable(False,False)
canvas = tkinter.Canvas(width=720,height=540)
canvas.pack()
img_bg = [
    tkinter.PhotoImage(file="chip00.png"),
    tkinter.PhotoImage(file="chip01.png"),
    tkinter.PhotoImage(file="chip02.png"),
    tkinter.PhotoImage(file="chip03.png"),
]
draw_screen()
root.mainloop()
    
