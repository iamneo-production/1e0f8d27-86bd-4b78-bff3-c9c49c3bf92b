from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
import mysql.connector
import jwt

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


#login part
@app.route("/mentor/login",methods=['POST'])
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
        return render_template('student/home.html')
    
    else:
        #email or password is invalid
        query='SELECT * FROM mentors WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        userf=cursor.fetchone()
        
        if userf:
            #wrong password
        
            return redirect(url_for('login_page_men', error=True))

@app.route('/mentor/login', methods=['GET'])
def login_page_men():
    error = request.args.get('error')
    return render_template('mentor/login.html', error=error)
        
        

@app.route("/student/login",methods=['POST'])
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
        return render_template("mentor/home.html")
    
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

@app.route('/student/login',methods=['GET'])
def login_nor_stu():
    error=request.args.get('errorreg')
    return render_template('student/login.html', error=error)


@app.route('/student/login', methods=['GET'])
def login_page_stu():
    error = request.args.get('errorpass')
    return render_template('student/login.html', error=error)

#registration part
@app.route("/student/register",methods=['POST'])
def register():
    username=request.form.get('username')
    password=request.form.get('password')
    con_password=request.form.get('confirm-password')
    email=request.form.get('email')
    mobile-no=request.form.get('mobile_no')

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
    query="INSEERT INTO users (username, password, email)"
    values=(username, password, email)
    cursor.execute(query,values)
    cnx.commit() 

    
    return render_template('mentor/home.html')

@app.route('/student/register', methods=['GET'])
def register_page_exist():
    error = request.args.get('errorexist')
    return render_template('student/register.html', error=error)

@app.route('/student/register', methods=['GET'])
def register_page_existacc():
    error = request.args.get('erroracc')
    return render_template('student/register.html', error=error)

@app.route('/student/register', methods=['GET'])
def register_page_pass():
    error = request.args.get('erroracc')
    return render_template('student/register.html', error=error)















if __name__=='__main__':
    app.run(debug=True)
    