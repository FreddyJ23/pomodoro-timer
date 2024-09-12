from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")




# ---------------------------- TIMER MECHANISM ------------------------------- # 



def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_rep = SHORT_BREAK_MIN * 60
    long_break_rep = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(round(long_break_rep))
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(round(short_break_rep))
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(round(work_sec))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        marks = ""
        # check for every work session
        for rep in range(math.floor(reps/2)):
            marks += "✓"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row= 0)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tom_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold") )
checkmark.grid(column=1, row= 3)






window.mainloop()