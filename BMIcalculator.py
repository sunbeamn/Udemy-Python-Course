import tkinter
from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.minsize(width=300, height=250)
root.config(padx=30, pady=30)

Label_Weight = tkinter.Label(text="Enter your Weight (kg)")
Label_Weight.grid(column=0, row=0, pady=5)

enter_ur_kg = tkinter.Entry()
enter_ur_kg.grid(column=0, row=1, pady=10)

Label_Height = tkinter.Label(text="Enter your Height (cm)")
Label_Height.grid(column=0, row=2, pady=5)

enter_ur_cm = tkinter.Entry()
enter_ur_cm.grid(column=0, row=3, pady=10)

result_label = tkinter.Label(text="")
result_label.grid(column=0, row=5, pady=15)


def calculate():
    try:
        weight = float(enter_ur_kg.get())
        height = float(enter_ur_cm.get()) / 100
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is {round(bmi, 2)}", fg="black")
    except ValueError:
        result_label.config(text="Please enter valid characters.", fg="red")

Button1 = tkinter.Button(text="Calculate", command=calculate)
Button1.grid(column=0, row=4, pady=10)

root.mainloop()