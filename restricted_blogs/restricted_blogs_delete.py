import requests
import variables


def restricted_blogs_delete(access_token, created_blog_id):
    res = requests.delete(
        url=f'{variables.BASE_URL}/api/restricted-blogs/{created_blog_id}/',
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    ) 
    print("status Code:", res.status_code)
    print(res.text)
    assert res.status_code == 204 
    #checking whether id is deleted or not
    res = requests.get(
        url=f"{variables.BASE_URL}/api/restricted-blogs/{created_blog_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    assert res.status_code == 404
