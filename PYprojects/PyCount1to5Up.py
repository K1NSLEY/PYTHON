# Lista de dicionários contendo as informações dos membros
members = [
    {"name": "Maria Luiza", "age": 18, "surname": "Mello"},
    {"name": "Kinsley Chinda", "age": 18, "surname": "Amadi"},
    {"name": "João Gabriel Felix", "age": 17, "surname": "Fernandes"},
    {"name": "Luís Gabriel", "age": 17, "surname": "Oliveira"},
    {"name": "Giovanna de Oliveira", "age": 17, "surname": "Gamberini"}
]

while True:
    mensagem = input("Escolha de 1 a 5 (ou 'q' para sair): ")

    if mensagem.lower() == 'q':
        break  # Sai do loop se o usuário digitar 'q'
    
    # Verifica se a entrada é um número entre 1 e 5
    if mensagem.isdigit():
        indice = int(mensagem) - 1  # Converte para índice (0 a 4)
        if 0 <= indice < len(members):
            member = members[indice]
            print(f"Member: {member['name']} {member['surname']} {member['age']} anos")
        else:
            print("Número fora do intervalo (1 a 5)")
    else:
        print("Entrada inválida, tente novamente.")
