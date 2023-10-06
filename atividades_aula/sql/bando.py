import mysql.connector

def getConexao():
    con = mysql.conenector.connect(
        host = "localhost",
        user = "root",
        password = "user",
        database = "estoque"
    )
    