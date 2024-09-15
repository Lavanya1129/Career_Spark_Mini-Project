from flask import Flask, render_template,request,session,redirect,url_for,session
import os
import pymysql


app = Flask(__name__)

app.secret_key = '123#245c/jkh#!' 

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/about_rgukt')
def about_rgukt():
    return render_template('RGUKT.html')


@app.route('/chat_bot')
def chat_bot():
    return render_template('chat.html')

@app.route('/placement_policy')
def placement_policy():
    return render_template('Policy.html')

@app.route('/rules_and_regulations')
def rules_and_regulations():
    return render_template('Rules.html')

@app.route('/placement_records')
def placement_records():
    return render_template('gallery.html')

@app.route('/internship')
def internship():
    return render_template('intern.html')


@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    contact=request.form['contact']
    fathername=request.form['fathername']
    address=request.form['address']
    residance=request.form['residance']
    dob=request.form['dob']
    lang=request.form['lang']
    gb=request.form['gb']
    gm=request.form['gm'] 
    gp=request.form['gp']
    gs=request.form['gs']

    
   
    tvm=request.form['tvm'] 

    
    projetcs=request.form['projects'] 
    skills=request.form['skills']
    achievements=request.form['achievements']   
    return render_template('cv.html', name=name, email=email,contact=contact,dob = dob, lang = lang, address = address, fathername = fathername, residance = residance,gp=gp,gs=gs,gm=gm,gb=gb,tvm=tvm,projetcs = projetcs, skills = skills, achievements = achievements)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result,css_file="print.css")







def sql_connector():
     conn = pymysql.connect(user='root', password='12345678', db='companies', host='localhost')
     c = conn.cursor()
     return conn, c

@app.route('/cse_route')
def cse():
        conn, c = sql_connector()
        c.execute("SELECT * FROM cse;")
        company_data = c.fetchall()  # Fetch all rows
        conn.close()

        return render_template('rcse.html', company_data=company_data)



@app.route('/ece_route')
def ece():
    conn, c = sql_connector()
    c.execute("SELECT * FROM ece;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('rece.html', company_data=company_data)



@app.route('/eee_route')
def eee():
    conn, c = sql_connector()
    c.execute("SELECT * FROM eee;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('reee.html', company_data=company_data)




@app.route('/chem_route')
def chem():
    conn, c = sql_connector()
    c.execute("SELECT * FROM chem;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('rchem.html', company_data=company_data)



@app.route('/mech_rpute')
def mech():
    conn, c = sql_connector()
    c.execute("SELECT * FROM mech;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('rmech.html', company_data=company_data)@app.route('/')


@app.route('/civil_route')
def civil():
    conn, c = sql_connector()
    c.execute("SELECT * FROM civil;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('rcivil.html', company_data=company_data)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.config['UPLOAD_FOLDER'] = 'uploads'


uploads_folder = 'uploads'

# Check if the 'uploads' folder exists; if not, create it
if not os.path.exists(uploads_folder):
    os.makedirs(uploads_folder)


#singup details
    
def sql_connect():
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
       

        conn, c = sql_connect()
        c.execute("INSERT INTO signup VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
          (first_name, last_name, gender, branch, gmail, password, float(cgpa), college_name, phone_number))
        conn.commit()
        conn.close()
    
        return redirect(url_for('login'))

    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('gmail')
        password = request.form.get('password')

        # Query the database to check if the user exists
        conn, c = sql_connect()
        c.execute("SELECT gmail, password FROM signup WHERE gmail = %s AND password = %s",
                  (email, password))
        result = c.fetchone()
        conn.close()

        if result:
            # User exists with the provided email and password
            email, password = result
            session['email'] = email
            session['password'] = password

            return redirect(url_for('main_page'))
        else:
            # No matching user found
            # Perform your login failure logic here
            error_message = "Username or Password Invalid."
            return render_template('loginPage.html', login_error_message=error_message)

    return render_template('loginPage.html')



# Add this route to your Flask app
@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'email' in session:
        # Fetch user details from the database using the stored email
        email = session['email']
        conn, c = sql_connect()
        c.execute("SELECT * FROM signup WHERE gmail = %s", (email,))
        user_data = c.fetchone()
        conn.close()

        if user_data:
            # Pass user data to the profile template
            return render_template('profile.html', user_data=user_data)
    
    # If user is not logged in or no data found, redirect to login
    return redirect(url_for('login'))






# Add this route to your Flask app
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('main_page'))


  
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
    app.run(debug=True)





