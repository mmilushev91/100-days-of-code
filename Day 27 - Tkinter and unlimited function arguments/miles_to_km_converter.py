import tkinter

COUNT = 3
MILE_IN_KM = 1.609344

def calculate_km():
  kilometers = float(miles_entry.get()) * MILE_IN_KM
  kilometers_amount_label.config(text=f"{kilometers:.2f}")
  miles_entry.delete(0, "end")

window = tkinter.Tk()
window.title(string="Mile To Km Conveter")
window.config(padx=50, pady=20)

#Miles entry
miles_entry = tkinter.Entry(width=7)
miles_entry.grid(row=0, column=1)


#Miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)


#is qual to label
is_qual_to_label = tkinter.Label(text="is equal to")
is_qual_to_label.grid(row=1, column=0)
is_qual_to_label.config(pady=20)

#Kilometers amount label

kilometers_amount_label = tkinter.Label(text=0)
kilometers_amount_label.grid(row=1, column=1)

#Kilometers label

kilometers_label = tkinter.Label(text="KM")
kilometers_label.grid(row=1, column=2)

#calculate button
calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
