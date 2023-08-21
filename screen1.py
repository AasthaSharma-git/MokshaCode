from tkinter import * 
from PIL import Image,ImageTk


def create_screen1(root):

    frame=Frame(root)

    #w = Label(frame, text ='Welcome', font = "50")
    #w.pack()

    # Load the image using PhotoImage
    image = Image.open("collage.png")
    tk_image = ImageTk.PhotoImage(image)

    # Create a Label widget to display the image
    image_label = Label(frame, image=tk_image)
    image_label.image = tk_image  # Keep a reference to avoid garbage collection    
    image_label.pack()

    return frame