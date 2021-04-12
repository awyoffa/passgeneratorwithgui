from tkinter import *
import random
def view():
    passfile = Text(screen2, wrap=WORD, width=45, height=20)
    with open("pass.txt", 'r') as f:
        passfile.insert(INSERT, f.read())
    passfile.pack()
def delete2():
    screen3.destroy()
def deletel():
    screen2.destroy()
def delete():
    screen1.destroy()
def error():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("250x250")
    screen1.title("Warning")
    wrnng = Label(screen1, text="You need to fill all", bg="red")
    wrnng.pack()
    Button(screen1, text="OK", command=delete, width="4", height="2", bg="red").pack()
def succ():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("600x400")
    screen2.title("Done")
    wrnng = Label(screen2, text="Your passwords are sucsessfully genereated to pass.txt", bg="green")
    wrnng.pack()
    Button(screen2, text="OK", command=deletel, width="4", height="2", bg="green").pack()
    Button(screen2, text="View the file", command=view, width="10", height="2", bg="green").pack()
    for x in range(0, passsum_get):
        password = ""
        for x in range(0, passleng_get):
            password_char = random.choice(chars)
            password = password + password_char
        file = open("pass.txt", "a")
        file.write(password + " \n")
        file.close()
    passsum_entry.delete(0,END)
    passleng_entry.delete(0,END)

def generate():
    global passleng_get
    global passsum_get
    passleng_get = passleng.get()
    passsum_get = passsum.get()
    if passleng_get == 0:
        error()
    elif passsum_get ==0:
        error()
    else:
        succ()
def clear():
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("600x250")
    screen3.title("Deleted")
    wrnng = Label(screen3, text="You are deleted the generated passes", bg="red")
    wrnng.pack()
    Button(screen3, text="OK", command=delete2, width="4", height="2", bg="red").pack()
    file = open("pass.txt", "w")
    file.write("You succesfully deleted the generated passwords" )
    file.close()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@&+!"

screen = Tk()
screen.geometry("500x500")
screen.title("Password Generator")
heading = Label(text = "Password generator", bg = "grey", fg = "black", height = "2", width = "500")
heading.pack()

passleng_t = Label(text = "Password length: *")
passsum_t = Label(text = "How many passwords do you want to create? *")
passleng_t.place(x=10,y=40)
passsum_t.place(x=10, y= 100)



passleng = IntVar()
passsum = IntVar()


passleng_entry = Entry(textvariable = passleng)
passsum_entry = Entry(textvariable = passsum)
passleng_entry.place(x= 300, y= 40)
passsum_entry.place(x = 300, y = 100)



reg = Button(text = "Generate", bg = "green", width = "10", height = "2", comman = generate)
reg.place(x= 200, y = 200)

clr = Button(text = "Clear your pass.txt", bg = "green", width = "30", height = "2", comman = clear)
clr.place(x= 120, y = 400)

screen.mainloop()