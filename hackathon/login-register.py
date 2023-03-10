from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
import mysql.connector
import jwt

app=Flask(__name__)
CORS(app)

#configuration of MYSQL
cnx=mysql.connector.connect(user="root",password="examly",host="localhost")
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
        return render_template('index.html')
    
    else:
        #email or password is invalid
        query='SELECT * FROM mentors WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        userf=cursor.fetchone()
        
        if userf:
            #wrong password
            response={
                'message':'Invalid password'
            }
            return make_response(jsonify(response),401)
        
        

@app.route("/student/login",methods=['POST'])
def login_student():
    email=request.json.get('email')
    password=request.json.get('password')

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
        return make_response(jsonify(response),200)
    
    else:
        #email or password is invalid
        query='SELECT * FROM users WHERE email=%s'
        values=(email,)
        cursor.execute(query,values)
        userf=cursor.fetchone()
        
        if userf:
            #wrong password
            response={
                'message':'Invalid password'
            }
            return make_response(jsonify(response),401)
        
        else:
            #not yet registered
            response={
                'message':'sign-up first'
            }
            return make_response(jsonify(response),401)

#registration part
@app.route("/student/register",methods=['POST'])
def register():
    username=request.json.get('username')
    password=request.json.get('password')
    email=request.json.get('email')
    mobile-no=request.json.get('mobile_no')

    #checking if username already exists
    query='SELECT * FROM users WHERE username=%s'
    values=(username,)
    cursor.execute(query,values)
    usere=cursor.fetchone()

    if usere:
        response={
            'message':'username already exists'
        }
        return make_response(jsonify(response),409)
    query='SELECT * FROM users WHERE email=%s'
    values=(email,)
    cursor.execute(query,values)
    emailu=cursor.fetchone()

    if emailu:
        response={
            'message':'acccount already exists'
        }
        return make_response(jsonify(response),409)
    
    #enter details in the database
    query="INSEERT INTO users (username, password, email)"
    values=(username, password, email)
    cursor.execute(query,values)
    cnx.commit() 

    response={
        'message':'Registration successful'
    } 
    return make_response(jsonify(response),201)

if __name__=='__main__':
    app.run(debug=True)
    