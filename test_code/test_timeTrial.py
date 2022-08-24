from unittest import TestCase
from main_code.time_trial import Timer
from main_code.periodic_table import PeriodicTable
from tkinter import *


class TestTimer(TestCase):
    def setUp(self):
        test_timer_root = Tk()
        test_timer_frame = Frame(test_timer_root)
        self.timer = Timer(test_timer_frame)
        self.periodic_table = PeriodicTable()

    def test_add_time(self):
        assert self.timer.remaining == 29
        self.timer.add_time()
        assert self.timer.remaining == 34

    def test_countdown(self):
        self.timer.countdown(50)
        assert self.timer.remaining is 49
        self.timer.countdown()
        assert self.timer.remaining is 48
        self.timer.countdown(5)
        assert self.timer.label['bg'] == 'red'
        self.timer.countdown(10)
        assert self.timer.label['bg'] == 'gold'

    def test_close_timer(self):
        self.timer.close_timer()
        assert self.timer.remaining is -1

    def test_get_time(self):
        assert self.timer.get_time() is 29
