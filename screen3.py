from tkinter import * 
from PIL import Image, ImageTk
import random
import screen2

def create_screen3(root,genre,Quotes):
    frame = Frame(root)
    frame.config(width=1200,height=1200)

    w = Label(frame, text =genre, font = "50")
    w.pack()
    def on_canvas_scroll(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units"),canvas.xview_scroll(-1 * (event.delta // 120), "units")
    canvas = Canvas(frame, bg="white")
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    #canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    scrollbar_x = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar.set)
    scrollbar_x.pack(side="bottom", fill="x")

    
    canvas.pack(side="left", fill="both", expand=True)

    # Configure canvas scrolling
    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<MouseWheel>", on_canvas_scroll)

    # Add some content to the canvas
    content_frame = Frame(canvas)
    canvas.create_window((0,0), window=content_frame, anchor="nw")
    temp=random.choice(Quotes)
    temp_list=[]
    temp_list.append(temp)
    for x in range(2):
        while len(temp)>40 and temp in temp_list :
            temp=random.choice(Quotes)
        temp_list.append(temp)
        text_label = Label(content_frame, text=temp, font=("Arial", 16), fg="blue", bg="yellow",wraplength=400)
        text_label.pack(pady=30)
        temp=random.choice(Quotes)
    def Back_func():
        frame.pack_forget()
        screen_2=screen2.create_screen2(root)
        screen_2.pack()
    b1_button = Button(frame, text ="Back",bg= '#80dfff', fg ="Black",command=Back_func)
    b1_button.pack( side = LEFT)

    print(Quotes)
    return frame
