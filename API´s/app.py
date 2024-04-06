# SQL - Structured Query Language
# db.sqlite3
import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodar comando SQL
    sql.execute('create table banda(nome text, estilo text, membros interger);')
    # Exemplo de inserir dados
    sql.execute('insert into banda(nome, estilo, membros) values("banda 1", "Rock", 3)')
    # Exemplo de usar dados da minha aplicação em um comando SQL
    nome = str(input('Digite o nome da banda'))
    estilo = str(input('Digite o estilo da banda'))
    quan_integ = int(input('Quantidade de integrantes da banda'))

    sql.execute('insert into banda values(?,?,?)', [nome, estilo, quan_integ])
    # Salvando alterações no bando de dados
    conexao.commit()

    # Exibir dados no console python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
