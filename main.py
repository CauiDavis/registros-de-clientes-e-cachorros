from tkinter import scrolledtext
import requests
from tkinter import *
from modelos.cachorro import cachorro
from modelos.cachorroDAO import cachorroDAO
from modelos.cliente import cliente
from modelos.clienteDAO import clienteDAO

def cadastrar():
    nomecliente = entrada1.get()
    telefone = entrada2.get()
    nomecachorro = entrada3.get()
    idade = entrada4.get()
    Cliente = cliente(id=None,nome = nomecliente,telefone= telefone)
    Cachorro = cachorro(id=None, nome= nomecachorro,idade=idade,idcliente=None)
    dao_cliente = clienteDAO()
    dao_cliente.registrar1(Cliente)
    dao_cachorro = cachorroDAO()
    dao_cachorro.registrar(Cachorro)
def listar():
    clientedao = clienteDAO()
    cachorrodao = cachorroDAO()
    resultado1 = clientedao.listar()
    resultado2 = cachorrodao.listar()
    caixa_de_texto1.insert(INSERT,resultado1)
    caixa_de_texto2.insert(INSERT,resultado2)
def buscar_cliente():
    id = entrada5.get()
    dao = clienteDAO()
    resultado = dao.buscar_cliente(id)
    resposta1["text"] = resultado
def buscar_cachorro():
    id = entrada6.get()
    dao = cachorroDAO()
    resultado = dao.buscar_cachorro(id)
    resposta2["text"] = resultado
def deletar_cliente():
    id = entrada7.get()
    dao = clienteDAO()
    dao.deletar_cliente(id)
def deletar_cachorro():
    id = entrada8.get()
    dao = cachorroDAO()
    dao.deletar_cachorro(id)

#while(True):
    #print("1-cadastrar cliente e cachorro|2-listar cliente e cachorro|3-buscar cliente")
    #print("4-buscar cachorro|5-deletar cliente|6-deletar cachorro")
    #opc = input("selecionar a opção que voce quer\n")
    #if (opc =='1'):
        #cadastrar()
    #elif(opc=='2'):
        #listar()
    #elif(opc=='3'):
        #buscar_cliente()
    #elif(opc=='4'):
        #buscar_cachorro()
    #elif(opc=='5'):
        #deletar_cliente()
    #elif(opc=='6'):
        #deletar_cachorro()
    #else:
       # exit()
def limpar_caixa_de_texto():
    caixa_de_texto1.delete(1.0,END)
    caixa_de_texto2.delete(1.0,END)
janela = Tk()
janela.title("registro de cliente e cachorro")
janela.geometry("400x550")
informacao1 = Label(janela,text="nome do cliente:")
informacao1.grid(column=0,row=0)
entrada1 = Entry(janela,font="arial 10 bold")
entrada1.grid(column=1,row=0)
informacao2 = Label(janela,text="telefone do cliente:")
informacao2.grid(column=0,row=1)
entrada2 = Entry(janela,font="arial 10 bold")
entrada2.grid(column=1,row=1)
informacao3 = Label(janela,text="nome do cachorro:")
informacao3.grid(column=0,row=2)
entrada3 = Entry(janela,font="arial 10 bold")
entrada3.grid(column=1,row=2)
informacao4 = Label(janela,text="idade do cachorro:")
informacao4.grid(column=0,row=3)
entrada4 = Entry(janela,font="arial 10 bold")
entrada4.grid(column=1,row=3)
botao1 = Button(janela,text="adicionar cliente",command=cadastrar)
botao1.grid(column=1,row=4)
informacao5 = Label(janela,text="id do cliente para buscar:")
informacao5.grid(column=0,row=5)
entrada5 = Entry(janela,font="arial 10 bold")
entrada5.grid(column=1,row=5)
botao2 = Button(janela,text="buscar cliente",command=buscar_cliente)
botao2.grid(column=1,row=6)
resposta1 = Label(janela,text="cliente:",bg="white")
resposta1.grid(column=0,row=7)
informacao6 = Label(janela,text="id do cachorro para buscar:")
informacao6.grid(column=0,row=8)
entrada6 = Entry(janela,font="arial 10 bold")
entrada6.grid(column=1,row=8)
botao3 = Button(janela,text="buscar cachorro",command=buscar_cachorro)
botao3.grid(column=1,row=9)
resposta2 = Label(janela,text="cachorro:",bg="white")
resposta2.grid(column=0,row=10)
informacao7 = Label(janela,text="id do cliente para deletar:")
informacao7.grid(column=0,row=11)
entrada7 = Entry(janela,font="arial 10 bold")
entrada7.grid(column=1,row=11)
botao4 = Button(janela,text="excluir cliente",command=deletar_cliente)
botao4.grid(column=1,row=12)
informacao8 = Label(janela,text="id do cachorro para deletar:")
informacao8.grid(column=0,row=13)
entrada8 = Entry(janela,font="arial 10 bold")
entrada8.grid(column=1,row=13)
botao5 = Button(janela,text="excluir cachorro",command=deletar_cachorro)
botao5.grid(column=1,row=14)
botao6 = Button(janela,text="listar cliente e cachorro",command=listar)
botao6.grid(column=0,row=15)
botao7 = Button(janela,text="limpar",command=limpar_caixa_de_texto)
botao7.grid(column=0,row=16)
caixa_de_texto1 = scrolledtext.ScrolledText(janela,width=25,height=5)
caixa_de_texto1.grid(column=1,row=16)
caixa_de_texto2 = scrolledtext.ScrolledText(janela,width=25,height=5)
caixa_de_texto2.grid(column=1,row=17)
janela.mainloop()