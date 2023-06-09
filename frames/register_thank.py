
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\logan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#153244")


canvas = Canvas(
    window,
    bg = "#153244",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.33203125,
    359.3330078125,
    image=image_image_2
)

canvas.create_text(
    99.33203125,
    269.3330078125,
    anchor="nw",
    text="Thank you for registering",
    fill="#F5F0E6",
    font=("Montserrat", 45 * -1)
)

canvas.create_text(
    429.0,
    550.0,
    anchor="nw",
    text="UCSD Makerspace",
    fill="#F5F0E6",
    font=("Montserrat", 45 * -1)
)

canvas.create_text(
    99.0,
    323.0,
    anchor="nw",
    text="First Name and Last Name",
    fill="#F5F0E6",
    font=("Montserrat", 73 * -1)
)
window.resizable(False, False)
window.mainloop()
