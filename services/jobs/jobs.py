from models.job import Job
from db.connection import connection

def createJob():
    title = input("Enter Title: ")
    description = input("Description: ")
    company = input("Company name: ")
    location = input("Location: ")
    salary = input("Salary: ")
    category = input("Category: ")
    status = "OPEN"
    cursor = connection.cursor()
    cursor.execute(f"SELECT title FROM users WHERE title='{Job.title}'")
    if cursor.fetchone() is not None:
        print("\nTitle already taken")
        return

    cursor.close()

#Connection to the database

    if connection.is_connected():
        query = ("INSERT INTO jobs(title, description, company, location, salary, category) "
                 "VALUES ('{job.title}', '{job.description}', '{job.company}', '{job.location}, '{job.salary}', '{job.category}')")

        connection.cursor().execute(query)
        connection.commit()
        print("\nJob succesfully registered")
#Output

def get_jobs():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    return jobs

def get_jobs_by_title(title):
    title = input("Enter title: ")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM jobs WHERE title='{title}'")
    job = cursor.fetchone()
    cursor.close()
    return job

def get_open_jobs():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE status='OPEN'")
    jobs = cursor.fetchall()
    cursor.close()
    return jobs