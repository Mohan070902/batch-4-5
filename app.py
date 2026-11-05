from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/database")
def database():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        use_pure = True
    )

    course = connection.cursor()

    course.execute("CREATE DATABASE schooldb")

    course.execute("use schooldb")

    connection.commit()

    connection.close()

    return "Database Created Successfully.."

#Table Create
@app.route("/table")
def table():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        use_pure = True,
        database = "schooldb"
    )

    course = connection.cursor()

    course.execute("""
                CREATE TABLE students(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100),
                course VARCHAR(100))
                """)

    connection.commit()

    connection.close()

    return "Table Created Successfully.."


@app.route("/create")
def create():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        use_pure = True,
        database = "schooldb"
    )

    course = connection.cursor()

    course.execute("insert into students (name, course) values (%s, %s)", ("Ajay", "Python"))
    course.execute("insert into students (name, course) values (%s, %s)", ("Vinod", "Java"))
    course.execute("insert into students (name, course) values (%s, %s)", ("Ajith", "Java"))
    course.execute("insert into students (name, course) values (%s, %s)", ("Dhanush", "DotNet"))
    
    connection.commit()

    connection.close()

    return "Student Added..."

@app.route("/view")
def vies():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        use_pure = True,
        database = "schooldb"
    )
    a = connection.cursor()
    a.execute("select * from students")

    students = a.fetchall()

    a.close()
    connection.close()

    return render_template("about.html", students = students)

@app.route("/about")
def about():
    return render_template("course.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)