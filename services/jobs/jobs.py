from models.job import Job
from db.connection import connection


def createJob():
    title = input("Title: ")
    description = input("Description: ")
    company = input("Company: ")
    location = input("Location: ")
    salary = input("Salary: ")
    category = input("Category: ")

    # cursor = connection.cursor()
    # cursor.execute(f"SELECT title FROM users WHERE title='{Job.title}'")
    # if cursor.fetchone() is not None:
    #     print("\nTitle already taken")
    #     return

    # cursor.close()

    if connection.is_connected():
      query = ("INSERT INTO jobs(title, description, company, location, salary, category) "
             f"VALUES ('{title}', '{description}', '{company}', '{location}', '{salary}', '{category}')")

    connection.cursor().execute(query)
    connection.commit()
    print("\nJob successfully registered")

def getJobs():
    jobs = []
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM jobs")
        for (id, title, description, company, location, salary, category) in cursor:
            job = Job(id=id, title=title, description=description, company=company, location=location, salary=salary, category=category)
            jobs.append(job)
        cursor.close()
    return jobs

def updateJobById(job_id, new_title, new_description, new_company, new_location, new_salary, new_category):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE jobs SET title=%s, description=%s, company=%s, location=%s, salary=%s, category=%s WHERE id=%s", 
                       (new_title, new_description, new_company, new_location, new_salary, new_category, job_id))
        connection.commit()
        cursor.close()
        print("Job successfully updated")
