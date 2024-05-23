# import sqlite
import sqlite3 as lite

#CRUD - CREATE, READ, UPDATE, DELETE

# criando conexao com banco de dados
con = lite.connect('dados.db')

# inserir dados no banco de dados
def inserirForm(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario( nome, cidade, bairro, logradouro, numero, cep, ano, andares, unidadesAndar, torres, valor, condominio, iptu, tipo, tamanho, quartos, suites, banheiros, vagas, portaria, elevadores, gas, gerador, portaoEletronico, salaoFestas, areaLazer, descricao, imagem) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

# Atualizar dados no banco de dados
def atulizarForm(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, cidade=?, bairro=?, logradouro=?, numero=?, cep=?, ano=?, andares=?, unidadesAndar=?, torres=?, valor=?, condominio=?, iptu=?, tipo=?, tamanho=?, quartos=?, suites=?, banheiros=?, vagas=?, portaria=?, elevadores=?, gas=?, gerador=?, portaoEletronico=?, salaoFestas=?, areaLazer=?, descricao=?, imagem=? WHERE id=? "
        cur.execute(query,i)

# Deletar dados no banco de dados
def deletarForm(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM  inventario WHERE id=?"
        cur.execute(query, i)


# Ver dados no banco de dados
def verForm():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM  inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


# Ver dados id individual no banco de dados

def verItem(id):
    verDadosIndividual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM  inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            verDadosIndividual.append(row)
    return verDadosIndividual

