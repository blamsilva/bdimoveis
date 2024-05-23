# importando sqlite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')

# criando tabela 
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, numero INTEGER, cep INTEGER, ano INTEGER, andares INTEGER, unidadesAndar INTEGER, torres INTEGER, valor DECIMAL, condominio DECIMAL, iptu DECIMAL, tipo INTEGER, tamanho DECIMAL, quartos INTEGER, suites INTEGER, banheiros INTEGER, vagas INTEGER, portaria BOOLEAN, elevadores BOOLEAN, gas BOOLEAN, gerador BOOLEAN, portaoEletronico BOOLEAN, salaoFestas BOOLEAN, areaLazer BOOLEAN, descricao TEXT, imagem TEXT)")
 