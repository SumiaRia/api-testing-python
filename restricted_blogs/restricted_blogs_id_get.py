import requests
import variables


def restricted_blogs_id_get(access_token, created_blog_id, blog_data):
    res = requests.get(
        url=f"{variables.BASE_URL}/api/restricted-blogs/{created_blog_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    print(res.text)
    assert res.status_code == 200
    assert res.json()["id"] == created_blog_id
    assert res.json()["title"] == blog_data["title"]

