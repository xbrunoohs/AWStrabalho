import mysql.connector

#deleta da tabela

def deleteExemplar(codigo):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""DELETE FROM exemplar WHERE codigoExemplar=(?)""", (int(codigo[0][0]), ))
    conn.commit()
    conn.close()
    
def deleteLivro(isbn):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""DELETE FROM livro WHERE isbn=(?)""", (int(isbn[0][0]), ))
    conn.commit()
    conn.close()

def deletePessoa(cpf):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""DELETE FROM pessoa WHERE cpf=(?)""", (int(cpf[0][0]), ))
    conn.commit()
    conn.close()

# deleteExemplar(1)
# deleteLivro("8585466294")
#deletePessoa("99999999917")