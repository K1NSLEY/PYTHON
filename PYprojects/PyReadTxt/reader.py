# Nome do arquivo de texto a ser verificado
nome_arquivo = "C:\\Users\\kinsb\\OneDrive\\Documentos\\VScode IDE\\PYTHON\\PYprojects\\PyReadTxt\\read.txt"

# Palavra que você deseja verificar no arquivo
palavra_a_verificar = "LUIGHI"

try:
    # Abre o arquivo em modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
        
        # Verifica se a palavra desejada está no conteúdo do arquivo
        if palavra_a_verificar in conteudo:
            print(f"A palavra '{palavra_a_verificar}' foi encontrada no arquivo.")
        else:
            print(f"A palavra '{palavra_a_verificar}' não foi encontrada no arquivo.")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
