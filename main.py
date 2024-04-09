from tkinter import *
from mile_to_kilometers import MileToKilometers


def main():
    window = Tk()
    window.title("Miles to Kilometer Converter")
    window.config(padx=20, pady=20)
    MileToKilometers()
    window.mainloop()


if __name__ == "__main__":
    main()
