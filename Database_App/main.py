import tkinter as tk
from tkinter import *

# importing tkinter as themed-tkinter module
import tkinter.ttk as ttk

from tkinter import messagebox, scrolledtext, PhotoImage

# importing Database class from custom sqlite database file
from database_class import Database

# Regular Expression for checking the validity of Entered User Details.
import re

# Creating an instance of the Database Class
my_db = Database('bank_record')


root = tk.TK()

# Windows Dimensions
win.geometry('400x600')
win.minsize(400, 600)
win.maxsize(400, 600)

# Configuring the style for the themed-tkinter module
style = ttk.Style()

# Title for the Window
win.title('My Database App')


#---------------------- User Details ----------------------------

user_details = ''

#---------------------- Entry Widgets Variable --------------------

fname_var = tk.StringVar()  # variable for FirstName
lname_var = tk.StringVar()  # variable for lastName
uid_var = tk.StringVar()    # Variable for User-Id
uid = ''
pass_var = tk.StringVar()   # Variable for User-Password
pas = ''
email_var = tk.StringVar()  # Variable for Email
pinentry_var = tk.StringVar()   # Variable for the Password-verify Button
statusbtn_var = tk.StringVar() # Text Variable for status button

# ----------------------- Buttons --------------------------------

preview_btn = ''
register_btn = ''
signin_btn = ''
search_btn = ''
status = 'LOCKED'

# ------------------------ Path for Icons --------------------------

lock_img = 'icons/lock1.png'
unlock_img = 'icons/unlock1.png'

# ------------------------ PhotoImage Object for the Button ---------

image = lock_img
img = PhotoImage(file=image)

# ------------------------ Functions -------------------------------

def remove_all_Widgets():
    
    '''
        Description : Function to remove all the widgets from the window.
    '''
    for wid in win.winfo_children():
        wid.grid_remove()


def clear_pin_entries(des):

    '''
        Description : Function for clearing Pin entries on the window.
        Parameter : des -> Check which of the Pin entries to be cleared.
    '''

    global fname_var, lname_var, uid_var, pass_var, email_var

    if des == 'userpass':
        uid_var.set('')
        pass_var.set('')

    elif des == 'cred':
        fname_var.set('')
        lname_var.set('')
        email_var.set('')

    else:
        uid_var.set('')
        pass_var.set('')
        fname_var.set('')
        lname_var.set('')
        email_var.set('')


def create_table():

    '''
        Description : Function for Creating Table in the Database.
    '''    

    my_db.create_table(
        'account_details'
    )












