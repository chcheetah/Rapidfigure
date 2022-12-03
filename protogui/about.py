from tkinter import *
var = "                   CS F301 Principles of Programming Language\n\n               \n                 RapidFigure, an Instagram backend simulator\n                  built using Python 3, Tkinter and Pandas.\n\n                                        Made By:\n\n                  Harshiv Chandra                     2020A7PS0085U\n                  Protik Mitra                              2020A7PS0113U\n                  Muhib Ahmed                          2020A7PS0167U\n\n                                         Made for:\n\n                Dr. Pranav M. Pawar                  Professor, PoPL\n\n  "
def aboutgui():
    infom = Tk()
    infom.title('about')
    infom.geometry("400x300")
    infom.configure(bg = "#000000")
    canvas = Canvas(infom,bg = "#FFFFFF",height = 300,width = 400)
    canvas.place(x = 0, y = 0)
    #image_image_1 = PhotoImage(file="assets\image_1.png")
    #image_1 = canvas.create_image(200.0,150.0,image=image_image_1)
    canvas.create_text(8.0,16.0,anchor="nw",
        text=var,
        font=("Inter", 12 * -1)
    )
    button_1 = Button(infom,text = "Go Back",command=lambda: infom.destroy())
    button_1.place(x=168.0,y=268.0,width=65.0,height=21.0)
    infom.resizable(False, False)
    infom.mainloop()
