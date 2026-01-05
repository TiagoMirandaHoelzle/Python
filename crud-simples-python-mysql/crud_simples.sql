DROP SCHEMA IF EXISTS crud_simples;
CREATE SCHEMA crud_simples;
USE crud_simples;

CREATE TABLE Produtos(
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(255) NOT NULL,
    descricao_produto VARCHAR(500) NOT NULL,
    preco_produto DECIMAL(10,2) NOT NULL,
    desconto_produto INT DEFAULT (0),
    valor_desconto DECIMAL(10,2) GENERATED ALWAYS AS ((preco_produto * desconto_produto)/100) STORED,
    preco_final_produto DECIMAL(10,2) GENERATED ALWAYS AS (preco_produto - valor_desconto) STORED,
    estoque_produto INT NOT NULL DEFAULT (1)
);
