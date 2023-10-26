import mysql.connector

def getConexao():
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "user",
        database = "estoque"
    )
    return con

print(getConexao)