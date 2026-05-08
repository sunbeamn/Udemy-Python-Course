mport tkinter
from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.minsize(width=450, height=300)

#I wanted to tried out the real "grid" logic . ..
empty = tkinter.Label(text="blah", fg="white")
empty.grid(column=0,row=0)

empty2 = tkinter.Label(text="blahh",fg="white")
empty2.grid(column=1,row=1)

empty3 = tkinter.Label(text="blahhh",fg="white")
empty3.grid(column=2,row=2)

def get_cm_func():
enter_ur_cm.get()

def get_kg_func():
enter_ur_kg.get()

Label_Weight= tkinter.Label(text="Enter your Weight (kg)", command=get_kg_func)
Label_Weight.grid(column=3, row=0)

Label_Height= tkinter.Label(text="Enter your Height (cm)", command=get_cm_func)
Label_Height.grid(column=3, row=10)


enter_ur_kg= tkinter.Entry()
enter_ur_kg.grid(column=3, row=1)

enter_ur_cm= tkinter.Entry()
enter_ur_cm.grid(column=3, row=15)
'''
def calculate_bmi():

weight=enter_ur_kg.get()
height=enter_ur_cm.get()

BMI = weight/(height*2)

print(f"Your BMI is {BMI}.")


Button1= tkinter.Button(text="Calculate", command=calculate_bmi)
Button1.grid(row=20, column=3)
'''
