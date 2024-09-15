from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


def sql_connector():
    conn = pymysql.connect(user='root', password='12345678', db='sample', host='localhost')
    c = conn.cursor()
    return conn, c

@app.route('/signup', methods=['GET','POST'])
def signup():
    # Retrieve form data
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        gender = request.form.get('gender')
        branch = request.form.get('branch')
        gmail = request.form.get('gmail')
        password = request.form.get('password')
        cgpa = request.form.get('cgpa')
        college_name = request.form.get('collegeName')
        phone_number = request.form.get('phoneNumber')
        profile_photo = request.form.get('profilePhoto')

        conn, c = sql_connector()
        c.execute("INSERT INTO signup VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
          (first_name, last_name, gender, branch, gmail, password, float(cgpa), college_name, phone_number,profile_photo))
        conn.commit()
        conn.close()
    
    return render_template('signup.html')

     # Redirect to a success page





 # Set a secret key for session security

# ... (Your existing code)


    # ... (Your existing code)

    # Store user details in the session after successful signup
      # Redirect to a success page


if __name__ == '__main__':
    app.run(debug=True)

