import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
  window.after_cancel(timer)
  
  global reps 
  reps = 0

  timer_label.config(text="Timer")
  canvas.itemconfig(timer_text, text="00:00")
  check_mark_label.config(text="")
  

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  timer_label_text = ""
  color = ""

      
  if reps % 8 == 0:
    minutes = LONG_BREAK_MIN
    timer_label_text = "Break"
    color = RED
  elif reps % 2 == 0:
    minutes = SHORT_BREAK_MIN
    timer_label_text = "Break"
    color = PINK
  else:
    minutes = WORK_MIN
    timer_label_text = "Work"
    color = GREEN
 
  count = minutes * 60
  timer_label.config(text=timer_label_text, fg=color)  
  count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
  seconds = count % 60
  minutes = count // 60
  time = str(minutes) + ":"
  
  if seconds < 10:
    time += "0"

  time += str(seconds)
 
  canvas.itemconfig(timer_text, text=time)
  
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    work_sessions = int(reps / 2)
    marks = ""

    for _ in range(work_sessions):
      marks += "✓"

    check_mark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#timer label

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)

timer_label.grid(row=0, column=1)

#canvas
canvas = tkinter.Canvas(width=220, height=224, highlightthickness=0, bg=YELLOW)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35))
canvas.grid(row=1, column=1)

print(303%60)

#start button
start_button = tkinter.Button(text="Start", highlightthickness=0, bg="white", command=start_timer)
start_button.grid(row=2, column=0)

#reset button
reset_button = tkinter.Button(text="Reset",  highlightthickness=0, bg="white", command=timer_reset)
reset_button.grid(row=2, column=2)

#check mark
check_mark_label = tkinter.Label(window, font=("Arial", 20), fg=GREEN, bg=YELLOW)

check_mark_label.grid(row=3, column=1)

window.mainloop()
