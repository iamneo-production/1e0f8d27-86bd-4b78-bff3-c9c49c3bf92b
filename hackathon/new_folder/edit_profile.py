from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="examly",
    database="team_13"
)

# Define a function for updating user profile
def update_profile(username, name, email, mobile):
    cursor = mydb.cursor()
    sql = "UPDATE users SET name=%s, email=%s, mobile=%s WHERE username=%s"
    val = (name, email, mobile, username)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

# Define a route for the edit profile page


# Define a route for submitting the updated profile
@app.route('/update_profile', methods=['POST'])
def update_profile_submit():
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    update_profile(username, name, email, mobile)
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
