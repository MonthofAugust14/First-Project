#this is my first program

import argparse
import tkinter as tk
import tkinter.messagebox as messagebox
import random
import winsound

parser = argparse.ArgumentParser(description="Change the amount of error windows.")
parser.add_argument('-w','--ew',type=int, default=40)
args = parser.parse_args()

window = tk.Tk()
window.geometry("1000x710")
window.title("My First GUI")
icon = tk.PhotoImage(file="3580-23831-8107.png")
window.iconphoto(True,icon)
window.config(background="#7c6b6b")

photo = tk.PhotoImage(file="braided red cutie.png")
photo = photo.subsample(2,2)

with open("phrases.txt") as mytxt:
    for line in mytxt:
        phrase = mytxt.readlines()

def submit():
    user_response = entry.get()
    if(user_response.upper() == "YES"):
        messagebox.showinfo(title='<3', message="I think so too!")
        entry.delete(0,tk.END)
    elif(user_response.upper() == "NO"):
        answer = messagebox.askquestion(title='Think Carefully.', message='Are you sure you want to have a wrong opinion?')
        if(answer == "yes"):
            wrong_answer()
        entry.delete(0,tk.END)

    else:
        messagebox.showwarning(title="Oops...", message="Please answer with yes or no.")
        entry.delete(0,tk.END)

def wrong_answer():
    winsound.Beep(440, 500)
    for _ in range(args.ew +1):
        errorMessage = tk.Toplevel()
        errorMessage.title("ERROR")
        errorMessage.geometry(f"+{int(random.randint(10,2000))}+{int(random.randint(10,2000))}")
        errorlabel = tk.Label(errorMessage, text= random.choice(phrase), font= ("",50,"bold"))
        errorlabel.pack()

label = tk.Label(window,text='This is a picture of an anime girl.',
              font=("",14,"italic"),
              fg="purple",
              bg="grey",
              bd=14,
              image=photo,
              padx=5,
              pady=5,
              compound="bottom")

label.pack()

label2 = tk.Label(window, text="Do you think she is cute? :3",
              font=("",14,"italic"),
              fg="purple",
              bg="grey",
              bd=14)

label2.pack()

entry = tk.Entry(window, font=(14))
entry.pack()

submit_button = tk.Button(window, text="Submit", command = submit)
submit_button.pack()

window.mainloop()