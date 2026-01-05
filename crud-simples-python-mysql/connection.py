import mysql.connector

try:
    # Estabelecendo a conexão com o banco de dados
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_simples",
        port=3306
    )

    # Verificando a conexão
    if conn.is_connected(): 
        print("Conexão realizada com sucesso!")

except mysql.connector.Error as error:
    print(f"Falha na conexão: {error}")

# Criando um objeto cursor para executar os comandos SQL

cursor = conn.cursor()
