# main.py

from gui import create_gui


def run():
    app, entry_price, entry_rent, entry_occupancy, entry_interest, entry_years, summary_text, canvas, ax = create_gui()
    app.mainloop()


if __name__ == "__main__":
    run()
