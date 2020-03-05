from tkinter import *
from tkinter.ttk import *
import random
from time import strftime 
from PIL import Image, ImageTk




root = Tk()


mushroomx= 1310
mushroomy= 650


def setBG():
    load = Image.open("bg2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)


def placemushroom(x,y):
    load = Image.open("mushroom.jpg")
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



def update(): 
    global mushroomx
    global mushroomy
    lbl.config(text = "Fired!")
    #lbl.config(text = strftime('%H:%M:%S %p'))
    lbl.after(300, update)
    setBG()
    if (mushroomx <= 0) or (mushroomy <= 0):
        print("outttt")
        pass
    else:
        mushroomx -= int(speedcombo.get())
        mushroomy -= int(Powercombo.get())
        placemushroom(mushroomx,mushroomy)
        placemario(mariox,marioy)
    



while True:

    setBG()
    
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

