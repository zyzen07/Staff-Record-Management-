from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Selva@1234",
    database="srikrish",
    raise_on_warnings=True
)
cursor = db.cursor()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_staff', methods=['POST'])
def add_staff():
    name = request.form['name']
    organization = request.form['organization']
    coursework = request.form['coursework']
    achievement = request.form['achievement']
    qualification = request.form['qualification']
    current_activity = request.form['current_activity']
    special_mention = request.form['special_mention']

    cursor.execute("""
        INSERT INTO staff (name, organization, coursework, achievement, qualification, current_activity, special_mention)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, organization, coursework, achievement, qualification, current_activity, special_mention))
    db.commit()
    return redirect(url_for('view_staff'))

@app.route('/view_staff')
def view_staff():
    cursor.execute("SELECT * FROM staff")
    staff_records = cursor.fetchall()
    return render_template('view_staff.html', staff_records=staff_records)

@app.route('/delete_staff/<int:id>')
def delete_staff(id):
    cursor.execute("DELETE FROM staff WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('view_staff'))

@app.route('/edit_staff/<int:id>', methods=['POST'])
def edit_staff(id):
    name = request.form['name']
    organization = request.form['organization']
    coursework = request.form['coursework']
    achievement = request.form['achievement']
    qualification = request.form['qualification']
    current_activity = request.form['current_activity']
    special_mention = request.form['special_mention']

    cursor.execute("""
        UPDATE staff
        SET name=%s, organization=%s, coursework=%s, achievement=%s, qualification=%s, current_activity=%s, special_mention=%s
        WHERE id=%s
    """, (name, organization, coursework, achievement, qualification, current_activity, special_mention, id))
    db.commit()
    return redirect(url_for('view_staff'))

if __name__ == '__main__':
    app.run(debug=True)



















