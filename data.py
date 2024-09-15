from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'sample'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data from the request object
        gmail = request.form.get('gmail')
        password = request.form.get('password')

        # Retrieve email and password from the database
        cursor = conn.cursor()
        query = "SELECT gmail, password FROM signup WHERE gmail = %s"
        cursor.execute(query, (gmail,))
        result = cursor.fetchone()

        if result:
            stored_email, stored_password = result
            if password == stored_password:
                # Passwords match, redirect to success page
                return redirect(url_for('success'))
            else:
                # Passwords don't match, handle invalid login
                return "Invalid email or password"
        else:
            # Email not found in the database, handle invalid login
            return "Invalid email or password"

    # Render the signup form template
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('loginPage.html')

if __name__ == '__main__':
    app.run(debug=True)

