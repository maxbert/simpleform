from flask import Flask, render_template, request, url_for,redirect,session#look at data in request
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
app.secret_key = 'a'
readfile()
@app.route("/")
def hey():
    if 'user' not in session:
        return(render_template('form.html'))
    else:
        return (render_template('sess.html', user = session['user']))
@app.route("/authenticate/", methods=["POST",'GET'])
def check():
    print request.form
    if 'login' in request.form:
        return(aut())
    else:
        return reg()

    
def aut():
    readfile()
    u= request.form['user']
    n= request.form['pass']
    if u in USERS.keys() and (USERS[u] == str(hashlib.md5(n).hexdigest())):
        session['user'] = u
        return (redirect(url_for('hey')))
    else:
        return (render_template('ok.html', message="access denied"))

def reg():
    u= request.form['user']
    n= request.form['pass']
    a = open("data/names.csv", "r+")
    x = a.read()
    #x = x + ("\n" + u + "," + n)
    if(u not in USERS.keys()):
        a.write("\n"+ u + "," + str(hashlib.md5(n).hexdigest()))
        a.close()
        return ('registered succesfully, login <a href="'+url_for('hey')+'"> here </a>')
    else:
        return ('name taken')

@app.route('/logout/')
def lo():
    while 'user' in session.keys():
        session.pop('user')
    return (redirect(url_for('hey')))



if __name__ == "__main__":
    app.debug = True
    app.run()
        
