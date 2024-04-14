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
    # cursor = connection.cursor()
    # cursor.execute(f"SELECT title FROM users WHERE title='{Job.title}'")
    # if cursor.fetchone() is not None:
    #     print("\nTitle already taken")
    #     return

    # cursor.close()

#Connection to the database

    if connection.is_connected():
      query = ("INSERT INTO jobs(title, description, company, location, salary, category, status) "
             f"VALUES ('{title}', '{description}', '{company}', '{location}', '{salary}', '{category}', '{status}')")

    connection.cursor().execute(query)
    connection.commit()
    print("\nJob successfully registered")

def getJobs():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    print("\n")
    print("ID\tTitle\t\t\tDescription\tSalary\t\tLocation\tCompany\t\tCategory\tStatus")
    print("========================================================================================================================")
    for job in jobs:
        print(f"{job[0]}\t{job[1]}\t{job[2]}\t\t{job[3]}\t{job[4]}\t\t{job[5]}\t\t{job[6]}\t\t{job[7]}")
    print("\n")
    return jobs

def updateJobById(job_id, new_title, new_description, new_company, new_location, new_salary, new_category):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE jobs SET title=%s, description=%s, company=%s, location=%s, salary=%s, category=%s WHERE id=%s", 
                       (new_title, new_description, new_company, new_location, new_salary, new_category, job_id))
        connection.commit()
        print("\nJob succesfully updated")
#Output

def closeJobById(job_id):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE jobs SET status='CLOSED' WHERE id=%s", (job_id,))
        connection.commit()
        print("\nJob closed")

def get_companies():
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT company FROM jobs")
    companies = cursor.fetchall()
    cursor.close()
    print("\n")
    print("Companies")
    print("=========")
    for company in companies:
        print(company[0])
    print("\n")
    return companies

def get_jobs_by_title(title):
    title = input("Enter title: ")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM jobs WHERE title='{title}'")
    job = cursor.fetchone()
    cursor.close()
    print("\n")
    print("ID\tTitle\t\t\tDescription\tSalary\t\tLocation\tCompany\t\tCategory\tStatus")
    print("========================================================================================================================")
    print(f"{job[0]}\t{job[1]}\t{job[2]}\t\t{job[3]}\t{job[4]}\t\t{job[5]}\t\t{job[6]}\t\t{job[7]}")
    print("\n")
    return job

def get_open_jobs():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE status='OPEN'")
    jobs = cursor.fetchall()
    cursor.close()
    print("\n")
    print("ID\tTitle\t\t\tDescription\tSalary\t\tLocation\tCompany\t\tCategory\tStatus")
    print("========================================================================================================================")
    for job in jobs:
        print(f"{job[0]}\t{job[1]}\t{job[2]}\t\t{job[3]}\t{job[4]}\t\t{job[5]}\t\t{job[6]}\t\t{job[7]}")
    print("\n")
    return jobs
