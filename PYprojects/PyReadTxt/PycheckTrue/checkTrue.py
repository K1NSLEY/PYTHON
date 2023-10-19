def Nome():
    nome1=input("Digite o primeiro nome: ")
    nome2=input("Digite o segundo nome: ")
    nome3=input("Digite o terceiro nome: ")
    print('O nome é: ',nome1,nome2,nome3)

def Pesquisador():
    curso=input("Qual curso está cursando: ")
    ano=(2023)
    inicio=input("Começou em que ano? ")
    fim=3+int(inicio)
    print("Você começou em ", inicio,"Está cursando: ", curso, " e terminará em ",fim)
def Idade():
    ano=input("Em que ano você nasceu? ")
    idade=2023-int(ano)
    if idade >=18:
        print("Você tem ", idade,"anos. Meus parabéns! De maior, já pode Hibilitação.")
    else:
        print("Você tem ", idade,"anos. Sem parabéns. Criança.")
while True:
    mensagem = input("Bem Vindo ao teste do Kinsley, Digite M para ver o Menu, ou S para sair: ")
    if mensagem == 'm'or mensagem =='M':
        print("Bem Vindo ao Menu!")
        print("1° - Digite 'N' para ir ao montador de nomes: ")
        print("2° - Digite 'P' para ir ao Pesquisador de Cursos")
        print("3° - Digite 'I' para descobrir sua idade")
        menu=input("Para onde deseja ir?")
    if menu == 'n'or menu=='N'or menu=='1':
        Nome()
    if menu == 'p'or menu=='P'or menu=='2':
        Pesquisador()
    if menu == 'i'or menu=='I'or menu=='3':
        Idade()