from flask import *
import sys
import sqlalchemy

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
@app.route('/info')
def info_page():
    return render_template('about.html')







if __name__ == "__main__":
    app.run(debug=True)