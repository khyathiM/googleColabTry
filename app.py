from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) 

@app.route('/') 
def index():
    return render_template('form.html')


@app.route('/calculate', methods=['POST']) 
def calculate():

    number = int(request.form['number']) 
    result = number * 2 
    # return render_template('calculate.html', result=result) 
    return redirect(url_for("end"))

@app.route('/end')
def end():
    return render_template('calculate.html')


if __name__ == '__main__':
    app.run()
