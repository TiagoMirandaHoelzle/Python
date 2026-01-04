# Importando a biblioteca request
import requests

#Informações da API
api_key = "Sua Chave da API" 
units = "metric"
lang = "pt_br"

def getCityName(city):

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}")

    # 200 é o status de sucesso na comunicação HTTP
    if response.status_code == 200:
        data = response.json()
        
        # Retorna os dados da API em formato JSON
        return data
    else:
        print(f"Falha na requisição: {response.status_code}")    

# Recebe o nome da cidade a ser consultada
cityName = str(input("Digite o nome de uma cidade: ")).strip().capitalize()

# Armazena os dados retornados da função em uma variavel
weatherInfo = getCityName(cityName)

# Verifica se a variável contém dados
if weatherInfo:

    # Acessa as chaves específicas do JSON retornado pela API
    print(f"\nCidade: {weatherInfo['name']}, {weatherInfo['sys']['country']}")
    print(f"Temperatura: {weatherInfo['main']['temp']} Cº")
    print(f"Humidade: {weatherInfo['main']['humidity']} %")
    print(f"Sensação Térmica: {weatherInfo['main']['feels_like']} Cº")
    print(f"Descrição: {weatherInfo['weather'][0]['description']}")
