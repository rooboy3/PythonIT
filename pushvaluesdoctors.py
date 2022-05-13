import csv, sqlite3

connection = sqlite3.connect("docotors.db")
print(connection.total_changes)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospital
    (hospital_id INTEGER NOT NULL,
    hospital_name TEXT NOT NULL,
    bed_count INTEGER NOT NULL)
    ''')
with open('hospitals.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['hospital_id'], i['hospital_name'], i['bed_count']) for i in dr]
cursor.executemany("INSERT INTO hospital (hospital_id, hospital_name, bed_count) VALUES (?, ?, ?);", to_db)
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
with open('doctors.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['doctor_id'], i['doctor_name'], i['hospital_id'], i['joining_date'], i['specialty'], i['salary']) for i in dr]
cursor.executemany("INSERT INTO doctor (doctor_id, doctor_name, hospital_id, joining_date, specialty, salary) VALUES (?, ?, ?, ?, ?, ?);", to_db)

print("NUMBER 1 !!!!!!!!!!!!!")
rows = cursor.execute("SELECT * FROM doctor").fetchall()
print(rows)
print (" {:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}".format("doctor_id", "doctor_name", "hospital_id", "joining_date", "specialty", "salary"))
print ("----------------+---------------+---------------+---------------+---------------+------")
for v in rows:
    doctor_id, doctor_name, hospital_id, joining_date, specialty, salary = v
    print (" {:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}".format( doctor_id, doctor_name, hospital_id, joining_date, specialty, salary))
new_salary_number = 30000
updated_doctor_name = "Michael"
cursor.execute(
    "UPDATE doctor SET salary = ? WHERE doctor_name = ?",
    (new_salary_number, updated_doctor_name),
).fetchall()
print("\nUpdating salary for \"" + updated_doctor_name + "\n")
target_doctor_name = "Michael"
rows3 = cursor.execute(
    "SELECT doctor_id, doctor_name, hospital_id, joining_date, specialty, salary FROM doctor WHERE doctor_name = ?",
    (target_doctor_name,),
).fetchall()
print (" {:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}".format("doctor_id", "doctor_name", "hospital_id", "joining_date", "specialty", "salary"))
print ("----------------+---------------+---------------+---------------+---------------+------")
for v in rows3:
    doctor_id, doctor_name, hospital_id, joining_date, specialty, salary = v
    print (" {:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}".format( doctor_id, doctor_name, hospital_id, joining_date, specialty, salary))
