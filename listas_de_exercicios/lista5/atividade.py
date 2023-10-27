import connectBanco

con = connectBanco.getConexao()
cursor = con.cursor()

# sql = "select * from item_venda"
# cursor.execute(sql)

# resultado = cursor.fetchall()

# for x in resultado:
#   print(x)

# con.close

#   Escreva um programa que utilize o banco de dados estoque para inserir itens em uma venda e abater do estoque.
sql = "INSERT INTO venda (id_venda, id_vendedor, id_cliente, dt_venda, vl_total_venda) VALUES (default, %s, %s, %s, %s)"
par = (1, 1, '2023-10-26', 73.44)
cursor.execute(sql, par)

con.commit()

print(cursor.rowcount, "registro inserido")
print("id_cliente:", cursor.lastrowid)

con.close

#   Escreva um programa que utilize o banco de dados estoque para exibir todas as vendas de um vendedor (nome) em um determinado mês e ano.


#   Escreva um programa que utilize o banco de dados estoque para exportar os dados de todas as vendas para um documento json.

