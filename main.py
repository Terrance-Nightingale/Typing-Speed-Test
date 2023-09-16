from tkinter import *
import math

SECONDS = 60
timer = None
sample = "\"Studying is the main source of knowledge. Books are indeed never failing friends of man. " \
         "For a mature mind, reading is the greatest source of pleasure and solace to distressed minds. " \
         "The study of good books ennobles us and broadens our outlook. Therefore," \
         " the habit of reading should be cultivated. A student should never confine himself to his schoolbooks only." \
         " He should not miss the pleasure locked in the classics, poetry, drama, history, philosophy etc." \
         " We can derive benefit from other’s experiences with the help of books. " \
         "The various sufferings, endurance and joy described in books enable us to have a closer look at human" \
         " life. They also inspire us to face the hardships of life courageously. " \
         "Nowadays there are innumerable books and time is scarce. " \
         "So we should read only the best and the greatest among them. " \
         "With the help of books we shall be able to make our thinking mature " \
         "and our life more meaningful and worthwhile.\""


def start_timer():
    count_down(SECONDS)


def restart_timer():
    speed_result.config(text="Result: 0 wmp")
    canvas.itemconfig(timer_text, text="1:00")
    test_entry.delete("1.0", "end")
    window.after_cancel(timer)


def count_words():
    input = test_entry.get('1.0', 'end-1c')
    words = input.split(" ")
    wpm = len(words)
    speed_result.config(text=f"Result: {wpm} wpm")


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or (count_sec < 10 and count_min == 0):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        count_words()


window = Tk()
window.title("Typing Speed Test App")
window.minsize(width=800, height=500)
window.config(padx=50, pady=20)

title_label = Label(text="Test your typing speed! Type the following within 1 minute: ", font=("Ariel", 15, "bold"))
title_label.pack()

sample_label = Label(text=sample, font=("Ariel", 10, "bold"), highlightthickness=5, borderwidth=3, relief="solid")
sample_label.config(wraplength=500, anchor="e", justify="left", pady=10, padx=10)
sample_label.pack()

test_entry = Text(width=50, height=15)
test_entry.pack(side="right", pady=30, padx=30)
test_entry.focus()

timer_frame = Frame()
timer_frame.pack(side="left")

canvas = Canvas(timer_frame, width=200, height=120, highlightthickness=0)
timer_title = canvas.create_text(100, 50, text="Timer", font=("Courier", 24, "bold"))
timer_text = canvas.create_text(100, 100, text="1:00", font=("Courier", 35, "bold"))
canvas.pack()

start_btn = Button(timer_frame, text="Start", width=8, font=("Courier", 24, "bold"), command=start_timer)
start_btn.pack()

restart_btn = Button(timer_frame, text="Restart", width=8, font=("Courier", 24, "bold"), command=restart_timer)
restart_btn.pack()

speed_result = Label(timer_frame, text="Result: 0 wpm", font=("Courier", 24, "bold"), fg="green")
speed_result.config(pady=15, padx=15)
speed_result.pack(side="bottom")

window.mainloop()
