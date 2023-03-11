from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret_key'

# connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",
  database="team_13"
)

# define a route to display the e-learning courses
@app.route('/courses')
def courses():
    # fetch courses from the database
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

# define a route to display a specific course
@app.route('/course/<int:id>')
def course(id):
    # fetch course details from the database
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM courses WHERE id=%s", (id,))
    course = cursor.fetchone()
    
    # check if the user is a student and has registered for the course
    if 'user_id' in session and session['user_type'] == 'student':
        student_id = session['user_id']
        cursor.execute("SELECT * FROM registrations WHERE student_id=%s AND course_id=%s", (student_id, id))
        registration = cursor.fetchone()
        if registration:
            return render_template('course.html', course=course, registered=True)
    
    # if the user is not registered for the course, redirect to the registration page
    return redirect('/register/'+str(id))

# define a route to register for a course
@app.route('/register/<int:id>', methods=['GET', 'POST'])
def register(id):
    # check if the user is a student and is logged in
    if 'user_id' in session and session['user_type'] == 'student':
        student_id = session['user_id']
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM registrations WHERE student_id=%s AND course_id=%s", (student_id, id))
        registration = cursor.fetchone()
        if registration:
            # if the user is already registered, redirect to the course page
            return redirect('/course/'+str(id))
        else:
            # if the user is not registered, process the registration form
            if request.method == 'POST':
                # insert the registration into the database
                cursor.execute("INSERT INTO registrations (student_id, course_id) VALUES (%s, %s)", (student_id, id))
                mydb.commit()
                # redirect to the course page
                return redirect('/course/'+str(id))
            else:
                # display the registration form
                return render_template('register.html', course_id=id)
    else:
        # if the user is not a student or is not logged in, redirect to the login page
        return redirect('/login')

# define a route to display the mentor dashboard
@app.route('/dashboard')
def dashboard():
    # check if the user is a mentor and is logged in
    if 'user_id' in session and session['user_type'] == 'mentor':
        mentor_id = session['user_id']
        # fetch the courses that the mentor has uploaded
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM courses WHERE mentor_id=%s", (mentor_id,))
        courses = cursor.fetchall()
        return render_template('dashboard.html', courses=courses)
    else:
        # if the user is not a mentor or is not logged in, redirect to the login page
        return redirect('/login')

# define a route to upload a course
@app.route('/upload_course', methods=['GET', 'POST'])
def upload_course():
    # check if the user is a mentor and is logged in
    if 'user_id' in session and session['user_type'] == 'mentor':
        mentor_id = session['user_id']
        if request.method == 'POST':
            # get the form data
            title = request.form['title']
            description = request.form['description']
            price = request.form['price']
            # insert the course into the database
            cursor = mydb.cursor()
            cursor.execute("INSERT INTO courses (title, description, price, mentor_id) VALUES (%s, %s, %s, %s)", (title, description, price, mentor_id))
            mydb.commit()
            # redirect to the mentor dashboard
            return redirect('/dashboard')
        else:
            # display the upload course form
            return render_template('upload_course.html')
    else:
        # if the user is not a mentor or is not logged in, redirect to the login page
        return redirect('/login')