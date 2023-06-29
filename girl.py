from tkinter import *
from tkinter import messagebox
import random
from random import randint
import winsound

response_list = ["You are Wrong!","I can't believe you!","That makes me sad...",">:^(","Are you stupid?","it's not like I like you or anything...","T-Tch! S-Shut up!"]

window = Tk()
window.geometry("1000x710")
window.title("My First GUI")
icon = PhotoImage(file="3580-23831-8107.png")
window.iconphoto(True,icon)
window.config(background="#7c6b6b")

photo = PhotoImage(file="braided red cutie.png")
photo = photo.subsample(2,2)

def submit():
    user_response = entry.get()
    if(user_response.upper() == "YES"):
        messagebox.showinfo(title='<3', message="I think so too!")
        entry.delete(0,END)
    elif(user_response.upper() == "NO"):
        answer = messagebox.askquestion(title='Think Carefully.', message='Are you sure you want to have a wrong opinion?')
        if(answer == "yes"):
            wrong_answer()
            entry.delete(0,END)
        else:
            pass
        entry.delete(0,END)
    else:
        messagebox.showwarning(title="Oops...", message="Please answer with yes or no.")
        entry.delete(0,END)

def wrong_answer():
    winsound.Beep(440, 500)
    for i in range(100):
        errorMessage = Toplevel()
        errorMessage.title("ERROR")
        errorMessage.geometry(f"+{int(randint(10,2000))}+{int(randint(10,2000))}")
        errorlabel = Label(errorMessage, text= random.choice(response_list), font= ("",50,"bold"))
        errorlabel.pack()

label = Label(window,text='This is a picture of an anime girl.',
              font=("",14,"italic"),
              fg="purple",
              bg="grey",
              bd=14,
              image=photo,
              padx=5,
              pady=5,
              compound="bottom")

label.pack()

label2 = Label(window, text="Do you think she is cute? :3",
              font=("",14,"italic"),
              fg="purple",
              bg="grey",
              bd=14)

label2.pack()

entry = Entry(window, font=(14))
entry.pack()

submit_button = Button(window, text="Submit", command = submit)
submit_button.pack()

window.mainloop()