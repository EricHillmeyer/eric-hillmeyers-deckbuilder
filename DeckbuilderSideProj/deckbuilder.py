# Deckbuilder
# Programmer: Eric Hillmeyer
# Email: ehillmeyer1@cnm.edu
# Purpose: Create a database to create a decklist for a user and output it to them

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, END, INSERT
import sqlite3

#Event functions and database initialization
def DeckCreator():
    conn = sqlite3.connect('deck.db')
    c = conn.cursor()
    deck_name = deck_name_entry.get()
    c.execute(f'CREATE TABLE IF NOT EXISTS {deck_name} (Card_Name, Num_In_Deck)')
    conn.commit()
    conn.close()
    return deck_name

# Load what is already under the chosen deck
def LoadOuput():
    try:
        conn = sqlite3.connect('deck.db')
        c = conn.cursor()
        deck = DeckCreator()
        c.execute(f'INSERT INTO {deck} (Card_Name, Num_In_Deck) VALUES (?,?)', (user_card.get(), num_in_deck.get()))
        sql_cmd = f'SELECT * FROM {deck}'
        c.execute(sql_cmd)
        data = c.fetchall()
        conn.commit()
        conn.close()

        formatted_data = ''

        format = "%s %s \n"
        for line in data:
            formatted_data = formatted_data.__add__(format%line)

        output.delete("1.0", END)
        output.insert(INSERT, formatted_data)

    except:
        output.insert(INSERT, "No deck found!")

# Main
deckbuilder_gui = tk.Tk()
deckbuilder_gui.title("Eric Hillmeyer's Deck Editor")
deckbuilder_gui.geometry("900x600")

# Textbox to name the user's deck
tk.Label(text = "Deck Name:").pack(anchor = tk.W, padx = 5)
deck_name_entry = tk.StringVar()
curr_deck = tk.Entry(deckbuilder_gui, textvariable = deck_name_entry)
curr_deck.pack(anchor = tk.W, padx = 5)

# Button to open deck
open_deck = tk.Button(text = 'Open Deck', command = DeckCreator)
open_deck.pack(anchor = tk.W, padx = 5)

# Textbox to add a card name to the deck
tk.Label(text = "Enter a card:").pack(anchor = tk.W, padx = 5)
card = tk.StringVar()
user_card = tk.Entry(deckbuilder_gui, textvariable = card)
user_card.pack(anchor = tk.W, padx = 5)

# Textbox to add a number of cards to the deck
tk.Label(text = "Number wanted in deck:").pack(anchor = tk.W, padx = 5)
num = tk.StringVar()
num_in_deck = tk.Entry(deckbuilder_gui, textvariable = num)
num_in_deck.pack(anchor = tk.W, padx = 5)

# Button to add a card to the deck
add_to_deck = tk.Button(text = 'Add to Deck', command = LoadOuput)
add_to_deck.pack(anchor = tk.W, padx = 5)

# Showing the name of the deck
deck_label = tk.Label(text = "Deck Contents")
deck_label.pack(anchor = tk.N)

# Showing user the result
output = scrolledtext.ScrolledText()
output.pack(anchor = tk.N, expand = True, fill = "y")

tk.mainloop()

# StackOverflow Credits:
# GUI code: https://stackoverflow.com/questions/53491341/how-to-use-tkinter-with-sqlite-in-python

# Changes made:
# Took the textvariable variable and used it. This is something I had not learned in the class

# To Dos:

# An actual database that takes a user's choice and catches to see if they actually chose an MTG card
# A tally of the total cards the user has in their deck
# A check to see if the number of cards entered in is greater than the amount they can have
# Functionality for rules on different game types implemented to be caught and handled through the code
# A database of databases to create and store multiple decks
# A delete button to delete a specific card
# Better formatting in the scrolltext window