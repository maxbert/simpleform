from flask import Flask, render_template, request#look at data in request


app = Flask(__name__)

@app.route("/")
def hey():
    print request
    print request.headers
    return(render_template('form.html'))
@app.route("/authenticate/", methods=["POST"])
def aut():
    u= request.form['user']
    n= request.form['pass']
    if (u == 'max') and (n == 'password123'):
        return ('youre in<p>' + u + ' is your name &' + n + ' is your password')
    else:
        return('get out')
if __name__ == "__main__":
    app.debug = True
    app.run()
