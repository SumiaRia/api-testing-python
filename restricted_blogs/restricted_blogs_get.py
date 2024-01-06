import requests
import variables

def restricted_blogs_get(access_token):
    res = requests.get(
        url=f'{variables.BASE_URL}/api/restricted-blogs/',
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    ) 
    print("status Code:", res.status_code)
    print(res.text)
    assert res.status_code == 200
