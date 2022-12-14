import mysql.connector

def addMPessoa(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO pessoa VALUES (?,?,?,?,?,?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMSocio(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO socio(cpf) VALUES (?)""", (many))
    conn.commit()
    conn.close()

def addMFuncionario(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO funcionario VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMLivro(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO livro VALUES (?,?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMExemplar(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO exemplar(emprestado, anoPubli, edicao, isbn) VALUES (?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMAutor(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO autor VALUES (?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMDevolucao(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO devolucao(socio, funcionario, codigoExemplar, data, hora) VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMEmprestimo(many):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany("""INSERT INTO emprestimo(socio, funcionario, codigoExemplar, dataE, horaE) VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()


livro=[
     ("8585466294", "F??bulas de Esopo", "F??bulas de Esopo", "Companhia das Letrinhas", "Infantil", 0),
            ("8574061557", "Hist??rias ?? Brasileira", "Historias ?? Brasileira", "Companhia das Letrinhas", "Infantil", 0),
            ("8574062197","Arca de No??, A", "Arca de No??, A", "Companhia das Letrinhas", "Religioso", 0),
            ("8565484572", "La??os, Turma da M??nica", "La??os, Turma da M??nica", "Panini", "Quadrinhos", 0),
            ("8537809667", "M??gico de Oz, O", "Wizard of Oz, The", "Aventura", "Zahar", 0),
]
#addMLivro(livro)

exemplar=[
    (0, 1999, 1, "8585466294"),
    (0, 1999, 2, "8585466294"),
    (0, 1999, 1, "8585466294"),
    (0, 1999, 3, "8585466294"),
    (0, 1999, 1, "8585466294"),
]
#addMExemplar(exemplar)

autor=[
    ( "Esopo",      "Esopo"     ,"8585466294" ),
    ( "Machado",    "Ana Maria" ,"8574061557" ),
    ( "Moraes, de", "Vin??cius"  ,"8574062197" ),
    ( "Cafaggi",    "Lu"        ,"8565484572" ),
    ( "Cafaggi",    "V??tor"     ,"8565484572" ),
    ( "Baum",       "L. Frank"  ,"8537809667" )
]
#addMAutor(autor)

pessoa=[
     ("99999999911","pessoNome1","pessoaSobrenome1","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999912","pessoNome2","pessoaSobrenome2","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999913","pessoNome3","pessoaSobrenome3","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999914","pessoNome4","pessoaSobrenome4","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999915","pessoNome5","pessoaSobrenome5","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999916","pessoNome6","pessoaSobrenome6","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999917","pessoNome7","pessoaSobrenome7","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999918","pessoNome8","pessoaSobrenome8","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
]
#addMPessoa(pessoa)

funcionario=[
    ("1231232",1.32,"bibliotecario","12-12-2012","99999999917"),
    ("1231231",1.211,"almoxarife","12-12-2012","99999999918"),
    ("1234566",1.3333,"faxina","12-12-2012","99999999916"),
]
#addMFuncionario(funcionario)

socio=[
    ("99999999911", ),
    ("99999999912", ),
    ("99999999913", ),
    ("99999999914", ),
]
#addMSocio(socio)
