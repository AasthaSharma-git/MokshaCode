from tkinter import * 
import screen1
import screen2


from PIL import Image, ImageTk
root = Tk()
root.title("Welcome")
root.geometry("700x700")
root.configure(bg='#9999ff')
topframe=screen1.create_screen1(root)
bottomframe=screen2.create_screen2(root)

topframe.pack()

def handleButtonClick1():
    bottomframe.pack()
    topframe.pack_forget()

def handleButtonClick2():
    bottomframe.pack_forget()
    topframe.pack()

b1_button = Button(topframe, text ="Explore Quotes",bg= '#80dfff', fg ="Black",command=handleButtonClick1)
b1_button.pack( side = LEFT)
#b1_button.place(x=3,y=380)

#name = Label(topframe,bg= '#80dfff',text = "Name: ")
#e1 = Entry(root)
#e1.pack( side = RIGHT)

#e1.grid(row=0,column=1)
#b2_button = Button(bottomframe, text ="Generate", fg ="red",command=handleButtonClick2)
#b2_button.pack( side = LEFT)




root.mainloop()