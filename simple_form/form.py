from flask import Flask, render_template, request, url_for,redirect#look at data in request
import hashlib
USERS = {}
def readfile():
    a = open("data/names.csv", "r")
    b = a.read().split("\n")
    for i in range(len(b)):
        if(b != ""):
            USERS[b[i].split(",")[0]] = b[i].split(",")[1]
    a.close()
app = Flask(__name__)
readfile()
@app.route("/")
def hey():
    print request
    print request.headers
    return(render_template('form.html'))
@app.route("/authenticate/", methods=["POST"])
def check():
    if "login" in request.form:
            return(aut())
    else:
        return((reg()))

    
def aut():
    readfile()
    u= request.form['user']
    n= request.form['pass']
    if (u in USERS.keys()) and (USERS[u] == str(hashlib.md5(n).hexdigest())):
        session[user] = u
        return (redirect(url_for('ine')))
    else:
        return ("incorrect")

def reg():
    u= request.form['user']
    n= request.form['pass']
    a = open("data/names.csv", "r+")
    x = a.read()
    #x = x + ("\n" + u + "," + n)
    if(u not in USERS.keys()):
        a.write("\n"+ u + "," + str(hashlib.md5(n).hexdigest()))
        a.close()
        return (redirect(url_for('hey')) )
    else:
        return ('name taken')


if __name__ == "__main__":
    app.debug = True
    app.run()
@app.route("/ine/")
def ine():
    if user in session.keys():
        return('in')
    else:
        return('out')
           
        
