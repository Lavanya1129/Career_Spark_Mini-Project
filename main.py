
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/about_rgukt')
def about_rgukt():
    return render_template('RGUKT.html')

@app.route('/placement_policy')
def placement_policy():
    return render_template('Policy.html')

@app.route('/rules_and_regulations')
def rules_and_regulations():
    return render_template('Rules.html')

@app.route('/placement_records')
def placement_records():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
