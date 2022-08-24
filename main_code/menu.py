from tkinter import *
from main_code import properties_quiz as pq, time_trial as tt, periodic_table as pt, statistics as st


# Creates a basic tkinter window with a title and its background set to white
class MainMenu:
    root = Tk()
    root.title("Know your elements")
    root.configure(bg="white")

    # Gets the requested values of the height and width.
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth() / 2.3 - window_width)
    position_down = int(root.winfo_screenheight() / 2.3 - window_height)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(position_right, position_down))

    # Program title
    program_title = Label(root, text="Know Your Elements", fg="black", bg='lightgrey')
    program_title.config(font=("Calibri", 21))
    program_title.grid(row=0, column=1, columnspan=3, sticky=NSEW)

    # Program info
    program_label = Label(root, text="Welcome to Know Your Elements! A program designed for both beginning "
                                     "learners\nas well as chemistry fanatics to test their knowledge of the "
                                     "periodic table of elements.\nIn the main menu below you will find several "
                                     "options to choose from.", fg="black", bg='white')
    program_label.config(font=("Calibri", 12))
    program_label.grid(row=1, column=1, columnspan=2, sticky=NSEW)

    # Creating a main menu title in the window, not sure if an image would not be better
    menu_name = Label(root, text="Main Menu", fg="black", bg='lightgrey')
    menu_name.config(font=("Calibri", 17))
    menu_name.grid(row=2, columnspan=2, column=1, pady=10, sticky=NSEW)

    # Creation of the first button which still has to be bound to periodic_table
    periodic_table_button = Button(root, text="Periodic table", command=lambda: pt.main('Menu'), fg="white", bg="grey40", width=17)
    periodic_table_button.config(font=("Calibri", 16))
    periodic_table_button.grid(row=4, columnspan=2, column=1, sticky=NS, padx=10, pady=10)

    # Second button creation which has to be bound to properties_quiz
    properties_quiz_button = Button(root, text="Properties Quiz", command=lambda: pq.main(), fg="white", bg="grey40", width=17,)
    properties_quiz_button.config(font=("Calibri", 16))
    properties_quiz_button.grid(row=6, columnspan=2, column=1, sticky=NS, padx=10, pady=10)

    # Third button creation which has to be bound to time_trial
    time_trial_button = Button(root, text="Time Trial", command=lambda: tt.main('TimeTrial'), fg="white", bg="grey40", width=17,)
    time_trial_button.config(font=("Calibri", 16))
    time_trial_button.grid(row=8, columnspan=2, column=1, sticky=NS, padx=10, pady=10)

    # Fourth button creation which has to be bound to statistics
    statistics_button = Button(root, text="Statistics", command=lambda: st.main(), fg="white", bg="grey40", width=17,)
    statistics_button.config(font=("Calibri", 16))
    statistics_button.grid(row=10, columnspan=2, column=1, sticky=NS, padx=10, pady=10)

    # Quit button just simply breaks the loop
    quit_button = Button(root, text="Exit Program", fg="red4", command=quit, bg="grey40", width=17)
    quit_button.config(font=("Calibri", 16))
    quit_button.grid(row=13, columnspan=2, column=1, sticky=NS, padx=10, pady=10)

    root.mainloop()
