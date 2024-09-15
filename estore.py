from flask import Flask, render_template, request
import os
import pymysql



def sql_connector():
    conn = pymysql.connect(user='root', password='12345678', db='companies', host='localhost')
    c = conn.cursor()
    return conn, c

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        logo = request.files.get('c_logo')
        name = request.form.get('c_name')
        overview = request.form.get('c_overview')
        website = request.form.get('c_website')
        industry = request.form.get('c_industry')
        size = request.form.get('c_size')
        headquarters = request.form.get('c_headquarters')
        founded = request.form.get('c_founded')
        specialities = request.form.get('c_specialities')
        turnover = request.form.get('c_turnover')



        uploads_folder = 'uploads'
        if not os.path.exists(uploads_folder):
            os.makedirs(uploads_folder)

        logo_path = os.path.join(uploads_folder, logo.filename)
        logo.save(logo_path)
        
        
        conn, c = sql_connector()


        c.execute("INSERT INTO eee (c_logo, c_name, c_overview, c_website, c_industry, c_size, c_headquarters, c_founded, c_specialities, c_turnover) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                  (logo_path, name, overview, website, industry, size, headquarters, founded, specialities, turnover))
        
        
       
        conn.commit()
        conn.close()
        c.close()
    return render_template('company.html')

if __name__ == '__main__':
    app.run(debug=True)
