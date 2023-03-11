from flask import Flask,request,jsonify,make_response, render_template
from flask_cors import CORS
import mysql.connector
import jwt
import random
import smtplib

app=Flask(__name__)
CORS(app)

#configuration of MYSQL
cnx=mysql.connector.connect(user="root",password="examly",host="localhost",database="team_13")
cursor=cnx.cursor()

#creating JWT token
def token(email,password):
    payload={
        'email':email,
        'password':password
    }

    #encode payload to create JWT token
    jwt_token=jwt.encode(payload,'frida_kahlo',algorithm='HS256')

    #returning token to the client
    return jsonify({'token':jwt_token.decode('utf-8')})


@app.route('/login_mentor', methods=['GET'])
def login_page_men():
    error = request.args.get('error')
    return render_template('/login_mentor.html', error=error)


#login part
@app.route("/login_mentor",methods=['POST'])
def login_mentor():

    email=request.form.get('email')
    password=request.form.get('password')

    #to check if there exist a valid email and password
    query="SELECT * FROM mentors WHERE email=%s AND password=%s"
    values=(email,password)

    cursor.execute(query,values)
    user=cursor.fetchone()

    #check if exists then login
    if user:
        #calling JWT token and return it to the client

        response={
            'message': 'Login Successful',
            'token': token(email,password)

        }
        return render_template('/login_mentor.html')
    
    else:
        #email or password is invalid
        query='SELECT * FROM mentors WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        userf=cursor.fetchone()
        
        if userf:
            #wrong password
        
            return redirect(url_for('login_page_men', error=True))


        
@app.route('/login_student',methods=['GET'])
def login_nor_stu():
    error=request.args.get('errorreg')
    return render_template('login_student.html', error=error)


@app.route('/login_student', methods=['GET'])
def login_page_stu():
    error = request.args.get('errorpass')
    return render_template('login_student.html', error=error)    

@app.route("/login_student",methods=['POST'])
def login_student():
    email=request.form.get('email')
    password=request.form.get('password')

    #to check if there exist a valid email and password
    query="SELECT * FROM users WHERE email=%s AND password=%s"
    values=(email,password)

    cursor.execute(query,values)
    user=cursor.fetchone()

    #check if exists then login
    if user:
        #calling JWT token and return it to the client

        response={
            'message': 'Login Successful',
            'token': token(email,password)

        }
        return render_template("/login_student.html")
    
    else:
        #email or password is invalid
        query='SELECT * FROM users WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        userf=cursor.fetchone()
        
        if userf:
            #wrong password
            
            return redirect(url_for('login_page_stu', error=True))
        
        else:
            #not yet registered
            
            return redirect(url_for('login_nor_stu', error=True))



#registration part
@app.route("/register",methods=['POST'])
def register():
    username=request.form.get('username')
    password=request.form.get('password')
    con_password=request.form.get('confirm_password')
    email=request.form.get('email')
    mobile_no=request.form.get('phone')

    #checking if username already exists
    query='SELECT * FROM users WHERE username=%s'
    values=(username,)
    cursor.execute(query,values)
    usere=cursor.fetchone()

    if usere:
        
        return redirect(url_for('register_page_exist', error=True))
    query='SELECT * FROM users WHERE email=%s'
    values=(email,)
    cursor.execute(query,values)
    emailu=cursor.fetchone()

    if emailu:
        response={
            'message':'acccount already exists'
        }
        return redirect(url_for('register_page_existacc', error=True))

    if con_password!=password:
        return redirect(url_for('register_page_pass', error=True))

    #enter details in the database
    query="INSERT INTO users (username, mobile_no ,password, email)"
    values=(username,mobile_no, password, email)
    cursor.execute(query,values)
    cnx.commit() 

    
    return render_template('SignUp2.html')

@app.route('/register', methods=['GET'])
def register_page_exist():
    error = request.args.get('errorexist')
    return render_template('SignUp2.html', error=error)

@app.route('/register', methods=['GET'])
def register_page_existacc():
    error = request.args.get('erroracc')
    return render_template('SignUp2.html', error=error)

@app.route('/register', methods=['GET'])
def register_page_pass():
    error = request.args.get('errorpass')
    return render_template('SignUp2.html', error=error)


EMAIL_ADDRESS = '20at1a3106@gpcet.ac.in'
EMAIL_PASSWORD = '#Sma2509'

def generate_verification_code():
    return str(random.randint(100000, 999999))

# define a function to send a verification code to the user's email address
def send_verification_code(email, code):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Forgot Password Verification Code'
        body = f'Your verification code is {code}'
        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, email, message)

# define the routes
@app.route('/')
def index():

    return render_template('index.html')



@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        # check if the email exists in the users list
        query='SELECT * FROM users WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        user=cursor.fetchone()
        if user:
            # generate a verification code and send it to the user's email
            code = generate_verification_code()
            send_verification_code(email, code)
            # store the verification code in the dictionary
            verification_codes[email] = code
            # redirect to the reset password page with the email parameter
            return redirect(url_for('reset_password', email=email))
        else:
            # display an error message if the email doesn't exist
            query='SELECT * FROM mentors WHERE email=%s'
            values=(email,)
            cursor.execute(query,values)
            user=cursor.fetchone()
            if user:
                # generate a verification code and send it to the user's email
                code = generate_verification_code()
                send_verification_code(email, code)
                # store the verification code in the dictionary
                verification_codes[email] = code
                # redirect to the reset password page with the email parameter
                return redirect(url_for('reset_password', email=email))
            else:
                message = 'Email does not exist'
                return render_template('forgotpassword.html', message=message)
    else:
        return render_template('forgotpassword.html')


@app.route('/verification_code', methods=['GET'])
def reset_pass_er():
    error = request.args.get('errorpass')
    return render_template('verification_code.html', error=error)

@app.route('/verification_code', methods=['GET'])
def reset_pass_code():
    error = request.args.get('errorcode')
    return render_template('verification_code.html', error=error)

@app.route('/verification_code', methods=['GET', 'POST'])
def reset_password():
    
    if request.method == 'POST':
        code = request.form['code']
        password = request.form['password']
        con_password=request.form['confirm_password']
        # check if the verification code and password are valid
        if con_password!=password:
            return redirect(url_for('reset_pass_er', error=True))
        if verification_codes.get(email) == code and password:
            # update the user's password in the users list
            user = next((user for user in users if user['email'] == email), None)
            user['password'] = password
            # display a success message and redirect to the login page
            message = 'Password reset successful'
            return redirect(url_for('index', message=message))
        else:
            # display an error message if the verification code or password is invalid
            message = 'Invalid verification code or password'
            return redirect(url_for('reset_pass_code', error=True))
    else:
        return render_template('reset_password.html', email=email)





















if __name__=='__main__':
    app.run( port=8080,debug=True)
    