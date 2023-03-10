import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",  
   
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE team_13")
# Create a table for storing user information
