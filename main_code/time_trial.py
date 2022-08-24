from main_code import periodic_table as pt, statistics as st
from tkinter import *
import time


def main(caller):
    pt.main(caller)


# Class for the timer that is on the time trial
class Timer(Label):
    def __init__(self, frame):
        Label.__init__(self)
        self.time_remaining_label = Label(frame, text="Time Remaining:", bg='lightgrey')
        self.time_remaining_label.config(font=("Calibri", 15))
        self.time_remaining_label.grid(row=3, column=2, columnspan=3, sticky=NSEW)
        self.label = Label(frame, text="", bg='lightgrey')
        self.label.grid(row=3, column=5, columnspan=2, sticky=NSEW)
        self.label.config(font=("Calibri", 15))
        self.remaining = 0
        self.score = 0
        self.timestamp = ""
        self.starting_time = 30
        self.countdown(self.starting_time)

    # Each correct answer gives 5 seconds extra
    def add_time(self):
        self.remaining += 5
        self.score += 1

    # Function for counting down and quitting and changing color
    def countdown(self, remaining=None):
        # skip this part if there is no remaining
        if remaining is not None:
            self.remaining = remaining

        if self.remaining in range(6, 11):
            self.time_remaining_label.configure(bg='gold')
            self.label.configure(bg='gold')
        elif self.remaining in range(1, 6):
            self.time_remaining_label.configure(bg='red')
            self.label.configure(bg='red')
        elif self.remaining > 10:
            self.time_remaining_label.configure(bg='lightgrey')
            self.label.configure(bg='lightgrey')

        # Time has run out
        if self.remaining == 0 or self.score == 118:
            self.timestamp = (time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())).split(' ')
            self.timestamp.remove(self.timestamp[0])
            self.timestamp = " ".join(self.timestamp)
            st.update(self.score, self.timestamp)
            self.label.configure(text="Time's up!\n You found " + str(self.score) +"/118 elements")
            self.label.config(font=("Calibri", 15))
            self.label.grid(row=3, column=5, columnspan=7, sticky=NSEW)
            pt.table.correct_label.grid_forget()
            pt.PeriodicTable.disable_answer_input(pt.table)
        # If the close button is pressed, the code stops looping
        elif self.remaining == -1:
            self.label.destroy()
            pt.table.root.destroy()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining -= 1
            self.after(1000, self.countdown)

    # Stops the timer
    def close_timer(self):
        if self.remaining == 0:
            pt.table.root.destroy()
        elif self.score != 118:
            self.remaining = -1
        else:
            self.label.destroy()
            pt.table.root.destroy()

    def get_time(self):
        return self.remaining
