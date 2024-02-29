import sqlite3

def create_database():
    try:
        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                courses TEXT
                                )''')

        
            cursor.execute("INSERT INTO students (name, courses) VALUES (?, ?)", ("Sam", "SQL Server,ASP.NET MVC,MongoDB"))
            cursor.execute("INSERT INTO students (name, courses) VALUES (?, ?)", ("Mary", "MongoDB,Java"))
            cursor.execute("INSERT INTO students (name, courses) VALUES (?, ?)", ("Tina", "MongoDB,PHP"))

            conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

def generate_report():
    try:
        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            for student in students:
                print("Student Name:", student[1])
                print("Courses:", student[2])
                print("-" * 40)
    except sqlite3.Error as e:
        print("SQLite error:", e)

if __name__ == "__main__":
    create_database()
    generate_report()
