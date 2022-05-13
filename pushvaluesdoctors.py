import sqlite3

connection = sqlite3.connect("docotors.db")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospital
    (hospital_id INTEGER NOT NULL,
    hospital_name TEXT NOT NULL,
    bed_count INTEGER NOT NULL)
    ''')
cursor.execute('''
    INSERT INTO hospital (hospital_id, hospital_name, bed_count)
    VALUES
     ('1','Mayo Clinic', 200),
     ('2','Cleveland Clinic', 400),
     ('3','Johns Hopkins', 1000),
     ('4','UCLA Medical Centre', 1500)
    ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctor
([doctor_id] INTEGER NOT NULL,
[doctor_name] TEXT NOT NULL,
[hospital_id] INTEGER NOT NULL,
[joining_date] TEXT NOT NULL,
[specialty] TEXT NOT NULL,
[salary] INTEGER NOT NULL
)
''')
cursor.execute('''
INSERT INTO doctor (doctor_id, doctor_name, hospital_id, joining_date, specialty, salary)
VALUES
('101', 'David', '1', '2005-2-10', 'Pediatric', '40000'),
('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000'),
('103', 'Susan', '2', '2016-05-19', 'Gynacologist', '25000'),
('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000'),
('105', 'Linda', '3', '2004-06-04', 'Gynacologist', '42000'),
('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000'),
('107', 'Richard', '4', '2014-08-21', 'Gynacologist', '32000'),
('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000')
''')
print("NUMBER 1 !!!!!!!!!!!!!")
rows = cursor.execute("SELECT * FROM doctor").fetchall()
print(rows)
print("NUMBER 2 !!!!!!!!!!!!!")
target_doctor_name = "Michael"
rows2 = cursor.execute(
    "SELECT doctor_id, doctor_name, hospital_id, joining_date, specialty, salary FROM doctor WHERE doctor_name = ?",
    (target_doctor_name,),
).fetchall()
print(rows2)
print("NUMBER 3 !!!!!!!!!!!!!")
new_salary_number = 30000
updated_doctor_name = "Michael"
cursor.execute(
    "UPDATE doctor SET salary = ? WHERE doctor_name = ?",
    (new_salary_number, updated_doctor_name),
).fetchall()
print("Updating salary for \"" + updated_doctor_name + "\"")
print("NUMBER 4 !!!!!!!!!!!!!")
target_doctor_name = "Michael"
rows3 = cursor.execute(
    "SELECT doctor_id, doctor_name, hospital_id, joining_date, specialty, salary FROM doctor WHERE doctor_name = ?",
    (target_doctor_name,),
).fetchall()
print(rows3)
