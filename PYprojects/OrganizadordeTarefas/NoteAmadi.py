import msvcrt

def obter_tecla():
    return msvcrt.getch()

print("Digite algo (pressione Esc para sair):")

while True:
    tecla = obter_tecla()

    if tecla == b'a':
        print("\nEncerrando o programa.")
        break