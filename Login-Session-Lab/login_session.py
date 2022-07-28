from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST']) 
def home():
	if request.method == 'POST':
		try:

			quote=request.form['Quote']
			name=request.form["Author's name"]
			age=request.form["Author's age"]
			login_session['Quote']=quote
			login_session["Author's name"]=name
			login_session["Author's age"]=age
			return render_template('thanks.html',quote= login_session['Quote'],name=login_session["Author's name"],age=login_session["Author's age"])
		except:
			return render_template('error.html')
	else:
		return render_template('home.html')

	






@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',quote= login_session['Quote'],name=login_session["Author's name"],age=login_session["Author's age"] ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)