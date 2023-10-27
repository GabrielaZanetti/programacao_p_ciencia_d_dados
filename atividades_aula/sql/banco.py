import mysql.connector

def getConexao():
  con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="estoque"
  )
  return con
