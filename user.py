import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",  
   
)
# Create a table for storing user information
mycursor = db.cursor()
mycursor.execute("create database mydb1")
mycursor.execute("use mydb1")
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

# Create a function for registering a new user
def register_user(username, email, password):
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    val = (username, email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("User registered successfully")

# Create a function for logging in a user
def login_user(username, password):
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()
    if user:
        print("User logged in successfully")
    else:
        print("Invalid username or password")

db.close()