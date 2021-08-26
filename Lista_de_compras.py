### MEU PRIMEIRO CODIGO NO GITHUB ###
###                               ###
######  LISTA DE COMPRA GERAL  ######

from tkinter import *          ### COMO ESTE CODIGO UTILIZA INTERFACE GRAFICA ELE PRECISA DA BIBLIOTECA tkinter ####
import math
import datetime                ### para uso futuro ###
from datetime import date      ### para uso futuro ###

##########      INICIO DA CRIAÇÃO DA JANELA      ##########

mercado = Tk()
mercado.title('LISTA DE COMPRA PICKLIS')

'''
PROGRAMA COMPRAS BASICO
'''
produto = []# RECEBE E ARMAZENDA TODOS OS PRODUTOS DIGITADOS PELO USUSARIO #
conta = [] # RECEBE E ARMAZENA OS DADOS PARA CALCULOS #
produto2 = None
#valor2 = 0
valor = []
quantidade = []
#quantidade2 = 0
#calculo = None
#calculo2 = []
conta = []
def prod():
    lb_produto = Label(mercado, text='PRODUTO :')
    lb_produto.grid(row = 1, column =1)
    ent_produto = Entry(mercado, width = 10)
    ent_produto.grid(row = 1, column =2)
    lb_valor = Label(mercado, text='VALOR :')
    ent_valor = Entry(mercado, width = 10)
    lb_quantidade = Label(mercado, text='QUANTIDADE :')
    ent_quantidade = Entry(mercado, width = 10)
    lb_valor.grid(row = 2, column =1)
    ent_valor.grid(row = 2, column =2)
    lb_quantidade.grid(row = 3, column =1)
    ent_quantidade.grid(row = 3, column =2)

    def calc_item():
        valor2 = float(ent_valor.get())
        quantidade2 = int(ent_quantidade.get())
        calculo = quantidade2 * valor2
        conta.append(calculo)
        produto2 = ent_produto.get()
        produto.append(produto2)
        lb_total_item1 = Label(mercado, text = produto2)
        lb_total_item1.grid(row = 4, column = 1)
        lb_total_item = Label(mercado, text=calculo)
        lb_total_item.grid(row = 4, column =2)

        #def total():
        print('estou sendo executado a cada click')

        calculo2 = list(map(float, conta))
        total = sum(calculo2)
        lb_total_g = Label(mercado, text = 'TOTAL DA COMPRA: R$')
        lb_total_g.grid(row = 5, column = 1)
        lb_total_geral = Label(mercado, text=total)
        lb_total_geral.grid(row = 5, column = 2)
        #print(calculo, produto,'total: ', conta)
    bt_qtde = Button(mercado, text='salvar', command=calc_item)
    bt_qtde.grid(row = 2, column = 3)
    #bt_qtde = Button(mercado, text='salvar', command=total)
    #bt_qtde.grid(row = 5, column = 2)
    lb_total_item1 = Label(mercado, text = '                                      ')
    lb_total_item1.grid(row = 4, column = 1)
    lb_total_item = Label(mercado, text="                                         ")
    lb_total_item.grid(row = 4, column =2)
bt_novo = Button(mercado, text='limpa', command=prod)
bt_novo.grid(row = 17, column = 2)
#prod()



mercado.mainloop()

