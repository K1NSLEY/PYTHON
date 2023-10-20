import os
import time
def Nome():
    nome1=input("Digite o primeiro nome: ")
    nome2=input("Digite o segundo nome: ")
    nome3=input("Digite o terceiro nome: ")
    print('O nome é: ',nome1,nome2,nome3)
    time.sleep(3)

def Pesquisador():
    curso=input("Qual curso está cursando: ")
    ano=(2023)
    inicio=input("Começou em que ano? ")
    fim=3+int(inicio)
    print("Você começou em ", inicio,"Está cursando: ", curso, " e terminará em ",fim)
    time.sleep(3)
def Idade():
    ano=input("Em que ano você nasceu? ")
    idade=2023-int(ano)
    if idade >=18:
        print("Você tem ", idade,"anos. Meus parabéns! De maior, já pode Hibilitação.")
    else:
        print("Você tem ", idade,"anos. Sem parabéns. Criança.")
    time.sleep(3)
def Calc():
    valor1=input("Digite 'ON'ou 'OFF': ")
    valor2=input("Digite o Segundo Valor: ")
    selector=input("Como deseja Calcular?\n1° AND\n2° OR\n3° NOT\n4° XOR\n5° NAND\n6° NOR: ")
    if valor1=='on'or valor1=='ON'or valor1=='On'or valor1=='oN'or valor1=='1'or valor1=='True':
        valor1=True
    if valor2=='off'or valor2=='OFF'or valor2=='Off'or valor2=='oFf'or valor2=='OfF'or valor2=='ofF'or valor2=='oN'or valor2=='0'or valor2=='False':
        valor2=False
    if selector== 'x'or selector=='AND'or selector=='ANd'or selector=='AnD'or selector=='aND'or selector=='And'or selector=='anD'or selector=='and':
        print("Você selecionou And")
        time.sleep(1)
        print("A soma das portas lógiacas: ",valor1," x ",valor2,"resulta em:")
        resultado=valor2 and valor1
        if resultado ==True:
            print('Verdadeiro')
        if resultado ==False:
            print('Falso')
time.sleep(5)

while True:
    os.system('cls')
    print("""\n██╗  ██╗██╗███╗   ██╗███████╗██╗     ███████╗██╗   ██╗
██║ ██╔╝██║████╗  ██║██╔════╝██║     ██╔════╝╚██╗ ██╔╝
█████╔╝ ██║██╔██╗ ██║███████╗██║     █████╗   ╚████╔╝ 
██╔═██╗ ██║██║╚██╗██║╚════██║██║     ██╔══╝    ╚██╔╝  
██║  ██╗██║██║ ╚████║███████║███████╗███████╗   ██║   
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝   ╚═╝  
""")
    mensagem = input("Bem Vindo ao teste do Kinsley, Digite M para ver o Menu, ou S para sair: ")
    if mensagem == 'm'or mensagem =='M':
        os.system('cls')
        print("""\n███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
""")
        print("Bem Vindo ao Menu!")
        print("1° - Digite 'N' para ir ao montador de nomes: ")
        print("2° - Digite 'P' para ir ao Pesquisador de Cursos")
        print("3° - Digite 'I' para descobrir sua idade")
        print("4° - Digite 'C' para descobrir sua idade")
        menu=input("Para onde deseja ir?")
    if menu == 'n'or menu=='N'or menu=='1':
        Nome()
    if menu == 'p'or menu=='P'or menu=='2':
        Pesquisador()
    if menu == 'i'or menu=='I'or menu=='3':
        Idade()
    if menu == 'c'or menu=='C'or menu=='4':
        Calc()
    if menu == 's'or menu=='S'or menu=='0':
        exit()