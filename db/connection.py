from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ndangira"
)