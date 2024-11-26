import requests

def main():
    while True:
        url = "http://127.0.0.1:8000/check-approval/"
        status = input("Digite o status (aprovado/negado): ").strip()
        
        response = requests.post(url, json={"status": status})
        
        if response.status_code == 200:
            print(f"Resposta da API: {response.json()['message']}")
        else:
            print("Erro ao acessar a API")

if __name__ == "__main__":
        main()
main()