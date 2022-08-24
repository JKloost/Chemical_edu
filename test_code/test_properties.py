from unittest import TestCase
from main_code.properties_quiz import Properties
from main_code import database_reader as data
from tkinter import *


class TestProperties(TestCase):
    def setUp(self):
        self.properties = Properties()
        self.properties.choice = 1
        self.properties.random_element = 8
        self.properties.answer_input = Entry()
        self.properties.a_e = 0

    def test_answer_check(self):
        test_answer_root = Tk()
        self.properties.question_label2 = Label(test_answer_root, text='Please plug in your answer', bg='snow')
        self.properties.question_label2.pack()
        self.properties.answer_check('Helium')
        assert '' is self.properties.answer_input.get()
        assert 'Helium' != self.properties.database_answer
        assert 'Fluorine' == self.properties.database_answer
        assert self.properties.question_label2['text'] == 'Wrong!'

    def test_question_generation(self):
        test_question_root = Tk()
        self.properties.question_label = Label(test_question_root, text='', bg='snow')
        self.properties.question_generation()
        question = 'What is the english name of atomic number ' + data.atomic_number[self.properties.random_element] + '?'
        assert question == self.properties.question_label['text']