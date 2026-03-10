# Importandao a biblioteca requests
import requests

# Consulta a API ViaCEP para obter informações de um CEP específico.
def get_cep(cep):
    
    # URL a ser consultada
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # Envia uma requisição HTTP GET para buscar dados na URL
        response = requests.get(url, timeout=5)

        # Se a API retornar um código de erro (4xx ou 5xx), lança uma exceção
        # Transformar erros HTTP em exceções Python
        response.raise_for_status()

        # Converte a resposta JSON(String) em um dicionário Python
        data = response.json()

        # O ViaCEP retorna {'erro': 'true'} em vez de erro HTTP para CEPs inexistentes
        if "erro" in data:
            print("CEP não encontrado!")
            return None
        
        # Dados do endereço se encontrado.
        return data
        
    except requests.exceptions.HTTPError as error:
        # Erros de status HTTP
        print(f"Erro HTTP: {error}")
    except requests.exceptions.ConnectionError:
        # Problemas de internet
        print(f"Erro de conexão")
    except requests.exceptions.Timeout:
        # O servidor demorou mais que os 5 segundos definidos
        print(f"O tempo de resposta expirou.")
    except Exception as error:
        # Captura qualquer outro erro inesperado
        print(f"Erro inesperado: {error}")

if __name__ == "__main__":

    data = None

    # Obtendo CEP a ser consultado
    cep = str(input("Digite seu CEP: ")).strip().replace("-", "")
    
    # Verificando se o CEP é valido
    # isdigit() verifica se todos os caracteres em uma string são dígitos (0-9)
    if len(cep) == 8 and cep.isdigit():
        # Armazenando as informações retornadas
        data = get_cep(cep)

        # Vericando se a variavel não esta vazia
        if data:
            print(f"\nCEP: {data['cep']}")
            print(f"Estado (UF): {data['uf']}")
            print(f"Cidade: {data['localidade']}")
            print(f"Bairro: {data['bairro']}")
            print(f"Logradouro: {data['logradouro']}")
            print(f"DDD: {data['ddd']}")
    else:
        print("O CEP deve conter exatamente 8 números")