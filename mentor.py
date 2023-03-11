import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",  
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE mentors")
# create table
mycursor.execute("USE mentors")

mycursor.execute("CREATE TABLE mentors(id INT PRIMARY KEY,name VARCHAR(50) NOT NULL,email VARCHAR(100) NOT NULL,password VARCHAR(50) NOT NULL");

mycursor.execute("INSERT INTO mentors(id, name, email, password) VALUES (1, 'Mentor 1', 'mentor1@example.com', 'password1'),(2, 'Mentor 2', 'mentor2@example.com', 'password2'),(3, 'Mentor 3', 'mentor3@example.com', 'password3'),(4, 'Mentor 4', 'mentor4@example.com', 'password4'),(5, 'Mentor 5', 'mentor5@example.com', 'password5')")
db.close()