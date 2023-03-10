import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="examly",
  database="team_13"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE users (username VARCHAR(255), name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), mobile_number BIGINT(20), skills VARCHAR(10000))")

#mycursor.execute("CREATE TABLE workshops (username VARCHAR(255), email VARCHAR(255),workshop_id VARCHAR(255), workshop_name VARCHAR(255), timestamp_w TIMESTAMP) ")

#mycursor.execute("CREATE TABLE hackathons (username VARCHAR(255), email VARCHAR(255),hackathon_id VARCHAR(255), hackathon_name VARCHAR(255), timestamo_h TIMESTAMP)")

#mycursor.execute("DROP DATABASE team_13");
#sql = "DROP TABLE team_13.mentors"

#mycursor.execute(sql)
#mycursor.execute("CREATE TABLE mentors (username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

#print(mentors)
username="user4"
password="1234"
email="Shirisha0572@gmail.com"
values=(username, email, password)

query="INSERT INTO team_13.mentors (username,email, password) VALUES (%s, %s, %s)"
mycursor.execute(query,values)
mydb.commit()