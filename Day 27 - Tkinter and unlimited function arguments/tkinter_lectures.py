import tkinter

def button_got_clicked():
  #takes input value
  input_message = input.get()
  my_label.config(text=input_message)

#creating window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#creating label component
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

#display the label centered on the window
# my_label.pack()
#places label on exact cordinates
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
#change label text
# my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50, pady=50)

#create new button

new_button = tkinter.Button(text="New Button")
new_button.grid(row=1, column=2)

#create button

button = tkinter.Button(text="Click me", command=button_got_clicked)
button.grid(row=2, column=1)

#create input field
input = tkinter.Entry()
input.grid(row=3, column=3)

#keeps window open and needs to be at the bottom of the code
window.mainloop()
