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
    return(render_template('form.html', route = url_for('regg')))
@app.route("/authenticate/", methods=["POST"])
def aut():
    readfile()
    u= request.form['user']
    n= request.form['pass']
    if (u in USERS.keys()) and (USERS[u] == str(hashlib.md5(n).hexdigest())):
        return ('youre in<p>' + u + ' is your name &' + n + ' is your password')
    else:
        return redirect(url_for('regg'))
@app.route("/reg/register/", methods = ["POST"])
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
@app.route("/reg/")
def regg():
    return render_template('register.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
