from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'secret_key'

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shannu@21",
    database="team_13"
)

# Define the hackathon table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS hackathons (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description TEXT, theme VARCHAR(255), location VARCHAR(255), date DATE, time TIME, rules TEXT, prizes TEXT)")
mydb.commit()

# Define the registration table
mycursor.execute("CREATE TABLE IF NOT EXISTS registrations (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, hackathon_id INT, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (hackathon_id) REFERENCES hackathons(id))")
mydb.commit()

# Define the submission table
mycursor.execute("CREATE TABLE IF NOT EXISTS submissions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, hackathon_id INT, project_name VARCHAR(255), project_description TEXT, project_file VARCHAR(255), FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (hackathon_id) REFERENCES hackathons(id))")
mydb.commit()

# Define the mentor table
mycursor.execute("CREATE TABLE IF NOT EXISTS mentors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
mydb.commit()

# Define the user table
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), is_mentor BOOLEAN DEFAULT 0)")
mydb.commit()


@app.route('/hackathons')
def hackathons():
    # Retrieve all the hackathons from the database
    mycursor.execute("SELECT * FROM hackathons")
    hackathons = mycursor.fetchall()

    # Check if the user is logged in
    if 'loggedin' in session:
        # Check if the user is a student or mentor
        if session['is_mentor'] == 0:
            # Retrieve the registered hackathons for the user
            user_id = session['id']
            mycursor.execute("SELECT hackathons.id, hackathons.name FROM hackathons INNER JOIN registrations ON hackathons.id = registrations.hackathon_id WHERE registrations.user_id = %s", (user_id,))
            registered_hackathons = mycursor.fetchall()
            return render_template('hackathons.html', hackathons=hackathons, registered_hackathons=registered_hackathons)
        else:
            return render_template('hackathons.html', hackathons=hackathons, is_mentor=True)
    else:
        return redirect(url_for('login'))

@app.route('/register_hackathon/<int:id>')
def register_hackathon(id):
    # Check if the user is logged in
    if 'loggedin' in session:
        # Check if the user is a student
        if session['is_mentor'] == 0:
            user_id = session['id']

            # Insert the registration into the database
            mycursor.execute("INSERT INTO registrations (user_id, hackathon_id) VALUES (%s, %s)", (user_id, id))
            mydb.commit()

            return redirect(url_for('hackathons'))
        else:
            return redirect(url_for('hackathons'))
    else:
        return redirect(url_for('login'))

@app.route('/submissions', methods=['GET', 'POST'])
def submissions():
    if 'loggedin' in session:
        user_type = request.cookies.get('user_type')
        if request.method == 'POST' and user_type == 'student':
            github_link = request.form.get('github_link')
            if github_link:
                username = request.cookies.get('username')
                submission = {
                    'username': username,
                    'github_link': github_link
                }
                submissions.append(submission)
                return redirect(url_for('submissions'))
        elif user_type == 'mentor':
            return render_template('submissions.html', submissions=submissions)
        else:
            return redirect(url_for('hackathons'))
    else:
        return redirect(url_for('login'))

@app.route('/upload_hackathon', methods=['GET', 'POST'])
def upload_hackathon():
    # Check if the user is logged in and is a mentor
    if 'loggedin' in session and session['is_mentor'] == 1:
        if request.method == 'POST':
            # Retrieve the form data
            name = request.form['name']
            description = request.form['description']
            theme = request.form['theme']
            location = request.form['location']
            date = request.form['date']
            time = request.form['time']
            rules = request.form['rules']
            prizes = request.form['prizes']

            # Validate the form data
            if not name or not description or not theme or not location or not date or not time:
                return render_template('upload_hackathon.html', error='Please fill in all the required fields')
            try:
                datetime.strptime(date, '%Y-%m-%d')
                datetime.strptime(time, '%H:%M')
            except ValueError:
                return render_template('upload_hackathon.html', error='Please enter a valid date and time')

            # Insert the hackathon into the database
            mycursor.execute("INSERT INTO hackathons (name, description, theme, location, date, time, rules, prizes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                             (name, description, theme, location, date, time, rules, prizes))
            mydb.commit()

            return redirect(url_for('hackathons'))
        else:
            return render_template('upload_hackathon.html')
    else:
        return redirect(url_for('login'))
    
@app.route('/send_reminder/<int:id>')
def send_reminder(id):
    # Retrieve the hackathon details from the database
    mycursor.execute("SELECT * FROM hackathons WHERE id = %s", (id,))
    hackathon = mycursor.fetchone()

    # Retrieve the list of registered users for the hackathon
    mycursor.execute("SELECT users.email FROM registrations INNER JOIN users ON registrations.user_id = users.id WHERE registrations.hackathon_id = %s", (id,))
    registered_users = mycursor.fetchall()

    # Calculate the time difference between the current time and the start time of the hackathon
    start_time = datetime.datetime.combine(hackathon[5], hackathon[6])
    current_time = datetime.datetime.now()
    time_diff = (start_time - current_time).total_seconds() // 60

    # Send reminder emails to users whose hackathon is starting in less than 30 minutes
    if time_diff <= 30:
        for user in registered_users:
            send_email(user[0], hackathon[1], start_time)

    return redirect(url_for('hackathons'))

def send_email(to_email, hackathon_name, start_time):
    from_email = 'your_email_address'
    password = 'your_email_password'

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = f'Reminder: {hackathon_name} starts in 30 minutes'

    body = f'Hello,\n\nThis is a reminder that the hackathon {hackathon_name} is starting in 30 minutes at {start_time}. Good luck!\n\nBest regards,\nYour Hackathon Team'
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
    except:
        print('Failed to send email')
