#this is my first program
import os
import argparse
import tkinter as tk
import tkinter.messagebox as messagebox
import random
import winsound

def window_center(width=1000, height=710):
    sw = os.environ.get('SCREEN_WIDTH', screen_width)
    sh = os.environ.get('SCREEN_HEIGHT', screen_height)
    print(sw)
    print(os.environ.get('SCREEN_WIDTH'))
    x = (int(sw)/2) - (width/2)
    y = (int(sh)/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

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
    for _ in range(args.error_windows +1):
        errorMessage = tk.Toplevel()
        errorMessage.title("ERROR")
        errorMessage.geometry(f"+{int(random.randint(0,screen_width))}+{int(random.randint(0,screen_height))}")
        errorlabel = tk.Label(errorMessage, text= random.choice(phrase_list), font= ("",50,"bold"))
        errorlabel.pack()

parser = argparse.ArgumentParser(description="Change the amount of error windows.")
parser.add_argument('-ew','--error_windows',type=int, default=40)
args = parser.parse_args()

window = tk.Tk()
window.withdraw()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.deiconify()
window.geometry(window_center())
window.title("My First GUI")
icon = tk.PhotoImage(file="3580-23831-8107.png")
window.iconphoto(True,icon)
window.config(background="#7c6b6b")

photo = tk.PhotoImage(file="braided red cutie.png")
photo = photo.subsample(2,2)

with open("phrases.txt") as file_content:
    for line in file_content:
        phrase_list = file_content.readlines()

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