import sqlite3

conn = sqlite3.connect('registration2.sqlite3')

conn.execute('CREATE TABLE IF NOT EXISTS Students (Id INT, Name TEXT)')

conn.execute("INSERT INTO Students (Id, Name) VALUES (1, 'Sam')")
conn.execute("INSERT INTO Students (Id, Name) VALUES (2, 'Mary')")
conn.execute("INSERT INTO Students (Id, Name) VALUES (3, 'Tina')")


conn.execute('CREATE TABLE IF NOT EXISTS Courses (Id INT, Name TEXT)')

conn.execute("INSERT INTO Courses (Id, Name) VALUES (1, 'SQLServer')")
conn.execute("INSERT INTO Courses (Id, Name) VALUES (2, 'ASP.NET MVC')")
conn.execute("INSERT INTO Courses (Id, Name) VALUES (3, 'MongoDB')")
conn.execute("INSERT INTO Courses (Id, Name) VALUES (1, 'Java')")
conn.execute("INSERT INTO Courses (Id, Name) VALUES (2, 'PHP')")


conn.execute('CREATE TABLE IF NOT EXISTS StudentCourses (StudentID INT, CourseId INT)')

conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (1, 1)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (1, 2)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (1, 3)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (2, 3)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (2, 4)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (3, 3)")
conn.execute("INSERT INTO StudentCourses (StudentID, CourseId) VALUES (3, 5)")

conn.commit()

cursor = conn.execute('SELECT * FROM Students')
for row in cursor:
    print(f"Id = {row[0]}, Name = {row[1]},")
print('')

cursor = conn.execute('SELECT * FROM Courses')
for row in cursor:
    print(f"Id = {row[0]}, Name = {row[1]},")
print('')

cursor = conn.execute('SELECT * FROM StudentCourses')
for row in cursor:
    print(f"StudentID = {row[0]}, CourseId = {row[1]},")
print('')

conn.close()
