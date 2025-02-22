from tkinter import *
from tkinter import messagebox

def submit():
    if question1entry.get() == "Linus Torvalds":
        messagebox.showinfo("Correct", "Correct!!!!")
        question1submit.pack_forget()
        question1entry.pack_forget()
        question2entry.pack()
        question2submit.pack()
        questionlabel.config(text= "Question 2 : Is Steve Jobs the co-founder of Apple Inc.?")
    if question1entry.get() != "Linus Torvalds":
        messagebox.showinfo("Incorrect", "Incorrect!!!!")


def submit2():
    if question2entry.get().lower() == "yes":
        messagebox.showinfo("Correct", "Correct!!!!")
        question2entry.pack_forget()
        question2submit.pack_forget()
        questionlabel.config(text="Question 3 : What is currently the most popular free and open source operating system?")
        question3entry.pack()
        question3submit.pack()
    if question2entry.get() != "yes":
        messagebox.showinfo("Incorrect", "Incorrect!!!!")


def submit3():
    if question3entry.get().lower() == "linux":
        messagebox.showinfo("Correct", "Correct!!!!")
        question3entry.pack_forget()
        question3submit.pack_forget()
        questionlabel.config(text="Question 4 : What is currently the most popular desktop operating system?")
        question4entry.pack()
        question4submit.pack()
    if question3entry.get() != "linux":
        messagebox.showinfo("Incorrect", "Incorrect!!!!")
def submit4():
    if question4entry.get().lower() == "windows":
        messagebox.showinfo("Correct", "Correct!!!!")
        question4entry.pack_forget()
        question4submit.pack_forget()
        questionlabel.config(text="Question 5: What is the most popular mobile operating system?")
        question5entry.pack()
        question5submit.pack()
    if question4entry.get() != "windows":
        messagebox.showinfo("Incorrect", "Incorrect!!!!")

def submit5():
    if question5entry.get().lower() == "android":
        messagebox.showinfo("Correct", "Correct!!!!")
        messagebox.showinfo("yay","YOU WIN YAYYYYY")
    if question5entry.get() != "android":   
        messagebox.showinfo("Incorrect", "Incorrect!!!!")

window = Tk()
window.title("Quiz")
window.geometry("600x300")
window.config(bg="grey")



questionlabel = Label(window, text="Question 1 : Who created the Linux Kernel?")
questionlabel.pack()

question1entry = Entry(window)
question1entry.pack()

question2entry = Entry(window)

question1submit = Button(window,text = "Submit",command=submit)
question1submit.pack()

question2submit = Button(window,text = "Submit",command=submit2)

question3entry = Entry(window)
question3submit = Button(window,text = "Submit",command=submit3)

question4entry = Entry(window)
question4submit = Button(window,text="Submit",command=submit4)

question5entry = Entry(window)
question5submit = Button(window,text="Submit",command=submit5)

window.mainloop()