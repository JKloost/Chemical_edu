from unittest import TestCase
from main_code.periodic_table import PeriodicTable
from main_code import periodic_table as pt, time_trial as tt
from tkinter import *


class TestPeriodicTable(TestCase):
    def setUp(self):
        self.periodic_table = PeriodicTable()
        self.periodic_table.correct = 5

    def test_get_correct(self):
        assert self.periodic_table.get_correct() is 5

    def test_element_select(self):
        self.periodic_table.element_select(6)
        assert self.periodic_table.element_url == "https://en.wikipedia.org/wiki/Carbon"
        assert self.periodic_table.element_title['text'] == "       Element " + '6' + "       "

    def test_update_table(self):
        self.periodic_table.table_window('TimeTrial')
        test_update_root = Tk()
        self.periodic_table.timer = tt.Timer(test_update_root)
        assert pt.element8['text'] == "?"
        self.periodic_table.update_table('Oxygen', [])
        assert pt.element8['text'] == "O"
