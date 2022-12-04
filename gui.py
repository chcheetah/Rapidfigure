from pathlib import Path
from tkinter import *
from apifetcher import *
var = "                   CS F301 Principles of Programming Language\n\n               \n                 RapidFigure, an Instagram backend simulator\n                  built using Python 3, Tkinter and Pandas.\n\n                                        Made By:\n\n                  Harshiv Chandra                     2020A7PS0085U\n                  Protik Mitra                              2020A7PS0113U\n                  Muhib Ahmed                          2020A7PS0167U\n\n                                         Made for:\n\n                Dr. Pranav M. Pawar                  Professor, PoPL\n\n  "
class app():
    def logout(app, pagehandler):
        logout = Tk()
        logout.title("Warning")
        logout.geometry("250x100")
        logout.resizable(False,False)
        logout.configure(bg="#000000")
        Label(logout, text = "Are you sure you want to logout?", bg = "#000000",fg = "#FFFFFF").pack()
        Button(logout, text = "Yes", bg = "#FFDA00", fg = "#000000",command = lambda: app.multidestroyer(logout,pagehandler)).pack(side=LEFT, expand=YES)
        Button(logout, text = "No", bg = "#FFDA00", fg = "#000000",command = lambda: logout.destroy()).pack(side=RIGHT, expand=YES)
        logout.mainloop()
    def multidestroyer(app, *args):
        for i in args:
          i.destroy()
    def login(app):
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
            file="assets/frame0/image_1.png")
        image_1 = canvas.create_image(
            350.0,
            243.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file="assets/frame0/image_2.png")
        image_2 = canvas.create_image(
            159.04525756835938,
            347.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file="assets/frame0/image_3.png")
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

        button_image_1 = PhotoImage(file="assets/frame0/right-chevron.png")
        button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,bg="#494949",command=lambda: print("login function invoked"),relief="flat")
        button_1.place(x=127.0,y=402.0, width=44.0,height=43.0)
        button_image_2 = PhotoImage(
            file="assets/frame0/right-chevron.png")
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
            file="assets/frame0/info.png")
        button_3 = Button(
            image=button_image_3,
            bg="#000000",
            relief = FLAT,
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda: app.aboutpg(),
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
    def aboutpg(app):
        infom = Tk()
        infom.title('About This App')
        infom.geometry("400x300")
        infom.configure(bg = "#000000")
        canvas = Canvas(infom,bg = "#000000",height = 300,width = 400)
        canvas.place(x = 0, y = 0)
##        image_image_1 = PhotoImage(file="assets/image_1.png")
##        image_1 = canvas.create_image(200.0,150.0,image=image_image_1)
        canvas.create_text(8.0,16.0,anchor="nw",
            text=var,
            fill = "#FFFFFF",
            font=("Inter", 12 * -1)
        )
        button_1 = Button(infom,text = "Go Back",command=lambda: infom.destroy())
        button_1.place(x=168.0,y=268.0,width=65.0,height=21.0)
        infom.resizable(False, False)
        infom.mainloop()
    def profile_pg(app,userid):
        d = extendedapi()
        r = d.fetchuser(userid,'userid')
        print(r)
        friendcount = len(r['followerid'].strip("[]").split(","))
        postcount = len(r['postids'].strip("[]").split(","))
        profilepg = Tk()
        profilepg.title("Profile Page")
        profilepg.geometry("700x487")
        profilepg.configure(bg = "#000000")
        canvas = Canvas(
            profilepg,
            bg = "#000000",
            height = 487,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            168.0,
            -1.0,
            169.0,
            487.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            13.0,
            12.0,
            anchor="nw",
            text="RapidFigure",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        canvas.create_rectangle(
            170.0,
            156.0,
            700.0,
            158.0,
            fill="#FFFFFF",
            outline="")

        ## profile name
        canvas.create_text(
            371.0,
            35.0,
            anchor="nw",
            text=" "+r['username'],
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        ## friend count & Post count
        canvas.create_text(
            414.0,
            66.0,
            anchor="nw",
            text=" "+str(friendcount)+" Friends - "+str(postcount)+" Posts",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        image_image_1 = PhotoImage(
            file="Images/Profile/"+r['profilepic'])
        image_1 = canvas.create_image(
            262.0,
            75.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file="assets/home.png")
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            text= "\t Home",
            bg = "#000000",
            fg = "#FFFFFF",
            compound = LEFT,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=12.0,
            y=157.0,
            width=143.0,
            height=38.0
        )

        button_image_2 = PhotoImage(
            file="assets/user.png")
        button_2 = Button(
            image=button_image_2,
            text = "\tProfile",
            borderwidth=0,
            bg = "#000000",
            fg = "#FFFFFF",
            compound = LEFT,
            highlightthickness=0,
            command=lambda: print("profile"),
            relief="flat"
        )
        button_2.place(
            x=12.0,
            y=199.0,
            width=143.0,
            height=38.0
        )

        button_image_3 = PhotoImage(
            file="assets/log-out.png")
        button_3 = Button(
            text="\tLog out",
            image = button_image_3,
            bg = "#000000",
            fg = "#FFFFFF",
            borderwidth=0,
            compound = LEFT,
            highlightthickness=0,
            command=lambda: app.logout(profilepg),
            relief="flat"
        )
        button_3.place(
            x=12.0,
            y=241.0,
            width=143.0,
            height=38.0
        )

        button_image_5 = PhotoImage(
            file="assets/info.png")
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg = "#000000",
            command=lambda: app.aboutpg(),
            relief="flat"
        )
        button_5.place(
            x=67.0,
            y=53.0,
            width=33.0,
            height=34.0
        )

        image_image_2 = PhotoImage(
            file="assets/frame0/image_2.png")

        frame1 = Frame(profilepg)
        image_2 = canvas.create_window(
            435.0,
            340.0,
            window = frame1,
            width = 529,
            height = 287
        )

        canvas2 = Canvas(
            frame1,
            bg = "#000000",
            height = 287,
            width = 529,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas2.place(x=0,y=0)
        postbw_1 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_1 = Button(frame1,
            image=postbw_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post 1 clicked"),
            relief="flat"
        )
        postb_1.place(
            x=53.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_2 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_2 = Button(frame1,
            image=postbw_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post 3 clicked"),
            relief="flat"
        )
        postb_2.place(
            x=337.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_3 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_3 = Button(frame1,
            image=postbw_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post 2 clicked"),
            relief="flat"
        )
        postb_3.place(
            x=195.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_4 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_4 = Button(frame1,
            image=postbw_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("postb_4 clicked"),
            relief="flat"
        )
        postb_4.place(
            x=53.0,
            y=150.0,
            width=139.0,
            height=136.0
        )

        postbw_5 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_5 = Button(frame1,
            image=postbw_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("postb_5 clicked"),
            relief="flat"
        )
        postb_5.place(
            x=337.0,
            y=150.0,
            width=139.0,
            height=136.0
        )

        postbw_6 = PhotoImage(
            file="assets/frame0/sp3.png")
        postb_6 = Button(frame1,
            image=postbw_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("postb_6 clicked"),
            relief="flat"
        )
        postb_6.place(
            x=195.0,
            y=150.0,
            width=139.0,
            height=136.0
        )
        canvas.create_text(
            436.0,
            87.0,
            anchor="nw",
            text=r['location'],
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        button_image_6 = PhotoImage(
            file='assets/posts.png')
        button_6 = Button(
            image=button_image_6,
            text = "\t My Posts",
            borderwidth=0,
            bg = "#000000",
            fg = "#FFFFFF",
            compound = LEFT,
            
            highlightthickness=0,
            command=lambda: print("My Posts"),
            relief="flat"
        )
        button_6.place(
            x=171.0,
            y=158.0,
            width=264.0,
            height=41.0
        )

        button_image_7 = PhotoImage(
            file='assets/saved.png')
        button_7 = Button(
            image=button_image_7,
            text = "\t Saved Posts",
            borderwidth=0,
            bg = "#000000",
            fg = "#FFFFFF",
            highlightthickness=0,
            compound = LEFT,
            command=lambda: print("Disabled - will implement later."),
            relief="flat"
        )
        button_7.place(
            x=436.0,
            y=158.0,
            width=264.0,
            height=41.0
        )

        canvas.create_text(
            41.0,
            440.0,
            anchor="nw",
            text="PoPL Edition",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )
        profilepg.resizable(False, False)
        profilepg.mainloop()
##    def loginpg(app):
##
##    def post_pg(app,postid):
        
