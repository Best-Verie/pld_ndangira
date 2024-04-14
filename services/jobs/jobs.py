from models.job import Job
from db.connection import connection

def createJob():
    title = input("Title: ")
    description = input("Description: ")
    company = input("Company: ")
    location = input("Location: ")
    salary = input("Salary: ")
    category = input("Category: ")

    cursor = connection.cursor()
    cursor.execute(f"SELECT title FROM users WHERE title='{Job.title}'")
    if cursor.fetchone() is not None:
        print("\nTitle already taken")
        return

    cursor.close()

    if connection.is_connected():
        query = ("INSERT INTO jobs(title, description, company, location, salary, category) "
                 "VALUES ('{job.title}', '{job.description}', '{job.company}', '{job.location}, '{job.salary}', '{job.category}')")

        connection.cursor().execute(query)
        connection.commit()
        print("\nJob succesfully registered")

def get_jobs():
    if connection.is_connected():
        query=("SELECT * FROM jobs")

        connection.cursor().execute(query)
        connection.commit()
        print("Jobs successfully retrieved")

def get_jobs_by_title():
    title = input("Enter job title: ")
    query = f"SELECT * FROM jobs WHERE title = '{title}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        print("No jobs found with that title")
    else:
        for job in result:
            print(job)
    cursor.close()