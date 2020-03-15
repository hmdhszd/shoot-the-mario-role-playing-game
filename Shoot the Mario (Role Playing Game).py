from tkinter import *
from tkinter.ttk import *
import random
from time import strftime
from PIL import Image, ImageTk
import pygame




class Bullet:
    def __init__(self):
        self.point = 0
        
    def levelup(self):
        self.point += self.levelup_degree
        print(self.point)


class Mushroom(Bullet):
    def __init__(self):
        super().__init__()
        self.name = "Mushroom"
        self.bullet_image = "mushroom.jpg"
        self.bullet_width = 74
        self.bullet_height = 72
        self.levelup_degree = 10


class Turtle(Bullet):
    def __init__(self):
        super().__init__()
        self.name = "Turtle"
        self.bullet_image = "turtle.png"
        self.bullet_width = 43
        self.bullet_height = 39
        self.levelup_degree = 20



how_many_rounds = 6
position_of_mario = {(0,0)}



def PlaceImage(x,y,img,window):
    load = Image.open(img)
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.place(x=x, y=y)



def update(): 
    global bulletplacex
    global bulletplacey
    lblll.config(text = "Fired!")
    lblll.after(500, update)
    PlaceImage(0,0,"bg.png",root)

    
    
    if (bulletplacex <= 0) or (bulletplacey <= 0):
        print("outttt")
        root.destroy()
        
    elif (((bulletplacex,bulletplacey) in position_of_mario) or ((bulletplacex  + player.bullet_width,bulletplacey) in position_of_mario) or ((bulletplacex,bulletplacey + player.bullet_height) in position_of_mario) or ((bulletplacex + player.bullet_width,bulletplacey + player.bullet_height) in position_of_mario)):
        print("khordddd")
        player.levelup()
        root.destroy()

    else:
        bulletplacex -= int(speedcombo.get())
        bulletplacey -= int(Powercombo.get())
        PlaceImage(bulletplacex,bulletplacey, player.bullet_image ,root)
        PlaceImage(mariox,marioy, "mario.jpg", root)
        
    



def SelectMushroom():
    global player
    player = Mushroom()
    selectplayer.destroy()

def SelectTurtle():
    global player
    player = Turtle()
    selectplayer.destroy()


#________________________________________________________


selectplayer = Tk()
PlaceImage(-600,-500,"bg.png",selectplayer)

pygame.init()
pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play()

titre = Label(selectplayer,text= "Select Your Bullet" , font = ('arial', 20, 'bold'), foreground = 'red')
titre.pack(anchor = 'center') 

#________________________________________________________


PlaceImage(80,180,"mushroom.jpg",selectplayer)
lbl1 = Label(selectplayer,text= "Mushroom", font = ('arial', 20, 'bold'), foreground = 'red')
lbl1.place(x=50,y=120)

lbl3 = Label(selectplayer,text= "Successful Shot:", font = ('arial', 15, 'bold'), foreground = 'red')
lbl3.place(x=35,y=270)


lbl5 = Label(selectplayer,text= "+10 Points", font = ('arial', 20, 'bold'), foreground = 'red')
lbl5.place(x=50,y=300)

btn = Button(selectplayer, text="Select Mushroom", command=SelectMushroom)
btn.place(x=55,y=340)


#________________________________________________________


PlaceImage(370,195,"turtle.png",selectplayer)
lbl2 = Label(selectplayer,text= "Turtle", font = ('arial', 20, 'bold'), foreground = 'red')
lbl2.place(x=353,y=120)

lbl4 = Label(selectplayer,text= "Successful Shot:", font = ('arial', 15, 'bold'), foreground = 'red')
lbl4.place(x=310,y=270)

lbl6 = Label(selectplayer,text= "+20 Points", font = ('arial', 20, 'bold'), foreground = 'red')
lbl6.place(x=325,y=300)

btn1 = Button(selectplayer, text="Select Turtle", command=SelectTurtle)
btn1.place(x=348,y=340)


#________________________________________________________

selectplayer.geometry("529x460")
selectplayer.mainloop()

#________________________________________________________
#________________________________________________________




for i in range(1,how_many_rounds):
    pygame.init()
    pygame.mixer.music.load("music2.mp3")
    pygame.mixer.music.play()
    bulletplacex= 1310
    bulletplacey= 650
    root = Tk()
    PlaceImage(0,0,"bg.png",root)
    mariox = random.randrange(50, 850)
    marioy = random.randrange(50, 650)
    PlaceImage(mariox,marioy, "mario.jpg", root)
    PlaceImage(bulletplacex,bulletplacey, player.bullet_image , root)
    
    

    #________________________________________________________


    for ii in range(mariox , (mariox + 135)):
        for jj in range(marioy, (marioy + 163)):
            position_of_mario.add((ii,jj))
    
       
    #________________________________________________________

       
    speedcombo = Combobox(root)
    speedcombo['values']= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    speedcombo.current(0)
    speedcombo.place(x=1350, y=890)
    speedlable = Label(root, text="Horizontal (10 to 100)")
    speedlable.place(x=1200, y=891)



    Powercombo = Combobox(root)
    Powercombo['values']= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    Powercombo.current(0)
    Powercombo.place(x=1350, y=920)
    Powerlable = Label(root, text="Vertical (10 to 100)")
    Powerlable.place(x=1200, y=921)


    #________________________________________________________


    gameround = "round " + str(i) + " of " + str(how_many_rounds-1)

    pointtt = Label(root, font = ('arial', 20, 'bold'), foreground = 'red', text=gameround ) 
    pointtt.pack(anchor = 'center') 

    gamepoint = "your point is " + str(player.point)
    lblll = Label(root, font = ('arial', 20, 'bold'), foreground = 'red', text=gamepoint) 
    lblll.pack(anchor = 'center') 


    #________________________________________________________
    
    btn = Button(root, text="Fire!", command=update)
    btn.place(x=1310, y=945)

    root.geometry("1529x976")
    root.mainloop()


#________________________________________________________
#________________________________________________________



endingpage = Tk()
PlaceImage(-600,-500,"bg.png",endingpage)

titre = Label(endingpage,text= "Game is finished" , font = ('arial', 20, 'bold'), foreground = 'red')
titre.pack(anchor = 'center')

msgg = "Total Point is:" + str(player.point)
titre = Label(endingpage,text= msgg , font = ('arial', 20, 'bold'), foreground = 'red')
titre.pack(anchor = 'center')
endingpage.mainloop()
