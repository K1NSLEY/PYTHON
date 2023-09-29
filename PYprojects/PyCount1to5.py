name1="Maria Luiza"
age1=18
surname1="Mello"

name2="Kinsley Chinda"
age2=18
surname2="Amadi"

name3="João Gabriel Felix"
age3=17
surname3="Fernandes"

name4="Luís Gabriel"
age4=17
surname4="Oliveira"

name5="Giovanna de Oliveira"
age5=17
surname5="Gamberini"

while True:
    mensagem = input("Escolha de 1 a 5 (ou 'q' para sair): ")

    if mensagem.lower() == 'q':

        if mensagem=="1":
            print(f"Member: {name1} {surname1}, {age1} years old")
        elif mensagem=="2":
            print(f"Member: {name2} {surname2}, {age2} years old")
        elif mensagem=="3":
            print(f"Member: {name3} {surname3}, {age3} years old")
        elif mensagem=="4":
            print(f"Member: {name4} {surname4}, {age4} years old")
        elif mensagem=="5":
            print(f"Member: {name5} {surname5}, {age5} years old")
        else:
            print("Not registered, denied access")