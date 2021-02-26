# dietetyk online
from tkinter import *


# inicjacja okna
dietWindow = Tk()
dietWindow.geometry("600x300")
dietWindow.resizable(0, 0)
dietWindow.title("DIETETYK")
Label(dietWindow, text='LICZNIK BMI', font='arial 15 bold').pack()
Label(dietWindow, text='DIETETYK ONLINE', font='arial 15 bold').pack(side=BOTTOM)
weight_label = Label(dietWindow, text='Podaj swoją wagę w kg', font='arial 10 bold').pack()
selectedWeight = IntVar(dietWindow, value=0)
setweight = Spinbox(dietWindow, from_=30, to_=200, textvariable=selectedWeight, width=15).pack()
height_label = Label(dietWindow, text='Podaj swój wzrost w cm', font='arial 10 bold').pack()
selectedHeight = IntVar(dietWindow, value=0)
setheight = Spinbox(dietWindow, from_=50, to_=250, textvariable=selectedHeight, width=15).pack()
bmiResult = StringVar()


def ObliczBmi():

    bmi = (selectedWeight.get() / ((selectedHeight.get()/100) * (selectedHeight.get()/100)))
    bmiComment = ''
    bmiResult.set(0)
    if 25 >= bmi > 18:
        bmiComment = 'Twoje bmi jest w porządku, zalecana dieta podtrzymującą aktualną masę ciała'
    if bmi < 18:
        bmiComment = ' Masz niedowagę. Zalecana dieta zwiększająca masę ciała.'
    if 25 < bmi < 30:
        bmiComment = 'Masz nadwage.Schudnij.'
    if 30 < bmi < 40:
        bmiComment = 'Masz otyłość pierwszego stopnia natychmiast zredukuj wagę.'
    if bmi > 40:
        bmiComment = 'Jesteś otyły i to w drugim stopniu. Schudnij świniaku.'
    bmiResult.set(bmiComment)


Button(dietWindow, text="Oblicz BMI", command=ObliczBmi).pack(pady=10)
Entry(dietWindow, textvariable=bmiResult, width='80').pack(pady=10)

dietWindow.mainloop()
