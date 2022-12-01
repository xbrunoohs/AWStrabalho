import mysql.connector

# ------ PESQUISAS POR LIVROS ------

def livroExiste(isbn):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM livro
                WHERE 
                    EXISTS(
                        SELECT 1
                        FROM livro
                        WHERE isbn=?
                    )
                """, (isbn,))
    rows=c.fetchall()
    conn.commit()
    conn.close()
    return rows


# PESQUISA POR NOME DO AUTOR

#pesquisa por nome autor ordena por a-z de título
def ordemAlfAutor(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Titulo
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(ordemAlfAutor("Esopo"))

#pesquisa por nome autor ordena por z-a de título
def ordemAlfCAutor(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Titulo DESC;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfAutor("Esopo"))

#pesquisa por nome autor ordena por a-z de sobrenome
def buscaAutorOAS(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Sobrenome
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaAutorOAS("Esopo"))

#pesquisa por nome autor ordena por z-a de sobrenome
def buscaAutorOADS(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Sobrenome DESC
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaAutorOADS("Esopo"))

#pesquisa por nome autor ordena por editora
def buscaAutorOEdit(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Editora
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaAutorOEdit("Esopo"))

#pesquisa por nome autor ordena por a-z de títuloOriginal
def buscaAutorOATO(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY TituloOriginal
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaAutorOATO("Esopo"))

#pesquisa por nome autor ordena por z-a de títuloOriginal
def buscaAutorOADTO(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY TituloOriginal DESC
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaAutorOADTO("Esopo"))

def buscaAutorOrdenaData(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Publicacao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 

def buscaAutorOrdenaEdicao(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Nome=?
                ORDER BY Edicao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 



# --------------------------------
# PESQUISA POR SOBRENOME DO AUTOR

#pesquisa por sobrenome autor ordena por a-z de título
def ordemAlfSAutor(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Titulo;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfSAutor("Esopo"))

#pesquisa por sobrenome autor ordena por z-a de título
def ordemAlfCSAutor(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Titulo DESC;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfCSAutor("Esopo"))

#pesquisa por sobrenome autor ordena por a-z de nome
def buscaSAutorOAN(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Nome
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaSAutorOAN("Esopo"))

#pesquisa por sobrenome autor ordena por z-a de nome
def buscaSAutorOADN(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Nome DESC
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaSAutorOADN("Esopo"))

def buscaSAutorOrdenaData(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Publicacao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 

def buscaSAutorOrdenaEdicao(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Sobrenome=?
                ORDER BY Edicao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 

# --------------------------------
# PESQUISA POR EDITORA

#pesquisa por editora ordena por a-z de título
def ordemAlfEditora(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Editora=?
                ORDER BY Titulo;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfEditora("Companhia das Letrinhas"))

#pesquisa por editora ordena por z-a de título
def ordemAlfDEditora(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Editora=?
                ORDER BY Titulo DESC;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfDEditora("Companhia das Letrinhas"))


# --------------------------------
# PESQUISA POR TÍTULO

#pesquisa por título ordem alfabética
def ordemAlfLivro(titulo):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo=? 
                ORDER BY Titulo;
            """, (titulo, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfLivro("Fábulas de Esopo"))

#pesquisa por título ordem alfabética contraria
def ordemAlfDLivro(titulo):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo=? 
                ORDER BY Titulo DESC;
            """, (titulo, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisa por titulo ordena por a-z de autor
def buscaTituloOANA(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo=?
                ORDER BY Nome
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOANA("Fábulas de Esopo"))

#pesquisa por titulo ordena por z-a de autor
def buscaTituloOADNA(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo=?
                ORDER BY Nome DESC
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOADNA("Fábulas de Esopo"))

#pesquisa por titulo ordena por editora
def buscaTituloOEdit(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo=?
                ORDER BY Editora
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOEdit("Fábulas de Esopo"))

# --------------------------------
# PESQUISA POR TÍTULO ORIGINAL
#pesquisa por título ordem alfabética
def ordemAlfLivroO(titulo):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=? 
                ORDER BY TituloOriginal;
            """, (titulo, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfLivroO("Fábulas de Esopo"))

#pesquisa por titulo ordena por a-z de autor
def buscaTituloOrigOANA(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=?
                ORDER BY Nome
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOrigOANA("Fábulas de Esopo"))

#pesquisa por titulo ordena por z-a de autor
def buscaTituloOrigOADNA(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=?
                ORDER BY Nome DESC
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOrigOADNA("Fábulas de Esopo"))

#pesquisa por titulo ordena por editora
def buscaTituloOrigOEdit(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=?
                ORDER BY Editora
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 
#print(buscaTituloOrigOEdit("Fábulas de Esopo"))

def buscaTituloOrdenaEdicao(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=?
                ORDER BY Edicao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows 

def buscaTituloOrdenaPublicacao(nome):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE TituloOriginal=?
                ORDER BY Publicacao
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

# --------------------------------
# PESQUISA POR ISBN

#pesquisa livro por isbn
def volumes(isbn):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE isbn=?
            """, (isbn,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(volumes("8585466294"))

# --------------------------------
#PESQUISA POR PALAVRA-CHAVE

#pesquisa por palavra chave ordena por a-z de título
def ordemAlfPC(text):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo LIKE ? OR TituloOriginal LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY Titulo;
            """, (text, text, text, text, text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfPC("Companhia das Letrinhas"))

#pesquisa por palavra chave ordena por z-a de título
def ordemAlfDPC(text):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Titulo LIKE ? OR TituloOriginal LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY Titulo DESC;
            """, (text, text, text, text, text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfDPC("Companhia das Letrinhas"))
