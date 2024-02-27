from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}"))
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


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
