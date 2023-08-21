from tkinter import * 
from PIL import Image, ImageTk
import screen3
import pandas as pd

df=pd.read_csv('Info.csv')

def show_quotes(genre):
    Quotes=[]
    for index,rows in df.iterrows():
        if genre in rows['category']:
            Quotes.append(rows['quote'])
    return(Quotes)


def create_screen2(root):
    frame = Frame(root)
    frame.config(width=700,height=700)
    w = Label(frame, text ='Pick the Genre', font = "50")
    w.grid(row=0,column=0)
    
    def on_button_1_click():
        Quotes= show_quotes('love')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'love',Quotes)
        newframe.pack()
    # # Load the image using PhotoImage
    image1 = Image.open("assets\icons\love.png").resize((100,100))
    tk_image1 = ImageTk.PhotoImage(image1)
    # # Create an image button
    image_button1 = Button(frame, image=tk_image1,command=on_button_1_click , bd=0)
    image_button1.image = tk_image1
    image_button1.grid(row=1,column=0,padx=10,pady=10)

    #button3

    def on_button_3_click():
         Quotes= show_quotes('freedom')
         frame.pack_forget()
         newframe=screen3.create_screen3(root,'freedom',Quotes)
         newframe.pack()
    image3 = Image.open("assets/icons/freedom.png").resize((100,100))
    tk_image3 = ImageTk.PhotoImage(image3)

    
    # # Create an image button
    image_button3 = Button(frame, image=tk_image3,command=on_button_3_click, bd=0)
    image_button3.image = tk_image3
    image_button3.grid(row=1,column=2,padx=10,pady=10)

#button4
    def on_button_4_click():
        Quotes= show_quotes('cool')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'cool',Quotes)
        newframe.pack()
    image4 = Image.open("assets\icons\cool.png").resize((100,100))
    tk_image4 = ImageTk.PhotoImage(image4)
    # # Create an image button
    image_button4 = Button(frame, image=tk_image4,command=on_button_4_click,bd=0)
    image_button4.image = tk_image4
    image_button4.grid(row=2,column=0,padx=10,pady=10)

    #button5
    def on_button_5_click():
        Quotes= show_quotes('gratitude')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'gratitude',Quotes)
        newframe.pack()
    image5 = Image.open("assets/icons/gratitude.png").resize((100,100))
    tk_image5 = ImageTk.PhotoImage(image5)
    # # Create an image button
    image_button5 = Button(frame, image=tk_image5,command=on_button_5_click,bd=0)
    image_button5.image = tk_image5
    image_button5.grid(row=2,column=1,padx=10,pady=10)

        #button6
    def on_button_6_click():
        Quotes= show_quotes('inspirational')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'inspirational',Quotes)
        newframe.pack()
    image6 = Image.open("assets\icons\inspirational.png").resize((100,100))
    tk_image6 = ImageTk.PhotoImage(image6)
    # # Create an image button
    image_button6 = Button(frame, image=tk_image6,command=on_button_6_click,bd=0)
    image_button6.image = tk_image6
    image_button6.grid(row=2,column=2,padx=10,pady=10)

        #button7
    def on_button_7_click():
        Quotes= show_quotes('knowledge')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'knowledge',Quotes)
        newframe.pack()
    image7 = Image.open("assets\icons\mindfulness.png").resize((100,100))
    tk_image7 = ImageTk.PhotoImage(image7)
    # # Create an image button
    image_button7 = Button(frame, image=tk_image7,command=on_button_7_click, bd=0)
    image_button7.image = tk_image7
    image_button7.grid(row=3,column=0,padx=10,pady=10)
            #button8
            
    def on_button_8_click():
        Quotes= show_quotes('meditation')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'meditation',Quotes)
        newframe.pack()
        
    image8 = Image.open("assets/icons/patience.png").resize((100,100))
    tk_image8 = ImageTk.PhotoImage(image8)
    # # Create an image button
    image_button8 = Button(frame, image=tk_image8,command=on_button_8_click,bd=0)
    image_button8.image = tk_image8
    image_button8.grid(row=3,column=1,padx=10,pady=10)
                #button9
    def on_button_9_click():
        Quotes= show_quotes('pray')
        frame.pack_forget()
        newframe=screen3.create_screen3(root,'pray',Quotes)
        newframe.pack()
    image9 = Image.open("assets/icons/hands_4955340.png").resize((100,100))
    tk_image9 = ImageTk.PhotoImage(image9)
    # # Create an image button
    image_button9 = Button(frame, image=tk_image9,command=on_button_9_click, bd=0)
    image_button9.image = tk_image9
    image_button9.grid(row=3,column=2,padx=10,pady=10)

    name = Label(frame,text ="Name : ",bg= '#80dfff', fg ="Black",width='5')
    #name.pack( side = RIGHT)
    name.place(x=100,y=380)
    e1 = Entry(frame,bg= '#80dfff', fg ="Black",width='30')
    e1.place(x=150,y=380)
    
    def Search():
        value=e1.get()
        quotes=show_quotes(value.lower())
        frame.pack_forget()
        newframe=screen3.create_screen3(root,value,quotes)
        newframe.pack()
    
    search = Button(frame, text ="Search",bg= '#80dfff', fg ="Black",command=Search)
    search.grid(row=4,column=1)


    return frame
