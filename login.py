import requests
import variables

def login():
    res_login = requests.post(
        url=f'{variables.BASE_URL}/api/login/',
        json={
            "username": "admin",
            "password": "admin"
        }
    )
    print(res_login)
    print(res_login.text)
    token = res_login.json()['access']
    return token



