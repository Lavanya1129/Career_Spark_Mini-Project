from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Assume you have a user database or some way to validate login credentials
def is_valid_login(email, password):
   
    return email == 'r190208@rguktrkv.ac.in' and password == '12345678'

@app.route('/')
def home():
    return render_template('loginPage.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if is_valid_login(email, password):
            # Successful login, redirect to the home page or some other page
            return redirect(url_for('loginPage'))
        else:
            # Invalid login, show an error message or redirect to the login page
            return render_template('loginPage.html', error='Invalid login credentials')

if __name__ == '__main__':
    app.run(debug=True)
