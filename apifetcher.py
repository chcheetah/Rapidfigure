# Basic database functions
import pandas as p
class baseapi():
    def __init__(api):
        api.key = "0000"
        api.link = "www.example.com"
    def fetchlogin(api):
        fp = "Data/Login.csv"
        d = p.read_csv(fp, sep=",")
        return d
    def fetchpost(api,postid=""):
        if(postid == ""):
            return {"text":"unable to fetch content"}
        fp = "Data/Post.csv"
        d = p.read_csv(fp,sep=",")
        d = d.set_index('postid')
        d = d.T.to_dict()
        o = d.keys()
        if(postid not in o):
            return {"present":False}
        e = d[postid]
        e["present"] = True
        return e
    def fetchuser(api,userid="",search=""):
        if(userid == "" or search==""):
            return {"text":"unable to fetch content"}
        fp = "Data/User.csv"
        d = p.read_csv(fp,sep=",")
        d = d.set_index(search)
        d = d.T.to_dict()
        o = d.keys()
        if(userid not in o):
            return {"present":False}
        # must set return dictionary value to True for present key
        e = d[userid]
        e["present"] = True
        return e
    def fetchcomment(api,postid="",param="",search=""):
        fp = "Data/Comment.csv"
        com = []
        d = p.read_csv(fp,sep=",")
        if(postid=="" or search==""):
            return {"text":"unable to fetch content"}
        elif(search != "all"):
            d = d.set_index(search)
        else:
            d = d.set_index("commentid")
        d = d.T.to_dict()
        o = d.keys()
        for i in d.keys():
            if (d[i]['postid']==postid):
                com.append(d[i])
                continue
        return com
        
class extendedapi(baseapi):
    def isblocked(api,userid):
        r = api.fetchuser(userid)
        if(r['isblocked'] == "True"):
            return True
        return False
    def lastlogin(api,userid):
        r = api.fetchuser(userid)
        return r['lastlogin']
    def userexists(api,username):
        r = api.fetchuser(username,'username')
        if(r["present"]):
            return True
        return False
    def postexists(api,postid):
        r = api.fetchpost(postid,'postid')
        if(r["present"]):
            return True
        return False

d = extendedapi()
m = d.fetchuser(83930,'userid')
        
