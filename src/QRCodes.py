
# Part of this file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\logan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\build\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class QRCodes(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.photoList = []
        self.loadWidgets()
        
    def loadWidgets(self):  
        canvas = Canvas(
            self,
            bg = "#153246",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        
        self.photoList.append(image_image_1)
        
        image_1 = canvas.create_image(
            640.0,
            360.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        
        self.photoList.append(image_image_2)
        
        image_2 = canvas.create_image(
            639.333984375,
            359.333984375,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        
        self.photoList.append(image_image_3)
        
        image_3 = canvas.create_image(
            88.0,
            90.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        
        self.photoList.append(image_image_4)
        
        image_4 = canvas.create_image(
            421.0,
            360.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        
        self.photoList.append(image_image_5)
        
        image_5 = canvas.create_image(
            859.0,
            360.0,
            image=image_image_5
        )

        canvas.create_text(
            335.0,
            551.0,
            anchor="nw",
            text="Website",
            fill="#F5F0E6",
            font=("Montserrat", 40 * -1)
        )

        canvas.create_text(
            788.0,
            557.0,
            anchor="nw",
            text="Waiver",
            fill="#F5F0E6",
            font=("Montserrat", 40 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        
        self.photoList.append(image_image_6)
        
        image_6 = canvas.create_image(
            88.0,
            90.0,
            image=image_image_6
        )