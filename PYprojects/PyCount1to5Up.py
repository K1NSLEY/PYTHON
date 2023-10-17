members = [
    {"name": "Maria Luiza", "age": 18, "surname": "Mello"},
    {"name": "Kinsley Chinda", "age": 18, "surname": "Amadi"},
    {"name": "João Gabriel Felix", "age": 17, "surname": "Fernandes"},
    {"name": "Luís Gabriel", "age": 17, "surname": "Oliveira"},
    {"name": "Giovanna de Oliveira", "age": 17, "surname": "Gamberini"}
]

while True:
    mensagem = input("Escolha de 1 a 5 (ou 'Ctrl + C' para sair): ")

    if mensagem.isdigit():
        indice = int(mensagem) - 1
        if 0 <= indice < len(members):
            member = members[indice]
            print(f"Member: {member['name']} {member['surname']} {member['age']} anos")
        else:
            print("Número fora do intervalo (1 a 5) ou 'Ctrl + C' para sair")
    else:
        print("Entrada inválida, tente novamente.")
