from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)


def miles_to_km():
    miles_entered = float(miles_input.get())
    km_calculated = round(miles_entered * 1.609, 2)
    km_result.config(text=f"{km_calculated}")


miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

miles = Label(text="Miles", font=("Arial", 18))
miles.grid(row=0, column=2)

equal = Label(text="is equal to", font=("Arial", 18))
equal.grid(row=1, column=0)

km_result = Label(text=0, font=("Arial", 18))
km_result.grid(row=1, column=1)

km = Label(text="Km", font=("Arial", 18,))
km.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)
















window.mainloop()
