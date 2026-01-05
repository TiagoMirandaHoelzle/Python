from connection import *

def create():

    # Informações que serão armezandas na tabela produtos
    nome_produto = str(input("Digite o nome do Produto que deseja cadastrar: "))
    descricao_produto = str(input("Digite a descrição do Produto que deseja cadastrar: "))
    preco_produto = float(input("Digite o preço do Produto que deseja cadastrar: $ "))
    desconto_produto = int(input("Digite o desconto do Produto que deseja cadastrar: "))
    estoque_produto = int(input("Digite o estoque do Produto que deseja cadastrar: "))

    # Comando do SQL a ser executado
    sql = "INSERT INTO Produtos(nome_produto, descricao_produto, preco_produto, desconto_produto, estoque_produto)  VALUES(%s, %s, %s, %s, %s)"

    values = (nome_produto, descricao_produto, preco_produto, desconto_produto, estoque_produto)

    # Executando o camando no banco
    cursor.execute(sql, values)

    #commit() para salvar as alterações no banco de dados.
    conn.commit()

def read():
    sql = "SELECT * FROM Produtos;"
    cursor.execute(sql)

    # Obtendo as linhas retornadas pela consulta
    result = cursor.fetchall()

    # Verificando se a variavel esta vazia
    if not result:
        print("Nenhum Produto cadastrado!")
        return # Interrompe a execução da função
        
    for row in result:
        print(f"({row[0]}, {row[1]}, {row[2]}, $ {row[3]}, {row[4]} %, $ {row[5]}, $ {row[6]}, {row[7]} Unidades)")

def update():
    id_produto = int(input("Digite o ID do produto que deseja alterar: "))

    # Novos dados
    novo_nome = str(input("Digite o novo nome do Produto: "))
    nova_descricao = str(input("Digite a nova descrição do Produto: "))
    novo_preco = float(input("Digite o novo preço do Produto: $ "))
    novo_desconto = int(input("Digite o novo desconto do Produto: "))
    novo_estoque = int(input("Digite o novo estoque do Produto: "))

    sql = "UPDATE Produtos SET nome_produto = %s, descricao_produto = %s, preco_produto = %s, desconto_produto = %s, estoque_produto = %s WHERE id_produto = %s;"

    values = (novo_nome, nova_descricao, novo_preco, novo_desconto, novo_estoque, id_produto)
    cursor.execute(sql, values)
    conn.commit()

def delete():
    id_produto = int(input("Digite o ID do produto que deseja excluir: "))

    sql = f"DELETE FROM Produtos WHERE id_produto = %s"

    cursor.execute(sql, (id_produto, ))
    conn.commit()