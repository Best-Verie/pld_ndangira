from models.job import Job
from db.connection import connection

def createJob():
    title = input("Title: ")
    description = input("Description: ")
    company = input("Company: ")
    location = input("Location: ")
    salary = input("Salary: ")

