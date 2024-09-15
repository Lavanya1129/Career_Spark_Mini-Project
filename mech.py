from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import os
import pymysql

app = Flask(__name__)

def sql_connector():
    conn = pymysql.connect(user='root', password='12345678', db='companies', host='localhost')
    c = conn.cursor()
    return conn, c

@app.route('/')
def home():
    conn, c = sql_connector()
    c.execute("SELECT * FROM mech;")
    company_data = c.fetchall()  # Fetch all rows
    conn.close()

    return render_template('rmech.html', company_data=company_data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.config['UPLOAD_FOLDER'] = 'uploads'


uploads_folder = 'uploads'

# Check if the 'uploads' folder exists; if not, create it
if not os.path.exists(uploads_folder):
    os.makedirs(uploads_folder)


   

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
    app.run(debug=True)
