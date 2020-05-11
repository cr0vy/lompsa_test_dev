#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import requests


class MainWindow(Gtk.Window):
    stack = None

    month_widget = None

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title(title="Lompsa")
        self.set_size_request(800, 600)

        self.setup_widget()

    def setup_widget(self):
        self.stack = Gtk.Stack()
        self.month_widget = MonthlyWidget()

        self.stack.add_named(self.month_widget, "monthly")

        self.add(self.stack)


class MonthlyWidget(Gtk.Box):
    expenses_widget = None
    incomes_widget = None

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)

        self.setup_widget()
        self.get_month_json(5)

    def setup_widget(self):
        self.expenses_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.incomes_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.pack_start(self.incomes_widget, True, True, 5)
        self.pack_start(self.expenses_widget, True, True, 5)

    def get_month_json(self, month: int):
        url = "http://127.0.0.1:8000/month/" + str(month)
        r = requests.get(url)

        incomes_json = r.json()[0]
        expenses_json = r.json()[0]

        print(incomes_json, expenses_json)


def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
