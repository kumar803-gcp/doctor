from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
appointments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        doctor = request.form['doctor']
        specialization = request.form['specialization']
        issue = request.form['issue']
        days = request.form['days']
        symptoms = request.form['symptoms']

        appointments.append({
            'name': name,
            'doctor': doctor,
            'specialization': specialization,
            'issue': issue,
            'days': days,
            'symptoms': symptoms
        })

        return redirect(url_for('index'))

    return render_template('index.html', appointments=appointments)