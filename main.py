from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/resultpage')
def resultpage():
    username = request.args.get('username')
    up = 0
    lower =0
    digitcheck = False
    for letter in username:
        ascii = ord(letter)
        if (ascii>=65) & (ascii<=90):
            up = up +1
        elif (ascii>=97) & (ascii<=122):
            lower = lower + 1
    if (ord(username[-1])>=48) & (ord(username[-1])<=57):
        digitcheck = True
    return render_template('resultpage.html',username=username,up=up,lower=lower,digitcheck=digitcheck)

@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"),404

if __name__=='__main__':
    app.run(debug=True)
