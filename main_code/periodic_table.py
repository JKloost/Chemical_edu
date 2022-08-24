from tkinter import *
import webbrowser
from main_code import database_reader as data, time_trial as tt


def main(caller):
    global table
    table = PeriodicTable()
    table.table_window(caller)


class PeriodicTable:
    def __init__(self):
        # Group-to-colour linking
        self.group_colours = {"Reactive nonmetal": "mediumseagreen", "Noble gas": "dodgerblue", "Alkali metal": "red",
                              "Alkaline earth metal": "darkorange1", "Metalloid": "olivedrab2", "Transition metal":
                              "gold", "Post-transition metal": "lightgoldenrod1", "Lanthanide": "navajowhite3",
                              "Actinide": "navajowhite4", "Unknown": "ivory2"}
        self.correct = 0

    def get_correct(self):
        return self.correct

    def table_window(self, caller):
        self.root = Tk()
        frame = Frame(self.root, width=1, height=1, bg="white")
        frame.pack()
        self.root.title("Know your elements")

        # Gets the requested values of the height and width.
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(self.root.winfo_screenwidth() / 3.5 - window_width)
        position_down = int(self.root.winfo_screenheight() / 3 - window_height)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(position_right, position_down))

        # Adding a label with a name
        periodic_table_name = Label(frame, text="Periodic Table", fg="black", bg="white")
        periodic_table_name.grid(columnspan=18, row=0)
        periodic_table_name.config(font=("Calibri", 17))

        # Adds little space between main table and lanthanides and actinides
        little_space_0 = Label(frame, text=" ", bg="white")
        little_space_0.grid(row=8, column=0, sticky=NSEW)
        little_space_0.config(font=("Calibri", 21))

        # Creating the back button which is supposed to bring back to main menu upon event
        back_button = Button(frame, text="Close", fg="red4", command=lambda: self.close_table(caller), bg="grey40")
        back_button.grid(columnspan=2, row=11, sticky=NSEW)
        back_button.config(font=("Calibri", 21))

        # Creating a button for every element and positioning it correctly
        self.grid_column = [0, 17, 0, 1, 12, 13, 14, 15, 16, 17, 0, 1, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                       11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 2,
                       3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0,
                       1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                       16, 17]
        self.grid_row = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                    4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                    9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 7, 7,
                    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

        if caller == 'Menu':
            for element in range(1, 119):
                globals()['element%s' % element] = Button(frame, text=data.atomic_letters[element - 1],
                                                          command=lambda element=element: self.element_select(element),
                                                          fg="black",
                                                          bg=self.group_colours[data.element_group[element - 1]], width=3, height=1)
                globals()['element%s' % element].config(font=("Courier Bold", 21))
                globals()['element%s' % element].grid(column=self.grid_column[element - 1], row=self.grid_row[element - 1],
                                                      sticky=NSEW)

        elif caller == 'TimeTrial':
            found_list = []
            for element in range(1, 119):
                globals()['element%s' % element] = Button(frame, text="?", fg="lightgrey", bg="lightgrey", width=3)
                globals()['element%s' % element].config(font=("Courier Bold", 21))
                globals()['element%s' % element].grid(column=self.grid_column[element - 1], row=self.grid_row[element - 1],
                                                      sticky=NSEW)

            self.question_label = Label(frame, text="Enter an element:", anchor='w')
            self.question_label.config(font=("Calibri", 21))
            self.question_label.grid(row=11, column=2, columnspan=5, sticky=NSEW)

            self.answer_input = Entry(frame, bg="lightgrey")
            self.answer_input.config(font=("Calibri", 21))
            self.answer_input.grid(row=11, column=7, columnspan=9, sticky=NSEW)
            self.answer_input.bind("<Return>", lambda e: self.update_table(self.answer_input.get(), found_list))

            time_remaining_label = Label(frame, text="Time Remaining:")
            time_remaining_label.config(font=("Calibri", 15))
            time_remaining_label.grid(row=3, column=2, columnspan=3, sticky=NSEW)
            self.timer = tt.Timer(frame)

            self.correct_label = Label(frame, text="Elements found: " + str(self.get_correct()) + '/' + '118', bg='lightgrey')
            self.correct_label.config(font=("Calibri", 15))
            self.correct_label.grid(row=3, column=7, columnspan=5, sticky=NSEW)

    def element_select(self, atomic_number):
        main_root = Tk()
        main_root.title("Element " + str(atomic_number))
        main_root.configure(bg="white")
        frame = Frame(main_root, width=1, height=1, bg="lightgrey")
        frame.pack()

        # Gets the requested values of the height and widht.
        window_width = main_root.winfo_reqwidth()
        window_height = main_root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width)
        position_down = int(main_root.winfo_screenheight() / 1.7 - window_height)

        # Positions the window in the center of the page.
        main_root.geometry("+{}+{}".format(position_right, position_down))

        self.element_title = Label(frame, text="       Element " + str(atomic_number) + "       ", fg="black", bg="lightgrey", relief="groove")
        self.element_title.grid(columnspan=2, row=0)
        self.element_title.config(font=("Calibri", 13))

        # Button for wikipedia link
        wikipedia_text = Label(frame, text="   Wikipedia button:   ", fg="black", bg="lightgrey", relief="groove")
        wikipedia_text.grid(row=0, column=2)
        wikipedia_text.config(font=("Calibri", 13))

        self.element_url = "https://en.wikipedia.org/wiki/" + data.english_names[atomic_number - 1]
        element_atomic_letter = Button(frame, text=data.atomic_letters[atomic_number - 1], fg="black",
                                       command=lambda: webbrowser.open(self.element_url, new=1),
                                       bg=self.group_colours[data.element_group[atomic_number - 1]])
        element_atomic_letter.config(font=("Calibri", 80))
        element_atomic_letter.grid(column=2, rowspan=9, sticky=NSEW)

        element_english_names_0 = Label(frame, text="English name:", anchor='w')
        element_english_names_0.grid(column=0, row=1, sticky=NSEW)
        element_english_names_1 = Label(frame, text=data.english_names[atomic_number - 1], anchor='w')
        element_english_names_1.grid(column=1, row=1, sticky=NSEW)

        element_latin_names_0 = Label(frame, text="Latin name:", anchor='w')
        element_latin_names_0.grid(column=0, row=2, sticky=NSEW)
        element_latin_names_1 = Label(frame, text=data.latin_names[atomic_number - 1], anchor='w')
        element_latin_names_1.grid(column=1, row=2, sticky=NSEW)

        element_year_of_discovery_0 = Label(frame, text="Year of discovery:", anchor='w')
        element_year_of_discovery_0.grid(column=0, row=3, sticky=NSEW)
        element_year_of_discovery_1 = Label(frame, text=data.year_of_discovery[atomic_number - 1], anchor='w')
        element_year_of_discovery_1.grid(column=1, row=3, sticky=NSEW)

        element_element_group_0 = Label(frame, text="Element group:", anchor='w')
        element_element_group_0.grid(column=0, row=4, sticky=NSEW)
        element_element_group_1 = Label(frame, text=data.element_group[atomic_number - 1], anchor='w')
        element_element_group_1.grid(column=1, row=4, sticky=NSEW)

        element_atomic_mass_0 = Label(frame, text="Atomic mass:", anchor='w')
        element_atomic_mass_0.grid(column=0, row=5, sticky=NSEW)
        element_atomic_mass_1 = Label(frame, text=data.atomic_mass[atomic_number - 1] + " u", anchor='w')
        element_atomic_mass_1.grid(column=1, row=5, sticky=NSEW)

        element_atomic_density_0 = Label(frame, text="Atomic density:", anchor='w')
        element_atomic_density_0.grid(column=0, row=6, sticky=NSEW)
        element_atomic_density_1 = Label(frame, text=data.atomic_density[atomic_number - 1] + " g/cm^3", anchor='w')
        element_atomic_density_1.grid(column=1, row=6, sticky=NSEW)

        element_electron_shell_0 = Label(frame, text="Electron shells:", anchor='w')
        element_electron_shell_0.grid(column=0, row=7, sticky=NSEW)
        element_electron_shell_1 = Label(frame, text=data.electron_shell[atomic_number - 1], anchor='w')
        element_electron_shell_1.grid(column=1, row=7, sticky=NSEW)

        element_melting_point_0 = Label(frame, text="Melting point:", anchor='w')
        element_melting_point_0.grid(column=0, row=8, sticky=NSEW)
        element_melting_point_1 = Label(frame, text=data.melting_point[atomic_number - 1], anchor='w')
        element_melting_point_1.grid(column=1, row=8, sticky=NSEW)

        element_boiling_point_0 = Label(frame, text="Boiling point:", anchor='w')
        element_boiling_point_0.grid(column=0, row=9, sticky=NSEW)
        element_boiling_point_1 = Label(frame, text=data.boiling_point[atomic_number - 1], anchor='w')
        element_boiling_point_1.grid(column=1, row=9, sticky=NSEW)

        close_button = Button(frame, text="Close", fg="white", command=lambda: main_root.destroy(), bg="grey40")
        close_button.grid(columnspan=3, row=10, sticky=NSEW)
        close_button.config(font=("Calibri", 13))

    # Update the table for time trial
    def update_table(self, answer, found_list):
        given_input = answer
        # Given input in english names
        if given_input.capitalize() in data.english_names and (data.english_names.index(given_input.capitalize()) + 1) not in found_list:
            self.correct += 1
            self.timer.add_time()
            typed_element = data.english_names.index(given_input.capitalize()) + 1
            found_list.append(typed_element)
            globals()['element%s' % typed_element].configure(text=data.atomic_letters[typed_element - 1],
                                                             command=lambda typed_element=typed_element: self.element_select(
                                                                 typed_element), fg="black", width=3,
                                                             bg=self.group_colours[data.element_group[typed_element - 1]])
            globals()['element%s' % typed_element].config(font=("Courier Bold", 21))
            globals()['element%s' % typed_element].grid(column=self.grid_column[typed_element - 1],
                                                        row=self.grid_row[typed_element - 1], sticky=NSEW)
        # Given input in latin names
        elif given_input.capitalize() in data.latin_names and (data.latin_names.index(given_input.capitalize()) + 1) not in found_list:
            self.correct += 1
            self.timer.add_time()
            typed_element = data.latin_names.index(given_input.capitalize()) + 1
            found_list.append(typed_element)
            globals()['element%s' % typed_element].configure(text=data.atomic_letters[typed_element - 1],
                                                             command=lambda
                                                                 typed_element=typed_element: self.element_select(
                                                                 typed_element), fg="black", width=3,
                                                             bg=self.group_colours[
                                                                 data.element_group[typed_element - 1]])
            globals()['element%s' % typed_element].config(font=("Courier Bold", 21))
            globals()['element%s' % typed_element].grid(column=self.grid_column[typed_element - 1],
                                                        row=self.grid_row[typed_element - 1], sticky=NSEW)

        self.answer_input.delete(0, END)
        self.correct_label.configure(text="Elements found: " + str(self.get_correct()) + '/' + '118')

    def close_table(self, caller):
        if caller == 'TimeTrial':
            tt.Timer.close_timer(self.timer)
        else:
            self.root.destroy()

    def disable_answer_input(self):
        self.question_label.destroy()
        self.answer_input.destroy()
