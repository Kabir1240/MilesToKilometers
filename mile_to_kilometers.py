from tkinter import *
from tkinter_widgets import TkinterWidgets


class MileToKilometers:
    def __init__(self):
        """
        initializes all widgets, and widget data structure to store them
        """
        self.widgets = TkinterWidgets()
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self) -> None:
        """
        creates necessary labels and stores them in widget data structure
        :return: None
        """
        label_1 = Label(text="Miles")
        label_2 = Label(text="is equal to")
        label_3 = Label(text="0")
        label_4 = Label(text="Km")
        label_1.grid(row=0, column=2)
        label_2.grid(row=1, column=0)
        label_3.grid(row=1, column=1)
        label_4.grid(row=1, column=2)

        label_dict = {
            "miles": label_1,
            "is equal to": label_2,
            "miles to km": label_3,
            "km": label_4
        }

        self.widgets.add_label_dict(label_dict=label_dict)

    def create_entries(self) -> None:
        """
        creates necessary entries and stores them in widget data structure
        :return: None
        """
        entry = Entry()
        entry.grid(row=0, column=1)
        entry["width"] = 10

        self.widgets.add_entry(key="entry", entry=entry)

    def create_buttons(self) -> None:
        """
        creates necessary buttons and stores them in widget data structure
        :return: None
        """
        button = Button(text="Calculate")
        button.grid(row=2, column=1)
        button["command"] = self.convert_miles_to_kilometers

        self.widgets.add_button(key="button", button=button)

    def convert_miles_to_kilometers(self) -> None:
        """
        converts miles to kilometers and displays it for the user
        :return: None
        """
        entry = self.widgets.get_entries("entry")
        label = self.widgets.get_labels("miles to km")

        miles = float(entry.get())
        label["text"] = round(miles * 1.6, 3)
