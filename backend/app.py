from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        doctor = request.form['doctor']
        appointments.append({'name': name, 'doctor': doctor})
        return redirect(url_for('index'))
    return render_template('index.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)