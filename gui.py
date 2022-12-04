from tkinter import *
from tkinter import ttk
from apifetcher import *
import time
import threading
var = "                   CS F301 Principles of Programming Language\n\n               \n                 RapidFigure, an Instagram backend simulator\n                  built using Python 3, Tkinter and Pandas.\n\n                                        Made By:\n\n                  Harshiv Chandra                     2020A7PS0085U\n                  Protik Mitra                              2020A7PS0113U\n                  Muhib Ahmed                          2020A7PS0167U\n\n                                         Made for:\n\n                Dr. Pranav M. Pawar                  Professor, PoPL\n\n  "
d = extendedapi()

class check():
    # future implementation of a loading animation
    def animation(check):
        check.Rp = Tk()
        check.Rp.resizable(False,False)
        check.Rp.title('Loading...')
        check.Rp.configure(bg="#000000")
        pb = ttk.Progressbar(
            check.Rp,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
        pb.start()
        pb.pack()
        check.Rp.mainloop()
    def message(check, string):
        msg = Tk()
        msg.title("Warning")
        msg.geometry("250x100")
        msg.resizable(False,False)
        msg.configure(bg="#000000")
        Label(msg, text = string, bg = "#000000",fg = "#FFFFFF").pack()
        Button(msg, text= "Ok", bg = "#FFDA00", fg = "#000000", command = lambda:msg.destroy()).pack()
        msg.mainloop()
    def existencecheck(check,username):
        L = d.fetchuser(username,'username')
        if(L['present'] == False):
            check.message("This username does not exist! Try again!")
            return -1
        return 0
    def passwordcheck(check, username, password):
        L = d.fetchuser(username,'username')
        Lm = d.fetchlogin(L['userid'],'userid')
        if(Lm['password'].strip('""') != password):
            check.message("This password is wrong! Try again!")
            return -1
        return 0
    def blockcheck(check, username):
        L = d.fetchlogin(username,'username')
        if(L['isblocked'] == True):
            check.message("This user has been blocked for" + L['reasonBlocked'])
            return -1
        return 0

    def logcbar(check,username,password,pagehandler):
##        check.t1 = threading.Thread(target=check.animation)    future implementation of a loading animation
##        check.t2 = threading.Thread(target=check.logincheck(username,password,pagehandler))
##        check.t1.start()
##        check.t2.start()
        check.logincheck(username, password, pagehandler)
    def logincheck(check,username,password,pagehandler):
        health = check.existencecheck(username)
        if(health == -1):
            return None
        pwchk = check.passwordcheck(username,password)
        if(pwchk == -1):
            return None
        blockstat = check.blockcheck(username)
        if(blockstat == -1):
            return None
        ff = d.fetchuser(username, 'username')['userid']
        pagehandler.withdraw()
        app().profile_pg(ff, pagehandler)

class app():
    def logout(app, pagehandler,pg2):
        logout = Tk()
        logout.title("Warning")
        logout.geometry("250x100")
        logout.resizable(False,False)
        logout.configure(bg="#000000")
        Label(logout, text = "Are you sure you want to logout?", bg = "#000000",fg = "#FFFFFF").pack()
        Button(logout, text = "Yes", bg = "#FFDA00", fg = "#000000",command = lambda: app.multidestroyer(logout,pagehandler,pg2)).pack(side=LEFT, expand=YES)
        Button(logout, text = "No", bg = "#FFDA00", fg = "#000000",command = lambda: logout.destroy()).pack(side=RIGHT, expand=YES)
        logout.mainloop()
    def multidestroyer(app, *args):
        for i in range(len(args)-1):
          args[i].destroy()
        args[len(args)-1].update()
        args[len(args)-1].deiconify()
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
            file="assets/frame0/image_1.png", master=loginf)
        image_1 = canvas.create_image(
            350.0,
            243.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file="assets/frame0/image_2.png", master=loginf)
        image_2 = canvas.create_image(
            159.04525756835938,
            347.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file="assets/frame0/image_3.png", master=loginf)
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

        button_image_1 = PhotoImage(file="assets/frame0/right-chevron.png", master=loginf)
        button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,bg="#494949",command=lambda: check().logincheck(usernm.get(),pw.get(),loginf),relief="flat")
        button_1.place(x=127.0,y=402.0, width=44.0,height=43.0)
        button_image_2 = PhotoImage(
            file="assets/frame0/right-chevron.png", master=loginf)
        button_2 = Button(
            image=button_image_2,bg="#000000",
            relief = FLAT,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ("signup function invoked"),
        )
        button_2.place(
            x=503.0,
            y=293.0,
            width=44.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file="assets/frame0/info.png", master=loginf)
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
        image_image_1 = PhotoImage(master=infom,file="assets/image_1.png")
        image_1 = canvas.create_image(200.0,150.0,image=image_image_1)
        canvas.create_text(8.0,16.0,anchor="nw",
            text=var,
            fill = "#FFFFFF",
            font=("Inter", 12 * -1)
        )
        button_1 = Button(infom,text = "Go Back",command=lambda: infom.destroy())
        button_1.place(x=168.0,y=268.0,width=65.0,height=21.0)
        infom.resizable(False, False)
        infom.mainloop()
    def profile_pg(app,userid,pagehandler):
        d = extendedapi()
        wr = d.fetchuser(userid,'userid')
        friends = wr['followerid'].strip("[]").split(",")
        posts = wr['postids'].strip("[]").split(",")
        friendcount = len(friends)
        postcount = len(posts)
        if(posts == ['']):
            postcount = 0
        if(friends == ['']):
            friendcount = 0
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
            text=" "+wr['username'],
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
            file="Images/Profile/"+wr['profilepic'], master=profilepg)
        image_1 = canvas.create_image(
            262.0,
            75.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file="assets/home.png",master = profilepg)
        button_1 = Button(
            master = profilepg,
            image=button_image_1,
            borderwidth=0,
            text= "\t Home",
            bg = "#000000",
            fg = "#FFFFFF",
            compound = LEFT,
            highlightthickness=0,
            command=lambda: print("Home button clicked"),
            relief="flat"
        )
        button_1.place(
            x=12.0,
            y=157.0,
            width=143.0,
            height=38.0
        )

        button_image_2 = PhotoImage(
            file="assets/user.png",master=profilepg)
        button_2 = Button(
            master = profilepg,
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
            file="assets/log-out.png",master=profilepg)
        button_3 = Button(
            master = profilepg,
            text="\tLog out",
            image = button_image_3,
            bg = "#000000",
            fg = "#FFFFFF",
            borderwidth=0,
            compound = LEFT,
            highlightthickness=0,
            command=lambda: app.logout(profilepg,pagehandler),
            relief="flat"
        )
        button_3.place(
            x=12.0,
            y=241.0,
            width=143.0,
            height=38.0
        )

        button_image_5 = PhotoImage(
            file="assets/info.png",master=profilepg)
        button_5 = Button(
            master = profilepg,
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
            file="assets/frame0/image_2.png",master=profilepg)

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
            file="assets/frame0/sp1.png",master=profilepg)
        postb_1 = Button(frame1,
            image=postbw_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 1 clicked"),
            relief="flat"
        )
        postb_1.place(
            x=53.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_2 = PhotoImage(
            file="assets/frame0/sp2.png",master=profilepg)
        postb_2 = Button(frame1,
            image=postbw_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 3 clicked"),
            relief="flat"
        )
        postb_2.place(
            x=337.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_3 = PhotoImage(
            file="assets/frame0/sp3.png",master=profilepg)
        postb_3 = Button(frame1,
            image=postbw_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 2 clicked"),
            relief="flat"
        )
        postb_3.place(
            x=195.0,
            y=11.0,
            width=139.0,
            height=136.0
        )

        postbw_4 = PhotoImage(
            file="assets/frame0/sp4.png",master=profilepg)
        postb_4 = Button(frame1,
            image=postbw_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 4 clicked"),
            relief="flat"
        )
        postb_4.place(
            x=53.0,
            y=150.0,
            width=139.0,
            height=136.0
        )

        postbw_5 = PhotoImage(
            file="assets/frame0/sp5.png",master=profilepg)
        postb_5 = Button(frame1,
            image=postbw_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 6 clicked"),
            relief="flat"
        )
        postb_5.place(
            x=337.0,
            y=150.0,
            width=139.0,
            height=136.0
        )

        postbw_6 = PhotoImage(
            file="assets/frame0/sp6.png",master=profilepg)
        postb_6 = Button(frame1,
            image=postbw_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("post number 5 clicked"),
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
            text=wr['location'],
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        button_image_6 = PhotoImage(
            file='assets/posts.png',master=profilepg)
        button_6 = Button(
            master = profilepg,
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
            file='assets/saved.png',master=profilepg)
        button_7 = Button(
            master = profilepg,
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
##
##    def post_pg(app,postid):



        
