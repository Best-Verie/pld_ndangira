from mysql import connector

#Connection db

connection = connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ndangira"
)
