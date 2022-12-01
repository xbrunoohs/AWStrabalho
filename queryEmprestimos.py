import mysql.connector

# ------ PESQUISAS POR EMPRÉSTIMOS ------

#pesquisar emprestimos por cadastro do sócio ordem a-z titulo
def cadastroLivroTitulo(valor):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY Codigo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo z-a titulo
def codigoCadastroTit(valor): 
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY Cadastro
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows