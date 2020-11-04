from tkinter import *
from tkinter import ttk

root = None

def main_screen():
    global root
    root = Tk()
    root.title("Crypt Arthmetic Solver by- Prakhar Kumar")
    root.geometry('500x400')
    root.iconbitmap("G:\Workspace\Python\Tkinter\Images\MyIcon.ico")
    root.configure(bg='#87ceeb')


def start():
    global root
    top = Toplevel(root)
    top.title("Crypt Arthmetic Solver")
    top.geometry('1000x500')
    top.iconbitmap("G:\Workspace\Python\Tkinter\Images\MyIcon.ico")
    top.configure(bg='#87ceeb')

       

    top.mainloop()


main_screen()

welcome_label = Label(root, text='Welcome to Crypt Arthmetic Solver', fg='#800000', bg='#87ceeb', font=('Helvetica', 18, 'bold'))
welcome_label.grid(row=0, column=0, padx='40', pady=('120', 0), columnspan=3)


start_button = Button(root, text='Start', bg='#ffc0cb', fg='#800000', height='2', width='15', command=start)
start_button.grid(row=1, column=0, padx=(50, 0))

exit_button = Button(root, text='Exit', bg='#ffc0cb', fg='#800000', height='2', width='15', command=quit)
exit_button.grid(row=1, column=1, pady='20')



root.mainloop()
