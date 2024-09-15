from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/student')
def select():
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

if __name__ == '__main__':
   app.run(debug = True)