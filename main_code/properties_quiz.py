from random import randint
from tkinter import *
from main_code import database_reader as data


# Used to call the property quiz from menu
def main():
    pr = Properties()
    pr.category_menu()


# Class for the general variables
class Properties:
    def __init__(self):
        self.list_of_properties = [data.atomic_number, data.english_names, data.latin_names, data.year_of_discovery,
                                   data.electron_shell, data.atomic_mass, data.atomic_density, data.element_group,
                                   data.melting_point, data.boiling_point, data.atomic_letters]
        self.list_of_properties_names = ['atomic number', 'english name', 'latin name', 'year of discovery',
                                         'electron shell', 'atomic mass', 'atomic density', 'element group',
                                         'melting point', 'boiling point', 'atomic letter']
        self.choice = 0
        self.random_element = randint(0, 118)
        self.correct_answer = ''
        self.wrong_answer = ''
        self.wrong_answer_count = 0

    # Definition to delete windows that are not necessary
    def destroy_window(self, window):
        window.destroy()

    # Checks whether the answer is correct
    def answer_check(self, answer):
        database_answer_property = self.list_of_properties[self.choice]
        self.database_answer = database_answer_property[self.random_element]
        if answer.lower() == self.database_answer.lower():
            self.correct_answer = 'Correct! Answer next question.'
            self.question_label2['text'] = self.correct_answer
            self.wrong_answer_count = 0
            data.correct_audio.play()
            self.question_generation()
        else:
            self.wrong_answer = 'Wrong!'
            self.wrong_answer_count += 1
            self.question_label2['text'] = self.wrong_answer
            data.wrong_audio.play()

        self.answer_input.delete(0, END)

        if self.wrong_answer_count == 3:
            self.wrong_answer_count = 0
            self.question_label2['text'] = 'Wrong!\n The correct answer is: ' + self.database_answer + \
                                           '\nBetter luck with the next question!'
            data.wrong_audio.play()
            self.question_generation()

    def question_generation(self):
        # Creates the question
        self.random_element = randint(0, 118)

        if self.a_e == 0:
            question = 'What is the ' + self.list_of_properties_names[self.choice] + ' of atomic number ' + \
                       data.atomic_number[self.random_element] + '?'
        elif self.a_e == 1:
            question = 'What is the ' + self.list_of_properties_names[self.choice] + ' of ' + \
                       data.english_names[self.random_element] + '?'
        else:
            question = 'Error'
        self.question_label['text'] = question

    # Window for the screen where you input the answer
    def question_window(self, a_e, skip, window):
        # If previous window was skipped set choices for right questions, otherwise destroy previous window
        self.a_e = a_e
        if skip:
            if a_e == 1:
                self.choice = 1
                self.a_e = 0
            else:
                self.choice = 0
                self.a_e = 1
        else:
            self.destroy_window(window)

        # Create input screen for answering
        question_screen = Tk()
        question_screen.title('Know your elements')
        question_screen.configure(bg='white')
        question_screen.geometry("700x100")
        self.question_label = Label(question_screen, text='',bg='white')
        self.question_label.grid(row=0, column=0)
        self.question_generation()
        self.question_label.config(font=('Calibri', 13))

        self.question_label2 = Label(question_screen, text='Please plug in your answer', bg='white')
        self.question_label2.grid(row=1, columnspan=2)
        self.question_label2.config(font=('Calibri', 13))

        # Requests an answer input
        self.answer_input = Entry(question_screen)
        self.answer_input.grid(row=0, column=1)
        self.answer_input.config(font=('Calibri', 13))
        self.answer_input.bind('<Return>', lambda e: self.answer_check(self.answer_input.get()))

        # Gets the requested values of the height and width.
        window_width = question_screen.winfo_reqwidth()
        window_height = question_screen.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(question_screen.winfo_screenwidth() / 2.4 - window_width)
        position_down = int(question_screen.winfo_screenheight() / 1.65 - window_height)

        # Positions the window in the center of the page.
        question_screen.geometry('+{}+{}'.format(position_right, position_down))

    # Creates window where english name or atomic number can be chosen
    def question_format(self, i):
        self.choice = i
        aore = Tk()
        aore.title('Know your elements')
        aore.configure(bg='white')
        frame = Frame(aore, width=1, height=1, bg='lightgrey')
        frame.pack()

        # Gets the requested values of the height and width.
        window_width = aore.winfo_reqwidth()
        window_height = aore.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(aore.winfo_screenwidth() / 2.27 - window_width)
        position_down = int(aore.winfo_screenheight() / 1.7 - window_height)

        # Positions the window in the center of the page.
        aore.geometry('+{}+{}'.format(position_right, position_down))

        # Asks question A or E
        label_1 = Label(frame, text='Do you want to learn with atomic numbers or english names?', bg='white')
        label_1.grid(row=0, column=0)
        label_1.config(font=('Calibri', 13))

        a_button = Button(aore, text='Atomic numbers', command=lambda: self.question_window(0, False, aore), fg='black',
                          bg='lightgrey')
        a_button.config(font=('Calibri', 13))
        a_button.pack(expand=YES, pady=10)

        e_button = Button(aore, text='English names', command=lambda: self.question_window(1, False, aore), fg='black',
                          bg='lightgrey')
        e_button.config(font=('Calibri', 13))
        e_button.pack(expand=YES, pady=10)

    # Creates the main window where you choose the category
    def category_menu(self):
        # Creates a basic tkinter window with a title and its background set to white
        root = Tk()
        root.title('Know your elements')
        root.configure(bg='white')

        # Gets the requested values of the height and width.
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        position_right = int(root.winfo_screenwidth() / 1.96 - window_width)
        position_down = int(root.winfo_screenheight() / 4.2 - window_height)

        # Positions the window in the center of the page.
        root.geometry('+{}+{}'.format(position_right, position_down))

        # Creating a main menu title in the window
        menu_name = Label(root, text='Choose a category:', fg='black', bg='white')
        menu_name.config(font=('Calibri', 17))
        menu_name.pack(expand=YES, pady=30)

        categories = ['atomic number', 'english name', 'latin name', 'year of discovery', 'electron shell',
                      'atomic mass', 'atomic density', 'element group', 'melting point', 'boiling point']

        # Loop for the category buttons
        for i in range(0, len(categories)):
            globals()['button%s' % i] = Button(root, text=categories[i].capitalize(),
                                               command=lambda i=i: self.question_format(i)
                                               if i != 0 and i != 1 else
                                               self.question_window(i, True, root), fg='white', bg='grey40', width=17)
            globals()['button%s' % i].config(font=('Calibri', 15))
            globals()['button%s' % i].pack(expand=YES, pady=10, padx=80)

        # Quit button just simply breaks the loop
        back_button = Button(root, text='Close', fg='red4', command=lambda: root.destroy(), bg='grey40')
        back_button.config(font=('Calibri', 15))
        back_button.pack(expand=YES, pady=10)