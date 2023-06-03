from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Constants that determine the work and break lengths
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None


def start_timer():  # Control how the timings change after you click the start button
    global reps
    reps += 1  # counts how many times the timer has been reset, increases by 1 after the timer goes to 0

    # converts minutes into seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 4 == 0:  # long break every 2 work blocks (setup for 50-minute block)
        reps += 1
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # short break after every work block
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):  # controls how the program counts down
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # after one second the time counts down
    else:
        start_timer()
        if reps % 2 == 0:  # after every work block, a checkmark gets added
            new_text = checkmark_text.get()
            new_text += "✔"
            checkmark_text.set(new_text)


def timer_reset():  # resets all the settings once the reset button is clicked
    global reps
    canvas.itemconfig(timer_text, text=f"00:00")
    window.after_cancel(timer)
    title_label.config(text="Pomodoro")
    checkmark_text.set("")
    reps = 0
    pass


# screen setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato image setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(row=1, column=1)

# timer text setup
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# start button setup
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# reset button setup
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2)

# checkmark setup
checkmark_text = StringVar()
checkmark = Label(textvariable=checkmark_text, fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

# title setup
title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
title_label.grid(row=0, column=1)

window.mainloop()
