from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
CORS(app)

#configuration of MYSQL
cnx=mysql.connector.connect(user="\\\\",password="\\\\\\",host="\\\\",database="")
cursor=cnx.cursor()

#login part
@app.route("/login",methods=['POST'])
def login():
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
            'message': 'Login Successful'
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
@app.route("/register",methods=['POST'])
def register():
    username=request.json.get('username')
    password=request.json.get('password')
    email=request.json.get('email')

    #checking if username already exists
    query='SELECT * FROM users WHERE username=%s'
    values=(username,)
    cursor.execute(query,values)
    usere=cursor.fetchone()

    if usere:
        response={
            'message'='username already exists'
        }
        return make_response(jsonify(response),409)
    query='SELECT * FROM users WHERE email=%s'
    values=(email,)
    cursor.execute(query,values)
    emailu=cursor.fetchone()

    if emailu:
        response={
            'message'='acccount already exists'
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