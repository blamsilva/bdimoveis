from tkinter import*
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import filedialog as fd


from PIL import Image, ImageTk

# Importando Funçoes view
from view import *


#cores
co0 = "#2ed2ba" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # Verde Escuro
co9 = "#e9edf5" # Cinza

# Criando Janela

janela = Tk()
janela.title('BlamSilva') # Definir título da janela
janela.geometry('1200x795') # Definir tamanho da Janela
janela.configure(background=co9) # Definir Cor de Fundo
janela.resizable(width=FALSE, height=FALSE) # Tamanho de Janela Constante

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames

#1
frameTitulo = Frame(janela, width=1043, height=50, background=co1, relief=FLAT)
frameTitulo.grid(row=0, column=0,sticky=NSEW)
#2
frameCadastro = Frame(janela, width=1043, height=500, background=co1, pady=20, relief=FLAT)
frameCadastro.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#3
frameBancoDados = Frame(janela, width=1043, height=350, bg=co1, relief=FLAT)
frameBancoDados.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Criando Funcoes
global tree

# Funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem
     
    nome = e_nome.get()
    cidade = e_cidade.get()
    bairro = e_bairro.get()
    logradouro = e_logradouro.get()
    numero = e_numero.get()
    cep = e_cep.get()
    ano = e_ano.get()
    andares = e_andares.get()
    unidadesAndar = e_unidadesAndar.get()
    torres = e_torres.get()
    valor = e_valor.get()
    condominio = e_condominio.get()
    iptu = e_iptu.get()
    tipo = e_tipo.get()
    tamanho = e_tamanho.get()
    quartos = e_quartos.get()
    suites = e_suites.get()
    banheiros = e_banheiros.get()
    vagas = e_vagas.get()
    portaria = e_portaria.get()
    elevadores = e_elevador.get()
    gas = e_gas.get()
    gerador = e_gerador.get()
    portaoEletronico = e_portaoEletronico.get()
    salaoFestas = e_salaoFestas.get()
    areaLazer = e_areaLazer.get()
    descricao = e_descricao.get()
    imagem = imagem_string
    
    lista_inserir = [nome, cidade, bairro, logradouro, numero, cep, ano, andares, unidadesAndar, torres, valor, condominio, iptu, tipo, tamanho, quartos, suites, banheiros, vagas, portaria, elevadores, gas, gerador, portaoEletronico, salaoFestas, areaLazer, descricao, imagem]


    for i in lista_inserir:
        if i =='':
            messagebox.showerror('ERRO','Preencha todos os campos.' )
            return
        
    inserirForm(lista_inserir)
    mostrar()

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    
    e_nome.delete(0,'end')
    e_cidade.delete(0,'end')
    e_bairro.delete(0,'end')
    e_logradouro.delete(0,'end')
    e_numero.delete(0,'end')
    e_cep.delete(0,'end')
    e_ano.delete(0,'end')
    e_andares.delete(0,'end')
    e_unidadesAndar.delete(0,'end')
    e_torres.delete(0,'end')
    e_valor.delete(0,'end')
    e_condominio.delete(0,'end')
    e_iptu.delete(0,'end')
    e_tipo.delete(0,'end')
    e_tamanho.delete(0,'end')
    e_quartos.delete(0,'end')
    e_suites.delete(0,'end')
    e_banheiros.delete(0,'end')
    e_vagas.delete(0,'end')
    e_descricao.delete(0,'end')
    e_portaria.delete(0,'end')
    
   
  
    mostrar()


# Funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    ver_imagem()
    try:
        treeVerDados = tree.focus()
        treeDicionario = tree.item(treeVerDados)
        treevLista = treeDicionario['values']

        valor = treevLista[0]

        e_nome.delete(0,'end')
        e_cidade.delete(0,'end')
        e_bairro.delete(0,'end')
        e_logradouro.delete(0,'end')
        e_numero.delete(0,'end')
        e_cep.delete(0,'end')
        e_ano.delete(0,'end')
        e_andares.delete(0,'end')
        e_unidadesAndar.delete(0,'end')
        e_torres.delete(0,'end')
        e_valor.delete(0,'end')
        e_condominio.delete(0,'end')
        e_iptu.delete(0,'end')
        e_tipo.delete(0,'end')
        e_tamanho.delete(0,'end')
        e_quartos.delete(0,'end')
        e_suites.delete(0,'end')
        e_banheiros.delete(0,'end')
        e_vagas.delete(0,'end')
        e_descricao.delete(0,'end')
        
        id = int(treevLista[0])      
        e_nome.insert(0,treevLista[1])
        e_cidade.insert(0,treevLista[2])
        e_bairro.insert(0,treevLista[3])
        e_logradouro.insert(0,treevLista[4])
        e_numero.insert(0,treevLista[5])
        e_cep.insert(0,treevLista[6])
        e_ano.insert(0,treevLista[7])
        e_andares.insert(0,treevLista[8])
        e_unidadesAndar.insert(0,treevLista[9])
        e_torres.insert(0,treevLista[10])
        e_valor.insert(0,treevLista[11])
        e_condominio.insert(0,treevLista[12])
        e_iptu.insert(0,treevLista[13])
        e_tipo.insert(0,treevLista[14])
        e_tamanho.insert(0,treevLista[15])
        e_quartos.insert(0,treevLista[16])
        e_suites.insert(0,treevLista[17])
        e_banheiros.insert(0,treevLista[18])
        e_vagas.insert(0,treevLista[19])
        e_descricao.insert(0,treevLista[27])
        imagem_string = treevLista[28]
       
        def update():
            global imagem, imagem_string, l_imagem
        
            nome = e_nome.get()
            cidade = e_cidade.get()
            bairro = e_bairro.get()
            logradouro = e_logradouro.get()
            numero = e_numero.get()
            cep = e_cep.get()
            ano = e_ano.get()
            andares = e_andares.get()
            unidadesAndar = e_unidadesAndar.get()
            torres = e_torres.get()
            valor = e_valor.get()
            condominio = e_condominio.get()
            iptu = e_iptu.get()
            tipo = e_tipo.get()
            tamanho = e_tamanho.get()
            quartos = e_quartos.get()
            suites = e_suites.get()
            banheiros = e_banheiros.get()
            vagas = e_vagas.get()
            portaria = e_portaria.get()
            elevadores = e_elevador.get()
            gas = e_gas.get()
            gerador = e_gerador.get()
            portaoEletronico = e_portaoEletronico.get()
            salaoFestas = e_salaoFestas.get()
            areaLazer = e_areaLazer.get()
            descricao = e_descricao.get()
            imagem = imagem_string

            if imagem =='':
                imagem = e_nome.insert(0,treevLista[28])

            lista_update = [nome, cidade, bairro, logradouro, numero, cep, ano, andares, unidadesAndar, torres, valor, condominio, iptu, tipo, tamanho, quartos, suites, banheiros, vagas, portaria, elevadores, gas, gerador, portaoEletronico, salaoFestas, areaLazer, descricao, imagem,id]
            
            for i in lista_update:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atulizarForm(lista_update)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados.')

            e_nome.delete(0,'end')
            e_cidade.delete(0,'end')
            e_bairro.delete(0,'end')
            e_logradouro.delete(0,'end')
            e_numero.delete(0,'end')
            e_cep.delete(0,'end')
            e_ano.delete(0,'end')
            e_andares.delete(0,'end')
            e_unidadesAndar.delete(0,'end')
            e_torres.delete(0,'end')
            e_valor.delete(0,'end')
            e_condominio.delete(0,'end')
            e_iptu.delete(0,'end')
            e_tipo.delete(0,'end')
            e_tamanho.delete(0,'end')
            e_quartos.delete(0,'end')
            e_suites.delete(0,'end')
            e_banheiros.delete(0,'end')
            e_vagas.delete(0,'end')
            

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameCadastro, command=update, width=13, text="CONFIRMAR", overrelief=RIDGE, font=("Ivy 8 bold"), bg=co2, fg=co1)
        b_confirmar.place(x=790, y=420)

    except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na Tabela')



# Funcao deletar
def deletar():
    try:
        treeVerDados = tree.focus()
        treeDicionario = tree.item(treeVerDados)
        treevLista = treeDicionario['values']
        valor = treevLista[0]

        deletarForm([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram Deletados.')

    except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na Tabela')
    
    mostrar()

# Funcao para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem
    # Abrindo Imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((270,270))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameCadastro, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=920, y=50)


# Funcao para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treeVerDados = tree.focus()
    treeDicionario = tree.item(treeVerDados)
    treevLista = treeDicionario['values']

    valor = [int(treevLista[0])]
    
    item = verItem(valor)

    imagem = item[0][28]

    # Abrindo Imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((270,270))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameCadastro, image=imagem,bg=co1, fg=co4)
    l_imagem.place(x=920, y=50)


# Trabalhado frameTitulo
# Abrindo Imagem
app_img = Image.open('imagens\logoCasa.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameTitulo, image=app_img, text='SIGEDI - Sistema de Gestão e Disponibilidade', width=1200, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no frameCadastro
# Criando entradas

# nome
l_nome = Label(frameCadastro, text='Nome:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_nome.place(x=100, y=10)

# cidade
l_cidade = Label(frameCadastro, text='Cidade:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cidade.place(x=10, y=40)
e_cidade = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_cidade.place(x=100, y=40)

# bairro
l_bairro = Label(frameCadastro, text='Bairro:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_bairro.place(x=10, y=70)
e_bairro = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_bairro.place(x=100, y=70)

# logradouro
l_logradouro = Label(frameCadastro, text='Logradouro:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_logradouro.place(x=10, y=100)
e_logradouro = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_logradouro.place(x=100, y=100)

# numero
l_numero = Label(frameCadastro, text='Número:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_numero.place(x=10, y=130)
e_numero = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_numero.place(x=100, y=130)

# cep
l_cep = Label(frameCadastro, text='Cep:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cep.place(x=10, y=160)
e_cep = Entry(frameCadastro, width=30, justify='left', relief=SOLID)
e_cep.place(x=100, y=160)

# descrição
l_descricao = Label(frameCadastro, text='Descrição:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=215)
e_descricao = Entry(frameCadastro, width=75,  relief=SOLID)
e_descricao.place(x=100, y=215)


# ano
l_ano = Label(frameCadastro, text='Ano:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_ano.place(x=330, y=10)
e_ano = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_ano.place(x=420, y=10)

# andares
l_andares = Label(frameCadastro, text='Andares:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_andares.place(x=330, y=40)
e_andares = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_andares.place(x=420, y=40)

# unidadesAndar
l_unidadesAndar = Label(frameCadastro, text='Und./Andar:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_unidadesAndar.place(x=330, y=70)
e_unidadesAndar = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_unidadesAndar.place(x=420, y=70)

# torres
l_torres = Label(frameCadastro, text='Torres:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_torres.place(x=330, y=100)
e_torres = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_torres.place(x=420, y=100)

# valor
l_valor = Label(frameCadastro, text='Valor:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=330, y=130)
e_valor = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_valor.place(x=420, y=130)

# condominio
l_condominio = Label(frameCadastro, text='Condomínio:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_condominio.place(x=330, y=160)
e_condominio = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_condominio.place(x=420, y=160)

# iptu
l_iptu = Label(frameCadastro, text='IPTU/ANO:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_iptu.place(x=330, y=190)
e_iptu = Entry(frameCadastro, width=15, justify='left', relief=SOLID)
e_iptu.place(x=420, y=190)

# tipo
l_tipo = Label(frameCadastro, text='Tipo:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tipo.place(x=550, y=10)
e_tipo = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_tipo.place(x=650, y=10)

# tamanho
l_tamanho = Label(frameCadastro, text='Tamanho:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tamanho.place(x=550, y=40)
e_tamanho = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_tamanho.place(x=650, y=40)

# quartos
l_quartos = Label(frameCadastro, text='Quartos:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_quartos.place(x=550, y=70)
e_quartos = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_quartos.place(x=650, y=70)

# suites
l_suites = Label(frameCadastro, text='Suítes:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_suites.place(x=550, y=100)
e_suites = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_suites.place(x=650, y=100)

# banheiros
l_banheiros = Label(frameCadastro, text='Banheiros:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_banheiros.place(x=550, y=130)
e_banheiros = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_banheiros.place(x=650, y=130)

# vagas
l_vagas = Label(frameCadastro, text='Vagas:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_vagas.place(x=550, y=160)
e_vagas = Entry(frameCadastro, width=10, justify='left', relief=SOLID)
e_vagas.place(x=650, y=160)

# portaria
l_portaria = Label(frameCadastro, text='Portaria:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_portaria.place(x=770, y=190)
e_portaria = StringVar()
b_portaria = Checkbutton(frameCadastro, variable=e_portaria, onvalue="S", offvalue="N")
b_portaria.place(x=890, y=190)

# elevador
l_elevador = Label(frameCadastro, text='Elevador:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_elevador.place(x=770, y=10)
e_elevador = StringVar()
b_elevador = Checkbutton(frameCadastro, variable=e_elevador, onvalue="S", offvalue="N")
b_elevador.place(x=890, y=10)

# gas
l_gas = Label(frameCadastro, text='Gás Encanado:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_gas.place(x=770, y=40)
e_gas = StringVar()
b_gas = Checkbutton(frameCadastro, variable=e_gas, onvalue="S", offvalue="N")
b_gas.place(x=890, y=40)

# gerador
l_gerador = Label(frameCadastro, text='Gerador:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_gerador.place(x=770, y=70)
e_gerador = StringVar()
b_gerador = Checkbutton(frameCadastro, variable=e_gerador, onvalue="S", offvalue="N")
b_gerador.place(x=890, y=70)

# portaoEletronico
l_portaoEletronico = Label(frameCadastro, text='Portão Eletrônico:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_portaoEletronico.place(x=770, y=100)
e_portaoEletronico = StringVar()
b_portaoEletronico = Checkbutton(frameCadastro, variable=e_portaoEletronico, onvalue="S", offvalue="N")
b_portaoEletronico.place(x=890, y=100)

# salaoFestas
l_salaoFestas = Label(frameCadastro, text='Salão de Festas:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_salaoFestas.place(x=770, y=130)
e_salaoFestas = StringVar()
b_salaoFestas = Checkbutton(frameCadastro, variable=e_salaoFestas, onvalue="S", offvalue="N")
b_salaoFestas.place(x=890, y=130)

# areaLazer
l_areaLazer = Label(frameCadastro, text='Área de Lazer:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_areaLazer.place(x=770, y=160)
e_areaLazer = StringVar()
b_areaLazer = Checkbutton(frameCadastro, variable=e_areaLazer, onvalue="S", offvalue="N")
b_areaLazer.place(x=890, y=160)

# Criando Botoes

# Botao Carregar
l_carregar = Label(frameCadastro, text='Imagem:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=930, y=10)
b_carregar = Button(frameCadastro,command=escolher_imagem, width=30, text='CARREGAR', compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=1000, y=10)

# Botao Inserir
img_add = Image.open('imagens\iconsAdd.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameCadastro, command=inserir, image=img_add, width=95, text='  ADICIONAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=790, y=220)

# Botao Atualizar
img_atualizar = Image.open('imagens\iconAtualizar.png')
img_atualizar = img_atualizar.resize((20,20))
img_atualizar = ImageTk.PhotoImage(img_atualizar)

b_atualizar = Button(frameCadastro, command=atualizar, image=img_atualizar, width=95, text='  ATUALIZAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=790, y=260)

# Botao Deletar
img_deletar = Image.open('imagens\iconDelete.png')
img_deletar = img_deletar.resize((20,20))
img_deletar = ImageTk.PhotoImage(img_deletar)

b_deletar = Button(frameCadastro,command=deletar, image=img_deletar, width=95, text='  DELETAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=790, y=300)

# Botao pesquisar
img_pesquisar = Image.open('imagens\iconSearch.png')
img_pesquisar = img_pesquisar.resize((20,20))
img_pesquisar = ImageTk.PhotoImage(img_pesquisar)

b_pesquisar = Button(frameCadastro, image=img_pesquisar, width=95, text='  pesquisar', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_pesquisar.place(x=790, y=340)

# Ver Item
img_verItem = Image.open('imagens\iconSelect.png')
img_verItem = img_verItem.resize((20,20))
img_verItem = ImageTk.PhotoImage(img_verItem)

b_verItem = Button(frameCadastro,command=ver_imagem, image=img_verItem, width=95, text='  VER ITEM', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_verItem.place(x=790, y=380)

# Tabela
def mostrar():

    #creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome', 'Cidade', 'Bairro', 'Logradouro', 'Nº','CEP', 'Ano', 'Andares', 'Und/Andar', 'Torres', 'Valor', 'Condomínio', 'IPTU', 'Tipo', 'Tamanho', 'Quartos', 'Suítes', 'Banheiros', 'Vagas', 'Portaria', 'Elevador', 'Gás Encanado', 'Gerador', 'Portão Eletrônico', 'Salão de Festas', 'Área de Lazer', 'Descrição','Imagem']

    lista_itens = verForm()

    global tree

    tree = ttk.Treeview(frameBancoDados, selectmode="extended",columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frameBancoDados, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameBancoDados, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky=NSEW)
    vsb.grid(column=1, row=0, sticky=NS)
    hsb.grid(column=0, row=1,sticky=EW)
    frameBancoDados.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center","center"]
    h=[40,150,150,150,150,40,100,60,60,75,60,85,80,80,50,50,50,50,50,50,50,50,50,50,50,50,50,300,300]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    #inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


mostrar()


janela.mainloop()

