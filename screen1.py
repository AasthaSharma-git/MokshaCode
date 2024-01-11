import tkinter as tk
from tkinter import ttk, messagebox
import requests
import tkinter as tk
import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
import pandas as pd
import random


def fetch_quote(category=None, author=None):
    # result_text.config(text="Please Wait...")

    chunk_number = 1
    while True:

        print(chunk_number)
        url = f"https://aasthasharma.pythonanywhere.com/quotes?chunk_number={chunk_number}&"

        if category:
            url += f"category={category}"
        elif author:
            url += f"&author={author}"
        print(url)

        response = requests.get(url)
        if response.status_code == 200:
            quote_data = response.json()
            print(len(quote_data))

            if len(quote_data) < 5:

                chunk_number += 1
                continue
            else:

                all_quotes = []

                for quote in quote_data:
                    all_quotes.append(quote.get('quote'))

                idxs = []

                for i in range(5):

                    idxs.append(random.randint(0, len(all_quotes)))

                quotes = []

                for i in idxs:
                    quotes.append(all_quotes[i])

                return quotes

                

        # result_text.config(text=quote)
        else:
            return 'Error fetching quote'
            
           


class screen_1():
    def __init__(self, app, genre, welcome_frame):
        self.app = app
        self.welcome_frame = welcome_frame
        self.screen1_frame = ctk.CTkFrame(
            master=app, border_width=2, corner_radius=10, width=650, height=550)
        self.screen1_frame.place(x=30, y=30)
        result_text = tk.Label(master=self.screen1_frame,
                               text=genre, wraplength=400)
        result_text.place(x=10, y=10)
        Quotes = []
        b1_button = ctk.CTkButton(
            self.screen1_frame, text="Back", command=self.Back_func)
        b1_button.place(x=500, y=10)
        
        
        posy=20
        quotes=fetch_quote(genre)
        for quote in quotes:
            text_label = ctk.CTkLabel(
                self.screen1_frame, text=quote, font=("Arial", 16), wraplength=400)
            text_label.place(x=30, y=posy)
            posy = posy+50

    def Back_func(self):
        self.screen1_frame.place_forget()
        self.welcome_frame.place(x=30, y=30)
