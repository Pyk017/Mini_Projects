from tkinter import *
from tkinter import messagebox
import random 

# Creating Window.
root = Tk()
root.title("Secret Number")
root.iconbitmap("G:\Workspace\Python\Tkinter\Images\MyIcon.ico")
root.geometry("400x400")

# Some global scope variables
user_name, user_age = None, None
ls = list()
take_guess = None
user_guess = None
guess_submit = None
exit_btn = None
result_label = None

# Main function started.
def clickable():
    global submit
    global name_entry
    global age_entry
    global _name
    global _age

    global take_guess
    global user_guess
    global guess_submit
    global exit_btn
    global result_label

    # Get the information of User's Name and Age.
    user_name = name_entry.get()
    user_age = int(age_entry.get())
    
    # Information Message Box for creation of Secret Number.
    show_message = messagebox.showinfo("Getting Started", "Secret Number is Generated between 1 and your age!") 
    
    # Function after user hit reset button to reset all fields.
    def resetting():
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        user_guess.delete(0, END)
        guess_submit.config(state='disabled')
        result_label.destroy()


    # For Disabling the start button
    submit.destroy()
    submit = Button(root, text="Start Game", width=10, bd=3, bg='#FFBCE3', relief='raised', state='disabled')
    submit.config(font=('Arial', 12, 'bold'))
    submit.grid(row=3, column=0, pady=10, padx=30)

    reset = Button(root, text="Reset", width=10, bd=3, bg='#FFBCE3', relief='raised', command=resetting)
    reset.config(font=('Arial', 12, 'bold'))
    reset.grid(row=3, column=1, pady=10, padx=30)
    
    # Creating Take the Guess Label.
    take_guess = Label(root, text="Hi {}, Take the Guess!!".format(user_name), bg='#87ceeb')
    take_guess.config(font=("Arial", 15))
    take_guess.grid(row=4, column=0, columnspan=2, padx=30, pady=20)
    

    user_guess, guess_submit = None, None
    # Secret Number Creation
    secret_number = random.randint(1, int(user_age))

    # Function to show result label.
    def show_result(res):
        global result_label
        build_result = '{} ' * len(res)
        bs = build_result.format(*res)
        result_label = Label(root, text="Your Guessing Score is :- {} \n Your Guess Sequence is :- {}".format(len(res), bs), bg='#87ceeb')
        result_label.config(font=("Arial", 12, 'bold'))
        result_label.grid(row=7, column=0, columnspan=2)

        guess_submit = Button(root, text="Guess!", width=10, bd=3, bg='#FFBCE3', relief='raised', state='disabled', command=lambda :check(user_guess.get()))
        guess_submit.config(font=('Arial', 12, 'bold'))
        guess_submit.grid(row=6, column=0, pady=10, padx=30)

    # Function to check for the correct guess otherwise alert messagebox displays.
    def check(guessed_number):
        global user_guess

        try:
            guessed_number = int(guessed_number)
            if guessed_number < secret_number:
                messagebox.showinfo("Alert", "Your Guessed Number is too low!\n Try a different one.")
                user_guess.delete(0, END)
            elif guessed_number > secret_number:
                messagebox.showinfo("Alert", "Your Guessed Number is too high!\n Try a different one.")
            else:
                messagebox.showinfo("Information", "Congratulations! You have guessed right")
                ls.append(guessed_number)
                show_result(ls) 

        except ValueError:
            messagebox.showerror("Alert", "Please Enter Something in Guess Box.")

        ls.append(guessed_number)
        create_guess_box()
    
    
    # Function to create a guess box, submit button and exit button.
    def create_guess_box():
        global user_guess
        global guess_submit
        global exit_btn
        user_guess = Entry(root, width=30, bg='yellow', bd=2, font=('Arial', 12, 'bold'))
        user_guess.focus_force()
        user_guess.grid(row=5, column=0, columnspan=2)
        
        guess_submit = Button(root, text="Guess!", width=10, bd=3, bg='#FFBCE3', relief='raised', state='active', command=lambda :check(user_guess.get()))
        guess_submit.config(font=('Arial', 12, 'bold'))
        guess_submit.grid(row=6, column=0, pady=10, padx=30)
        
        exit_btn = Button(root, text="Exit!", width=10, bd=3, bg='#FFBCE3', relief='raised', state='active', command=quit)
        exit_btn.config(font=('Arial', 12, 'bold'))
        exit_btn.grid(row=6, column=1, pady=10, padx=30)

    create_guess_box()


# Welcome Label
welcome = Label(root, text="Hello! What is your Name and Age?", bg='#87ceeb')
welcome.config(font=("Arial", 15))
welcome.grid(row=0, column=0, columnspan=2, padx=30, pady=20)

# Name Label
name = Label(root, text='Name : ', bg='#87ceeb')
name.config(font=('Arial', 12, 'bold'))
name.grid(row=1, column=0)

# Name entry box
name_entry = Entry(root, width=30, bg='yellow', bd=2, font=('Arial', 10, 'bold'))
name_entry.grid(row=1, column=1, sticky=W)

# Age Label
age = Label(root, text='Age : ', bg='#87ceeb')
age.config(font=('Arial', 12, 'bold'))
age.grid(row=2, column=0)

# Age entry box
age_entry = Entry(root, width=10, bg='yellow', bd=2, font=('Arial', 10, 'bold'))
age_entry.grid(row=2, column=1, sticky=W)

# Submit button to submit the information
submit = Button(root, text="Start Game", width=10, bd=3, bg='#FFBCE3', relief='raised', command=clickable)
submit.config(font=('Arial', 12, 'bold'))
submit.grid(row=3, column=0, pady=10, padx=30)

reset = Button(root, text="Reset", width=10, bd=3, bg='#FFBCE3', relief='raised')
reset.config(font=('Arial', 12, 'bold'))
reset.grid(row=3, column=1, pady=10, padx=30)


root.configure(bg='#87ceeb')
root.mainloop()
