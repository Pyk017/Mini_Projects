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


root = tk.Tk()

# rootdows Dimensions
root.geometry('400x600')
root.minsize(400, 600)
root.maxsize(400, 600)

# Configuring the style for the themed-tkinter module
style = ttk.Style()

# Title for the rootdow
root.title('My Database App')


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
        Description : Function to remove all the widgets from the rootdow.
    '''
    for wid in root.rootfo_children():
        wid.grid_remove()


def clear_pin_entries(des):

    '''
        Description : Function for clearing Pin entries on the rootdow.
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

    my_db.create_table('account_details',
                        'user_fname text',
                        'user_lname text',
                        'user_id text',
                        'user_pass text',
                        'user_email text'
                    )


def check_validity(string, typ):

    '''
        Parameters:
            string = String to be validated.
            typ = which kind of string is it? i.e. (Password, Email)
    
        Description :
            To check the Validity of the passed string
    '''

    global pass_var, email_var

    if typ == 'email':
        # Compiling The Regular expression for checking the email pattern
        email_pattern = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

        # Now Matching the provided pattern
        pattern_match = email_pattern.match(string)

        if not pattern_match:
            messagebox.showwarning("Warning", "Email Incorrect! sample email : abc@example.com")
            email_var.set('')
            return False

        return True

    elif typ == 'password':

        # Password restriction will be -> First Character should be Capital and password should contain Digits and special characters.
        pass_pattern = re.compile(r"[A-Z]+[a-zA-Z0-9!@#$%^&*()_+]+[!@#$%^&*()_+]+[a-zA-Z0-9]+")

        pattern_match = pass_pattern.match(string)
        
        if not pattern_match:
            messagebox.showwarning('Warning', 'The Required Criteria for the password doesn\'t Match!!\
                                    1. First Character should be capital.\
                                    2. The password should contains atleast one special character and digits.')

            pass_var.set("")
            return False

        return True



def add_user(fname, lname, u_id, u_pass, email):

    '''
        Parameters:
            fname = First Name of the User
            lname = Last Name of the User
            u_id = The ID of the user
            u_pass = the Password of the User.
            email = The email of the user
        
        Description:
            Function to add a user details to the database.
    '''

    global register_btn

    flag = True

    # Making sure no field will be empty.
    if fname == '' and lname == '' and u_id == '' and u_pass == '' and email == '':
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!')

    else:
        # Retrieving the user_id and user_pass of all the users and checking if the user exists already.
        check = my_db.select_from_db('account_details', ['user_id', 'user_pass'])

        # Checking the validity of User email and password.
        pass_isValid = check_validity(u_pass, 'password')
        email_isValid = check_validity(email, 'email')

        if not pass_isValid or not email_isValid:
            messagebox.showerror("Error!", "Registration Failed! Please Try Again.")
            flag = False

        for entry in check:
            # If user-id and user-pass is present alredy in the database then issue a warning for that.
            if u_id and u_pass in entry:
                flag = False
                messagebox.showwarning("Field Error!", "Please use Another Username and Password!")
                # Clearing the entries or user-id and password fields
                clear_pin_entries('userpass')
                break

        if flag:
            # Inserting the new user details into the database.
            my_db.insert_into_db('account_details', fname, lname, u_id, u_pass, email)
            # Clearing the Entries except the User_id and Password fields.
            clear_pin_entries('cred')
            #Issuing process successful info.
            messagebox.shorootfo('User Accounts', 'User has been added Successfully!')


def update_user(u_fname, u_lname, u_id, u_pass, email):
    '''
        Description : Function to update the details of a user to the database.
    '''

    flag = True

    global user_details

    # Checking if the entries are valid or not and updating the respective info, to the user's database.
    if u_fname != '' and u_lname != '' and email != '':
        my_db.update_db('account details', {'user_fname': u_fname, 'user_lname': u_lname, 'user_email': email}, user_id=user_details[2], user_pass=user_details[3])

    elif u_fname != '' and u_lname != '':
        my_db.update_db('account details', {'user_fname': u_fname, 'user_lname': u_lname}, user_id=user_details[2], user_pass=user_details[3])

    elif email != '':
        my_db.update_db('account details', {'user_email': email}, user_id=user_details[2], user_pass=user_details[3])

    else:
        flag = False

    if flag:
        messagebox.shorootfo('Success', 'The Details have been updated successfully!')
        # Calling the query_db function to fetch and display the updated info via the function name provided.
        query_db(u_id, u_pass, 'extract_info')

    else:
        messagebox.showerror('Error', 'Some error occurred during the process! Please Try Again!')


def validate_user(u_id, u_pass):
    '''
        Description :
            Function to validate if the user exists or not.
    '''

    global search_btn

    if u_id != '' and u_pass != '':
        # Retrieving the details of all the users and checking if it exists.
        user = my_db.search_from_db('account_details', user_id=u_id, user_pass=u_pass)
        if user:
            print("User Exists!!")
            remove_all_Widgets()
            create_user_screen(user)
        else:
            print("User doesnot Exists!")
            clear_pin_entries('')
            messagebox.showerror("Login Error!!", 'Sorry! The user doesnot exists!')
    
    else:
        messagebox.showerror('Error', 'Blank Fields are not Allowed!')


def query_db(u_id, u_pass, call):
    
    '''
        Description : Function to see the Contents of the Database and debug whenever necessary.
    '''

    user = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)

    if call == 'extract_info':
        extract_info(user)

    
def search(u_fname, u_id):
    
    '''
        Description : Function to search whether the User exists or not.
    '''

    # Creating a list of the inputs in order to get desired ouput 
    lst = [['u_fname', u_fname], ['u_id', u_id]]

    # Creating which of the inputs are to be inserted in the Query.
    lst = [i for i in lst if i[1] != '']

    # Creating if the list is not empty.
    if lst != []:
        # If the length of the list is 1 then there exists only one parameter in the list.
        if len(lst) == 1:
            if lst[0][1] == 'u_fname':
                result = my_db.select_from_db('account_details', user_fname=u_fname)
            else:
                result = my_db.select_from_db('account_details', user_id=u_id)

        else:
            # else there are both parameters inputed by the user.
            result = my_db.select_from_db('account_details', user_id=u_id, user_fname=u_fname)

    # Passing the values along with the message to be displayed in the output rootdow.
    output_root(result, 'Search Results :')


def extract_info(user, reset=False):
    
    '''
        Description : Function to extract all different fields from the specific row of a table.
    '''

    global fname_var, lname_var, uid_var, pass_var, email_var, user_details

    if not reset:
        user_details = list(user[0])

    fname_var.set('')
    lname_var.set('')
    uid_var.set('')
    pass_var.set('')
    email_var.set('')


def output_root(string, msg):
    
    '''
        Description : Function to display the provided value and message in the output rootdows.
    '''

    text_widget_2 = tk.scrolledtext.ScrolledText(root, width=12, height=6)

    text_widget_2.insert('insert' , f'------{img}--------' + '\n')
    text_widget_2.insert('insert' , f'=======================' + '\n')

    for text in string:
        for txt in text:
            text_widget_2.insert('insert', txt + '\n')
            text_widget_2.insert('insert', '------------------------' + '\n')

        text.widget_2.insert('insert', '=================' + '\n')
    
    text_widget_2.grid(row=9, columnspan=2, padx=10, sticky='news')
    text_widget_2.config(state='disabled')


def shortcuts(param):
    '''
        Description : Function to handle the shortcuts provided in the view.
    '''

    if param == 'quit':
        root.destroy()


def pass_verify(u_pass):

    '''
        Description : Function to verify if the user is Authorized or not to make changes to the record.
    '''

    global top, status, pinentry_var

    # Checking whether the status is LOCKED and UNLOCKED.
    if status == 'LOCKED':
        # If Locked then, create a toplevel rootdow on the root rootdows

        top = tk.Toplevel(root)
        #assigning the rootdow a title.
        top.title('Verify!')

        # Configuring The Style of the Buttons.
        style.configure(SUNKABLE_BUTTON, foreground='green')

        # Setting the Geometry of the rootdow.
        top.geometry('220x100')
        top.minsize(220, 100)
        top.maxsize(220, 100)

        lb1 = tk.Label(top, text="Enter the password for the User : ")
        lb1.grid(row=0, columnspan=4, padx=20, sticky='news')

        u_p = tk.Entry(top, textvariable=pinentry_var)
        u_p.config(show='*')
        u_p.grid(row=1, columnspan=4, padx=20, sticky='news', pady=10)

        u_p.focus_set()

        btn = ttk.Button(top, text='Verify', style=SUNKABLE_BUTTON)
        btn.bind("<Button-1> ", lambda x: btn_status(u_p.get(), u_pass))
        btn.grid(row=2, column=1, columnspan=2, sticky='news', pady=10)

        top.mainloop()
    
    else:
        # If status is unlocked then directly call btn_status function.
        btn_status()


def btn_status(t_pass=None, u_pass=None):
    '''
        Parameter : 
            t_pass = the pass entered by the user in verification process.
            u_pass = the user_pass of the user to verify during state change.
        
        Description : Function to check whether the button is in LOCKED state or not.
    '''

    global statusbtn_var, fname, lname, email, status, top, pinentry_var, img, status_btn, user_details

    #  checking if the password  exists or not.
    if t_pass and u_pass:
        if t_pass ==  u_pass:
            # If the password match then, 
                # Create  a PhotoImage Object to  change the Icon of the button.
            img = PhotoImage(file=unlock_img)
            # Setting that icon to the Button
            status_btn.config(image=img)
            # Clearing a pin ENtry.
            pinetry_var.set('')
            # Destroying the Pin Verification rootdow
            top.destroy()
            # Changing the button text to UNLOCKED.
            status_btn.set('UNLOCKED')
            # making the entries editable
            fname.config(state=NORMAL)
            lname.config(state=NORMAL)
            email.config(state=NORMAL)
            # Setting the Global Variable to UNLOCKED.
            status = "UNLOCKED"

        else:
            # else display the error message and clear the pin entry.
            messagebox.showerror("Authentication Error!", "Please Try Again!")
            pinentry_var.set('')
        
    else:
        # If the status is UNLOCKED then set the buttton's text to LOCKED.
        statusbtn_var.set('LOCKED')
        # Creating a PhotoImage Object to change the Icon of the Button.
        img = PhotoImage(file=lock_img)
        # Setting that icon to the button 
        status_btn.config(image=img)
        # Resetting the original values.
        extract_info(user_details, True)
        #Making the entries non editable.
        fname.config(state=DISABLED)
        lname.config(state=DISABLED)
        email.config(state=DISABLED)
        # Setting the Global Variable to Locked 
        status = "LOCKED"


def logout():
    '''
        Description : Function to logout of the Current User's Account.
    '''

    clear_pin_entries()
    remove_all_Widgets()
    create_login_screen()


def show_db():
    '''
        Description : Function to display all the entries present in the database.
    '''

    # Acquiring all the entries from the Database.
    lst = my_db.select_from_db('account_details')

    output_root(lst, "All Database Entries.")


# ----------------------------------- Key Shortcuts ------------------

root.bind("<Control-q>", lambda x: shortcuts("quit"))


# Always leave this method enabled as it creates a connection and cursor objects to work with the Database.
my_db.create_db()

# Methods Below can be enabled or disabled depending on their usage. 
# create_table()

# Method to Remove a Secific Entity from the Database.
# my_db.remove_from_db('account_details', False, user_id=1716410101, user_pass=1234)

# Method to Delete the Table form the Database.
# my_db.drop_table('account_details')

# query_db()


# -------------------------------- User Interface Functions -----------------------

def create_login_screen():
    
    '''
        Description : Function to create the login screen
    '''

    global uid, pas

    # Text-Widget for displaying the Info and Result.
    text_widget = tk.scrolledtext.ScrolledText(root, width=12, height=6)  # Text Widget Variable
    text_widget_1 = tk.scrolledtext.ScrolledText(root, width=12, height=6) # Text Widget Variable

    # The title of the rootdow
    lb1 = tk.Label(root, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=2, ipadx=60, ipady=20)


    # ------------------ Form Labels and Inputs ---------------------

    lb2 = tk.Label(root, text="FIRST NAME : ")
    lb2.config(font=("Source Code Pro", 10))
    lb2.grid(row=1, column=0, ipadx=60, ipady=20, sticky='e')

    fname = tk.Entry(root, textvariable=fname_var)
    fname.grid(row=1, column=1, pady=2, ipady=70, sticky='nws')

    fname.focus_set()

    lb3 = tk.Label(root, text="LAST NAME : ")
    lb3.config(font=("Source Code Pro", 10))
    lb3.grid(row=2, column=0, ipadx=60, ipady=20, sticky='e')

    lname = tk.Entry(root, textvariable=lname_var)
    lname.grid(row=2, column=1, pady=2, ipady=70, sticky='nws')

    lb4 = tk.Label(root, text="USER-ID : ")
    lb4.config(font=("Source Code Pro", 10))
    lb4.grid(row=3, column=0, ipadx=60, ipady=20, sticky='e')

    uid = tk.Entry(root, textvariable=uid_var)
    uid.grid(row=3, column=1, pady=2, ipady=70, sticky='nws')

    lb5 = tk.Label(root, text="PASSWORD : ")
    lb5.config(font=("Source Code Pro", 10))
    lb5.grid(row=4, column=0, ipadx=60, ipady=20, sticky='e')

    pas = tk.Entry(root, textvariable=pass_var)
    pas.config(show='*')
    pas.grid(row=4, column=1, pady=2, ipady=70, sticky='nws')

    lb6 = tk.Label(root, text="EMAIL : ")
    lb6.config(font=("Source Code Pro", 10))
    lb6.grid(row=5, column=0, ipadx=60, ipady=20, sticky='e')

    email = tk.Entry(root, textvariable=email_var)
    email.grid(row=5, column=1, pady=2, ipady=70, sticky='nws')

    # ----------------------------------------------------------------------


    # ------------------------ Information Text Block -----------------------

    text_widget.insert('insert',"USER-ID and PASSWORD are unique for everyone!!\
                                        \nFor SignIn Only USER-ID and PASSWORD Fields are required!!\
                                To Search Somebody Input his USER-ID and PASSWORD.")

    text_widget.grid(row=6, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state='disabled')

    # ----------------------------------- Buttons ---------------------------------

    frame_btns = tk.Frame(root)
    frame_btns.grid(row=7, columnspan=3)

    style.configure(SUNKABLE_BUTTON, foreground='green')

    register_btn = ttk.Button(frame_btns, text='Register', style=SUNKABLE_BUTTON)
    register_btn.bind("<Button-1>", lambda x: add_user(fname.get(), lname.get(), uid.get(), pas.get(), email.get()))
    register_btn.grid(row=0, column=0)

    signin_btn = ttk.Button(frame.btns, text='SignIn', style=SUNKABLE_BUTTON)
    signin_btn.bind("<Button-1>", lambda x: validate_user(uid.get(), pas.get()))
    signin_btn.grid(row=0, column=1)

    search_btn = ttk.Button(frame.btns, text='Search', style=SUNKABLE_BUTTON)
    search_btn.bind("<Button-1>", lambda x: search(uid.get(), pas.get()))
    search_btn.grid(row=0, column=2)

    clear_btn = ttk.Button(frame.btns, text='Clear', style=SUNKABLE_BUTTON)
    clear_btn.bind("<Button-1>", lambda x: clear_pin_entries(''))
    clear_btn.grid(row=0, column=3)

    # ---------------------- The Output Text Block -----------------------------

    lb7 = Label(root, text='OUTPUT : ')
    lb7.grid(row=8, columnspan=2, pady=20)

    text_widget_1.insert('insert', 'THIS IS THE OUTPUT rootDOW')
    text_widget_1.grid(row=9, columnspan=2, padx=10, sticky='news')
    text_widget_1.config(state='disabled')

    # some helpful information.

    lb8 = Label(root, text="Press 'Ctrl + q' to Quit the APP.")
    lb8.grid(row=10, columnspan=2, pady=20)


def create_user_screen(user):
    
    '''
        Parameter: 
            user = details of the user whose account is being accessed.
        
        Description : Function for the user to provide functionality of Update, View and Delete Account.
    '''

    global uid, pas, statusbtn_var, fname, lname, email, status, status_btn

    # Text-Widgets for Displaying the Info and Results.
    text_widget = tk.scrolledtext.ScrolledText(root, width=12, height=6)     # Text-Widget Variable
    text_widget_1 = tk.scrolledtext.ScrolledText(root, width=12, height=6)   # Another Text-Widget Variable


    lb1 = tk.Label(root, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=4, ipadx=60, ipady=20)

    lb2 = tk.Label(root, text="------------ Your Details -----------")
    lb2.grid(row=1, columnspan=4, sticky="news")

    extract_info(user)

      # ------------- Form Labels and Inputs --------------

    lb2 = tk.Label(root, text="FIRSTNAME : ")
    lb2.config(font=("Source Code Pro", 10))
    lb2.grid(row=2, column=0, sticky="e")

    fname = tk.Entry(root, textvariable=fname_var, state=DISABLED)
    fname.grid(row=2, column=1, pady=2, ipadx=70, sticky="nws")

    lb3 = tk.Label(root, text="LASTNAME : ")
    lb3.config(font=("Source Code Pro", 10))
    lb3.grid(row=3, column=0, sticky="e")

    lname = tk.Entry(root, textvariable=lname_var, state=DISABLED)
    lname.grid(row=3, column=1, pady=2, ipadx=70, sticky="nws")

    lb4 = tk.Label(root, text="USER-ID : ")
    lb4.config(font=("Source Code Pro", 10))
    lb4.grid(row=4, column=0, sticky="e")

    uid = tk.Entry(root, textvariable=uid_var, state=DISABLED)
    uid.grid(row=4, column=1, pady=2, ipadx=70, sticky="nws")

    lb5 = tk.Label(root, text="PASSWORD : ")
    lb5.config(font=("Source Code Pro", 10))
    lb5.grid(row=5, column=0, sticky="e")

    pas = tk.Entry(root, textvariable=pas_var, state=DISABLED)
    pas.config(show='*')
    pas.grid(row=5, column=1, pady=2, ipadx=70, sticky="nws")

    lb6 = tk.Label(root, text="EMAIL : ")
    lb6.config(font=("Source Code Pro", 10))
    lb6.grid(row=6, column=0, sticky="e")

    email = tk.Entry(root, textvariable=email_var, state=DISABLED)
    email.grid(row=6, column=1, pady=2, ipadx=70, sticky="nws")

    # --------------------------------------------------------

    # ----------------- Information Text Block ---------------
    text_widget.insert('insert', "To Make Changes to any of the Input Fields(Except USER-ID and PASSWORD)just Press the LOCKED button and then type in the new Entries and then Press UPDATE button,and hit UNLOCKED Button to LOCK again!!\
         If you LOGOUT without UPDATING the changes made then your Progress will be LOST!!")
    text_widget.grid(row=7, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state="disabled")

    # ----------------- Buttons --------------------

    frame_btns = tk.Frame(root)
    frame_btns.grid(row=8, columnspan=3, ipady=10)

    style.configure(SUNKABLE_BUTTON, foreground='green')

    statusbtn_var.set("LOCKED")

    status_btn = ttk.Button(frame_btns, textvariable=statusbtn_var, style=SUNKABLE_BUTTON, compound="left")
    status_btn.config(image=img)
    status_btn.bind("<Button-1>", lambda x: pass_verify(pas.get()))
    status_btn.grid(row=0, column=0)

    update_btn = ttk.Button(frame_btns, text="Update", style=SUNKABLE_BUTTON)
    update_btn.bind("<Button-1>", lambda x: update_user(fname.get(), lname.get(), uid.get(), pas.get(), email.get()))
    update_btn.grid(row=0, column=1)

    db_btn = ttk.Button(frame_btns, text="ShowDB", style=SUNKABLE_BUTTON)
    db_btn.bind("<Button-1>", lambda x: show_db())
    db_btn.grid(row=0, column=2)

    logout_btn = ttk.Button(frame_btns, text="Logout", style=SUNKABLE_BUTTON)
    logout_btn.bind("<Button-1>", lambda x: logout())
    logout_btn.grid(row=0, column=3)

    # # ----------------- Information Text Block ---------------
    # text_widget_1.insert('insert', "")
    # text_widget_1.grid(row=7, columnspan=2, padx=10, pady=20, sticky="news")
    # text_widget_1.config(state="disabled")



create_login_screen()
root.mainloop()


