from flask import Flask, render_template,redirect, session,request 
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def home():
    if 'number' and 'guess' not in session:
        session['number']=random.randint(1,100)
        session['guess']=0
    if "count" not in session:
        session['count'] = 0
    return render_template("try.html", count=session['count'])

@app.route('/guess', methods=['POST'] )
def guess():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    if request.method == "POST":
        session['guess'] = int(request.form['input'])
        return redirect ('/check')

@app.route('/check')
def check():
    if session['count'] ==5:
        return render_template('lose.html')
    if session['guess'] > session['number']:
        return render_template ('tooHigh.html')
    if session['guess'] < session['number']:
        return render_template('tooLow.html')
    if session['guess'] == session['number']:
        return render_template('correct.html')
    

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'


if __name__ == "__main__":
    app.run(debug=True)