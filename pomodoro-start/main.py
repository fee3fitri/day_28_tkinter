from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
# Create Tkinter window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)

# Timer label
timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer.grid(row=0, column=1)

# Create image canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)
count_down(5)

# Start button
start = Button(text="Start", command=start_timer, bg=GREEN, highlightthickness=0, font=(FONT_NAME), cursor="hand2")
start.grid(row=2, column=0)
start.config(padx=10)

# Reset button
def reset():
    pass

reset = Button(text="Reset", command=reset, bg=GREEN, highlightthickness=0, font=(FONT_NAME), cursor="hand2")
reset.grid(row=2, column=2)
reset.config(padx=10)

# Checkmark label
check = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check.grid(row=3, column=1)
check.config(pady=20)
window.mainloop()
