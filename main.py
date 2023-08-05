from tkinter import *


def calculate():
    get_mile = user_input.get()
    get_mile_convert = float(get_mile)
    label_km_num["text"] = str(round(1.609 * get_mile_convert,2))


def calculate_km_to_mile():
    get_km = float(user_km_input.get())
    label_mile_num["text"] = str(round(get_km/1.609, 2))


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Labels
label_equal = Label(text="is equal to", font=("Arial", 19))
label_equal.grid(column=0, row=1)
label_equal.config(padx=10, pady=10)

label_mile = Label(text="Miles", font=("Arial", 18))
label_mile.grid(column=3, row=0)
label_mile.config(padx=10, pady=10)

label_km = Label(text="Km", font=("Arial", 18))
label_km.grid(column=3, row=1)
label_km.config(padx=10, pady=10)

label_km_num = Label(text="0", font=("Arial", 18))
label_km_num.grid(column=1, row=1)
label_km_num.config(padx=10, pady=10)


label_mile_num = Label(text="0", font=("Arial", 18))
label_mile_num.grid(column=2, row=0)
label_mile_num.config(padx=10, pady=10)

button_calculate = Button(text="Calculate Km", command=calculate)
button_calculate.grid(column=1, row=2)
button_calculate.config(padx=10, pady=10)

button_calculate2 = Button(text="Calculate Mile", command=calculate_km_to_mile)
button_calculate2.grid(column=2, row=2)
button_calculate2.config(padx=10, pady=10)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)
# user_input.config(padx=10, pady=10)

user_km_input = Entry(width=10)
user_km_input.grid(column=2, row=1)

window.mainloop()
