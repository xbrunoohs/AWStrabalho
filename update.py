import mysql.connector

# Alterar endereço
def updateEndereco(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.executemany(""" UPDATE pessoa 
            SET rua = ?, numero = ?, cidade = ?, cep = ?
            WHERE pessoa.cpf = ?""", (data))
    conn.commit()
    conn.close()

# Alterar telefone
def updateTelefone(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute(""" UPDATE pessoa 
            SET telefone = ?
            WHERE pessoa.cpf = ?""", (data))
    conn.commit()
    conn.close()

# Alterar email
def updateEmail(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute(""" UPDATE pessoa 
            SET email = ?
            WHERE pessoa.cpf = ?""", (data))
    conn.commit()
    conn.close()

# Alterar nome
def updateNome(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute(""" UPDATE pessoa 
            SET nome = ?
            WHERE pessoa.cpf = ?""", (data))
    conn.commit()
    conn.close()

# Alterar a função do funcionario
def updateFuncao(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute(""" UPDATE funcionario 
            SET funcao = ?
            WHERE funcionario.cpf = ?""", (data))
    conn.commit()
    conn.close()

# Alterar o salário do funcionario
def updateSalario(data):
    conexao = mysql.connector.connect(
    host = '172.31.96.227', #ip do banco
    user= 'admin',
    password= 'minich25',
    database= 'crud'
)
    c = conexao.cursor()
    c.execute(""" UPDATE funcionario
            SET salario = ?
            WHERE funcionario.cpf = ?""", (data))
    conn.commit()
    conn.close()

# newEndereco=[("Joana Juliana Grigol", 86, "Campinas", "13085-465", "99999999912"), ]
# updateEndereco(newEndereco)

# newTelefone=["988284588", "99999999912",]
# updateTelefone(newTelefone)

# newEmail=["inae.soares@unesp.br", "99999999912",]
# updateEmail(newEmail)

# newNome=["Inaê", "99999999912",]
# updateNome(newNome)

# newFuncao=["bibliotecario", "99999999918",]
# updateFuncao(newFuncao)

# newSalario=[1200, "99999999918",]
# updateSalario(newSalario)