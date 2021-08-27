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
valor = []
quantidade = []
conta = []

######### PARTE DE CODIGO QUE CAPTURA E PROCESSA OS DADOS IMPUTADOS PELO USUARIO  ##########
def prod():
    
    ###  EXIBE TEXTO NA JANELA DO PROGRAMA  ###
    lb_produto = Label(mercado, text='PRODUTO :')   
    lb_valor = Label(mercado, text='VALOR :')
    lb_quantidade = Label(mercado, text='QUANTIDADE :')
    
    ### CAMPOS PARA ENTRADA DE DADOS PELO USUARIO ###
    ent_valor = Entry(mercado, width = 10)          
    ent_quantidade = Entry(mercado, width = 10)     
    ent_produto = Entry(mercado, width = 10)        
    
    ### POSICIONA LABEL NA JANELA ###
    lb_produto.grid(row = 1, column =1)             
    lb_valor.grid(row = 2, column =1)
    lb_quantidade.grid(row = 3, column =1)
    
    ### POSICIONA O CAMPO "ENTRY", DE ENTRADA DE DADOS NA JANELA ### 
    ent_produto.grid(row = 1, column =2)
    ent_valor.grid(row = 2, column =2)
    ent_quantidade.grid(row = 3, column =2)
    
    
    ##### FUNÇÃO QUE EXECUTA CALCULOS, E ATRIBUI VALORES AS VARIAVEIS #####
    def calc_item():
        valor2 = float(ent_valor.get())                     ### CAPTURA O VALOR DIGITADO PELO USUARIO APÓS PRESSIONAR "BOTAO SALVAR" ###
        quantidade2 = int(ent_quantidade.get())             ### CAPTURA A QUANTIDADE DIGITADA PELO USUARIO APÓS PRESSIONAR "BOTAO SALVAR" ###
        calculo = quantidade2 * valor2                      ### EXECUTA CALCULO DE DUAS VARIAVEIS ###
        conta.append(calculo)                               ### ATRIBUI O RESULTADO DE "CALCULO" A LISTA PRRA USO FURUTO ###
        produto2 = ent_produto.get()                        ### CAPTURA NOME DO PRODUTO DIGITADO PELO USUARIO APÓS PRESSIONAR "BOTAO SALVAR" ###
        produto.append(produto2)                            ### ATRIBUI O NOME DO PRODUTO DIGITADO PELO USUARIO EM UMA LISTA PARA USO FUTURO ###
        lb_total_item1 = Label(mercado, text = produto2)    ####################################################################################
        lb_total_item1.grid(row = 4, column = 1)            # EXIBE NOME DO PRODUTO                                                            #
        lb_total_item = Label(mercado, text=calculo)        #                   E O RESULTADO DO CALCULO ENTRE VALOR E QUANTIDADE              #
        lb_total_item.grid(row = 4, column =2)              ####################################################################################
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

