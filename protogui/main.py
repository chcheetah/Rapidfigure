from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from about import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
loginf = Tk()
loginf.title('Welcome')
loginf.geometry("700x487")
loginf.configure(bg = "#FFFFFF")
canvas = Canvas(
    loginf,
    bg = "#FFFFFF",
    height = 487,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    243.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    159.04525756835938,
    347.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    159.0,
    262.0,
    image=image_image_3
)

canvas.create_text(
    248.0,
    102.0,
    anchor="nw",
    text="RapidFigure",
    fill="#FFFFFF",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    468.0,
    244.0,
    anchor="nw",
    text="New User?",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    349.0,
    236.0,
    350.0,
    455.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(file=relative_to_assets("right-chevron.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,bg="#494949",command=lambda: print("login function invoked"),relief="flat")
button_1.place(x=127.0,y=402.0, width=44.0,height=43.0)
button_image_2 = PhotoImage(
    file=relative_to_assets("right-chevron.png"))
button_2 = Button(
    image=button_image_2,bg="#000000",
    relief = FLAT,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("signup function invoked"),
)
button_2.place(
    x=503.0,
    y=293.0,
    width=44.0,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("info.png"))
button_3 = Button(
    image=button_image_3,
    bg="#000000",
    relief = FLAT,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda: aboutgui(),
)
button_3.place(
    x=652.0,
    y=7.0,
    width=36.0,
    height=34.0
)

canvas.create_text(
    64.0,
    244.0,
    anchor="nw",
    text="User",
    fill="#FFFFFF",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    64.0,
    327.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter", 10 * -1)
)
username = ""
password = ""
usernm = Entry(loginf, relief = FLAT,highlightcolor='green',
    borderwidth=0,
    highlightthickness=0,border = 0 ,textvariable = username, bg = "#909090",fg = "white")
pw = Entry(loginf,relief = FLAT,highlightcolor='green',
             borderwidth=0,
    highlightthickness=0,border = 0,textvariable = password,show="*", bg = "#909090",fg = "white")
usernm.place(
    x = 48.0,
    y = 263.0,
    w =  222.0,
    h = 20.0)
#    fill="#D9D9D9",
 #   outline="")
pw.place(
    x = 48.0,
    y = 347.0,
    w = 222.0,
    h = 20.0)
 #   fill="#D9D9D9",
  #  outline="")


loginf.resizable(False, False)
loginf.mainloop()
