# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(2, 4, 6))

from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


my_label["text"] = "New text"


def button_clicked():
    word = input.get()
    my_label.config(text=word)


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=3)





window.mainloop()