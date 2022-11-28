from pymongo import *

class dbcontroller():
    def __init__(self):
        # establishes a basic set of params needed to check into the database;
    def fetchpost(self,p_id):
        # fetches post details from the database
    def fetchcomment(self,c_id):
        #fetches comments from the database
    def fetchpcomm(self,p_id):
        #fetches post's comments from database
    def fetchusr(self,u_id):
        # fetches user using u_id from database
    

class mediacontroller():
    def __init__(self, u_id, p_id):

    def isvaliduser(u_id):
        # checks to see if user is valid, and compares post id to user id
    def push(self, media, u_id):
        # pushes some stuff to a random cloud store,
    def pull(self, media):
        if(self.isvaliduser(u_id, p_id)):
            return True
        return False
        # retrives items from the datastore
    
class login():
    def __init__(self,user,passw):
    def isvalidcreds(self):
        try(return True)except(return False)
        # if valid creds, returns true - if invalid login return false
    def auth(self):
        if(self.isvalidcreds()):
            # return session using the given credentials
        
class user():
    def __init__(self,u_id,*args):
        self.posts = args
        s
    def profile(self): # just a handler function that returns a profile pg of a user.
        return [dict(self.posts),friendcount]
    def friendship(self,
class post():
    def __init__(self,p_id):
        self.p_id = p_id
    def show(self):
        # r = dbcontroller()
        # r = r.fetchpost(self.p_id)
        return dict(r)
    def publish(self,content):
        try(return True)except(return False)
        # r = dbcontroller()
        # r.publish(content) # must be organised in the format [text, image_url, video_url]
        # return True if complete and return False if any issue
    def delete(self):
        try(return True)except(return False)
        # r = dbcontroller()
        # r = r.remove(p_id)
        # return True if complete and return False if any issue
    def like(self): # increment like count

class comment():
    def __init__(self, p_id, c_id, u_id):
    def fetch(self,c_id):
        return [p_id, u_id, commenttext,likes]
    def delete(self,c_id):
        # r = dbcontroller()
        # r = remove(c_id)


# all backend stuff defined.
