import datetime
import time
import random
import pyodbc

# Connect to the SQL Server database
try:
    con = pyodbc.connect('Driver={SQL Server};'
                         'Server=DESKTOP-RQPSSUJ\SQLEXPRESS;'
                         'Database=call_center;'
                         'Trusted_Connection=yes;')
    cursor = con.cursor()
except pyodbc.Error as e:
    print("Failed to connect to SQL Server:", e)

# Insert random data into the 'calls' table
while True:
    date = datetime.date.today()
    location = random.randint(111, 201)
    company = random.randint(11, 30)
    issue = random.randint(111, 130)
    csr = random.randint(111, 210)
    rtime = random.randint(1, 300)
    ctime = random.randint(1, 600)
    status = random.randint(1, 100)

    if status < 75:
        status = 1
    elif status < 85:
        status = 2
    elif status < 90:
        status = 3
    else:
        status = 4

    if status == 1:
        rating = random.randint(5, 10)
    elif status == 2:
        rating = random.randint(3, 8)
    elif status == 3:
        rating = random.randint(1, 3)
    else:
        rating = random.randint(1, 5)

    try:
        cursor.execute('INSERT INTO dbo.calls VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (datetime.datetime.now(), location, company, issue, csr, rtime, ctime, status, rating))
        con.commit()
        print("Data inserted successfully.")
    except pyodbc.Error as e:
        print("Error inserting data:", e)

    time.sleep(1)
