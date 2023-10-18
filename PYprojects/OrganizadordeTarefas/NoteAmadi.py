import msvcrt

def obter_tecla():
    return msvcrt.getch()

print("Digite algo (pressione Esc para sair):")

while True:
    tecla = obter_tecla()

    if tecla ==  b'\x1b':
        print("\nEscPress")
    break