from tkinter import *
from tkinter.ttk import *
import random
from time import strftime 
from PIL import Image, ImageTk




class Bullet: 
    def levelup(self):
        print(self.levelup_degree)


class Mushroom(Bullet):
    def __init__(self):
        self.name = "Mushroom"
        self.bullet_image = "mushroom.jpg"
        self.levelup_degree = 10


class Turtle(Bullet):
    def __init__(self):
        self.name = "Turtle"
        self.bullet_image = "turtle.png"
        self.levelup_degree = 20






x = 1


mushroomx= 1310
mushroomy= 650





def placemushroom(x,y):
    load = Image.open("turtle.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=x, y=y)


def placemario(x,y):
    load = Image.open("mario.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=x, y=y)


def PlaceImage(x,y,img,window):
    load = Image.open(img)
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.place(x=x, y=y)



def update(): 
    global mushroomx
    global mushroomy
    lbl.config(text = "Fired!")
    #lbl.config(text = strftime('%H:%M:%S %p'))
    lbl.after(300, update)
    PlaceImage(0,0,"bg.png",root)
    if (mushroomx <= 0) or (mushroomy <= 0):
        print("outttt")
        exit()
    else:
        mushroomx -= int(speedcombo.get())
        mushroomy -= int(Powercombo.get())
        placemushroom(mushroomx,mushroomy)
        placemario(mariox,marioy)
    



def SelectMushroom():
    global player
    player = Mushroom()
    selectplayer.destroy()

def SelectTurtle():
    global player
    player = Turtle()
    selectplayer.destroy()




selectplayer = Tk()
PlaceImage(-600,-500,"bg.png",selectplayer)

titre = Label(selectplayer,text= "Select Your Bullet" , font = ('arial', 20, 'bold'), foreground = 'red')
titre.pack(anchor = 'center') 



PlaceImage(80,180,"mushroom.jpg",selectplayer)
lbl1 = Label(selectplayer,text= "Mushroom", font = ('arial', 20, 'bold'), foreground = 'red')
lbl1.place(x=50,y=120)

lbl3 = Label(selectplayer,text= "Successful Shot:", font = ('arial', 15, 'bold'), foreground = 'red')
lbl3.place(x=35,y=270)


lbl5 = Label(selectplayer,text= "+10 Points", font = ('arial', 20, 'bold'), foreground = 'red')
lbl5.place(x=50,y=300)

btn = Button(selectplayer, text="Select Mushroom", command=SelectMushroom)
btn.place(x=55,y=340)








PlaceImage(370,195,"turtle.png",selectplayer)
lbl2 = Label(selectplayer,text= "Turtle", font = ('arial', 20, 'bold'), foreground = 'red')
lbl2.place(x=353,y=120)

lbl4 = Label(selectplayer,text= "Successful Shot:", font = ('arial', 15, 'bold'), foreground = 'red')
lbl4.place(x=310,y=270)

lbl6 = Label(selectplayer,text= "+20 Points", font = ('arial', 20, 'bold'), foreground = 'red')
lbl6.place(x=325,y=300)

btn1 = Button(selectplayer, text="Select Turtle", command=SelectTurtle)
btn1.place(x=348,y=340)








selectplayer.geometry("529x460")
selectplayer.mainloop()











for i in range(0,x):
    root = Tk()
    PlaceImage(0,0,"bg.png",root)
    print(player.name)
    mariox = random.randrange(50, 850)
    marioy = random.randrange(50, 650)
    placemario(mariox,marioy)
    
    placemushroom(mushroomx,mushroomy)


    speedcombo = Combobox(root)
    speedcombo['values']= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    speedcombo.current(0)
    speedcombo.place(x=1350, y=890)
    speedlable = Label(root, text="Select Speed (1 to 10)")
    speedlable.place(x=1200, y=891)



    Powercombo = Combobox(root)
    Powercombo['values']= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    Powercombo.current(0)
    Powercombo.place(x=1350, y=920)
    Powerlable = Label(root, text="Select Power (1 to 10)")
    Powerlable.place(x=1200, y=921)




        
        
        
    




    lbl = Label(root, font = ('arial', 20, 'bold'), foreground = 'red') 
    lbl.pack(anchor = 'center') 





    








    btn = Button(root, text="Fire!", command=update)
    btn.place(x=1310, y=945)
















    




    root.geometry("1529x976")
    root.mainloop()

