from flask import *
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/identify', methods=['GET', 'POST'])
def id():
    if request.method == 'POST':
        if request.form['code']=="238413":
            return "ICED{this_i$_me!!!}"
        else:
            return "238413"
    else:
        return "Method not allow"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
