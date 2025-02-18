import requests

# URL do servidor (não ajustar/-necessário)
BASE_URL = "http://127.0.0.1:8000"


def GetLogin(User, Password):

    data = {
        "User": User,
        "Password": Password
    }
    
    response = requests.post(f"{BASE_URL}/login", json=data)

    response_data = response.json()
    print(f"Mensagem do login: {response_data['message']}")
    
    return response_data