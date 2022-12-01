import mysql.connector

# ------ ORDENAR EXEMPLAR ------

#por estado de empréstimo
def ordemEmprestado(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Emprestado;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
print(ordemEmprestado("8585466294"))

#por ano de publicação
def ordemPubliAno(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Publicacao;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemPubliAno("8585466294"))

#por edição
def ordemEdiLivro(titulo):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Edicao
            """, (titulo, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemEdiLivro("8585466294"))

#livro por código
def ordemAlfCodigo(cod):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Codigo=?
            """, (cod, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfCodigo(1))

#por editora
def ordemEditora(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE ISBN=?
                ORDER BY Editora
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemEditora("8585466294"))
