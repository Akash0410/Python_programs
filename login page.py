from tkinter import *
from tkinter import messagebox


def login():
    username = entry1.get()
    password = entry2.get()

    if username == '' and password == '':
        messagebox.showerror('login', 'Incorrect Username or Password')
    elif username == 'admin' and password == '123':
        messagebox.showinfo('login', 'Login Successful')
        
        root.destroy()
        import bill
    
    else:
        messagebox.showerror('login', 'Incorrect Username or Password')

root = Tk()
root.configure(bg='cyan4')
root.geometry('500x400')

global entry1
global entry2



label1=Label(root, text ='LOGIN PAGE',bg='black', fg='cyan', font=('Areal',30))
label1.place(x=500,y=20)
label1.pack()

label2=Label(root, text ='USERNAME : ',bg='cyan4', fg='white', font=('Areal',20))
label2.place(x=380,y=150)


label3=Label(root, text ='PASSWORD : ',bg='cyan4', fg='white', font=('Areal',20))
label3.place(x=380,y=250)


entry1 =Entry(root, font=('Areal',15))
entry1.place(x=600, y=150)

entry2 =Entry(root, font=('Areal',15), show ='*')
entry2.place(x=600, y=250)

button = Button(root, text = 'LOGIN', bg='cyan3',font=('Areal', 20), bd=5,command=login)
button.place(x=500,y=300)



root.mainloop()