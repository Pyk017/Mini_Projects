from tkinter import *
from tkinter import messagebox
import random 

# Blue Yello Grey

root = Tk()
root.title("Secret Number")
root.iconbitmap("G:\Workspace\Python\Tkinter\Images\MyIcon.ico")
root.geometry("400x400")

user_name, user_age = None, None

def clickable():
    global submit
    global name_entry
    global age_entry
    global _name
    global _age

    user_name = name_entry.get()
    user_age = int(age_entry.get())
    
    # Information Message Box for creation of Secret Number.
    show_message = messagebox.showinfo("Getting Started", "Secret Number is Generated") 
    
    # For Disabling the start button
    submit.destroy()
    submit = Button(root, text="Start Game", width=10, bd=3, bg='#FFBCE3', relief='raised', state='disabled')
    submit.config(font=('Arial', 12, 'bold'))
    submit.grid(row=3, column=0, pady=10, padx=30)

    # reset = Button(root, text="Reset", width=10, bd=3, bg='#FFBCE3', relief='raised', state='active')
    # reset.config(font=('Arial', 12, 'bold'))
    # reset.grid(row=3, column=1, pady=10, padx=30)
    
    

    # Creating Take the Guess Label.
    take_guess = Label(root, text="Hi {}, Take the Guess!!".format(user_name), bg='#87ceeb')
    take_guess.config(font=("Arial", 15))
    take_guess.grid(row=4, column=0, columnspan=2, padx=30, pady=20)
    
    # def check(guessed_number):
    #     # global user_age
    #     global user_guess
    #     secret_number = random.randint(1, int(user_age))
    #     guessed_number = int(guessed_number)
    #     count = 1
    #     while True:
    #         if guessed_number < secret_number:
    #             messagebox.showerror("Alert", "Your Guessed Number is too low!\n Try a different one.")
    #             user_guess.delete(0, END)
    #         elif guessed_number > secret_number:
    #             messagebox.showerror("Alert", "Your Guessed Number is too high!\n Try a different one.")
    #             user_guess.delete(0, END)
    #         else:
    #             break
    #         count += 1
        
    #     print(count)
    
    # Creating Guess Box
    user_guess, guess_submit = None, None
    secret_number = random.randint(1, int(user_age))

    def create_guess_box():
        global user_guess
        global guess_submit
        user_guess = Entry(root, width=30, bg='yellow', bd=2, font=('Arial', 12, 'bold'))
        user_guess.focus_force()
        user_guess.grid(row=5, column=0, columnspan=2)

        guess_submit = Button(root, text="Guess!", width=10, bd=3, bg='#FFBCE3', relief='raised', state='active', command=lambda :check(user_guess.get()))
        guess_submit.config(font=('Arial', 12, 'bold'))
        guess_submit.grid(row=6, column=0, pady=10, padx=30)

    create_guess_box()

    def check(guessed_number):
        # global user_age
        global user_guess
        # global secret_number
        guessed_number = int(guessed_number)
        count = 1
        while True:
            if guessed_number < secret_number:
                messagebox.showerror("Alert", "Your Guessed Number is too low!\n Try a different one.")
                user_guess.delete(0, END)
                # create_guess_box()

            elif guessed_number > secret_number:
                messagebox.showerror("Alert", "Your Guessed Number is too high!\n Try a different one.")
                user_guess.delete(0, END)
                # create_guess_box()
            else:
                break
            create_guess_box()
            count += 1

            
        
        print(count)
    

    




welcome = Label(root, text="Hello! What is your Name and Age?", bg='#87ceeb')
welcome.config(font=("Arial", 15))
welcome.grid(row=0, column=0, columnspan=2, padx=30, pady=20)

name = Label(root, text='Name : ', bg='#87ceeb')
name.config(font=('Arial', 12, 'bold'))
name.grid(row=1, column=0)

name_entry = Entry(root, width=35, bg='yellow', bd=2, font=('Arial', 10, 'bold'))
name_entry.grid(row=1, column=1, sticky=W)

age = Label(root, text='Age : ', bg='#87ceeb')
age.config(font=('Arial', 12, 'bold'))
age.grid(row=2, column=0)

age_entry = Entry(root, width=10, bg='yellow', bd=2, font=('Arial', 10, 'bold'))
age_entry.grid(row=2, column=1, sticky=W)


submit = Button(root, text="Start Game", width=10, bd=3, bg='#FFBCE3', relief='raised', command=clickable)
submit.config(font=('Arial', 12, 'bold'))
submit.grid(row=3, column=0, pady=10, padx=30)

reset = Button(root, text="Reset", width=10, bd=3, bg='#FFBCE3', relief='raised')
reset.config(font=('Arial', 12, 'bold'))
reset.grid(row=3, column=1, pady=10, padx=30)



root.configure(bg='#87ceeb')
root.mainloop()