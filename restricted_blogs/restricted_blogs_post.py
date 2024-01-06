import requests
import variables

def restricted_blogs_post(access_token):
    payload = {
        "title": "heart-attack",
        "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi tempora, fugit, consequatur eligendi ea iure provident quod inventore quas debitis voluptatibus, culpa pariatur aspernatur esse qui assumenda ex quidem tenetur! Quisquam doloremque vero dolorem obcaecati expedita blanditiis sunt animi quidem enim architecto similique repellat saepe, ea pariatur cupiditate nihil fugit laudantium eum soluta culpa cum autem unde quibusdam. Similique nam dolores reiciendis delectus. Vitae beatae, consectetur nostrum numquam nihil explicabo omnis iste perspiciatis deleniti molestias quas dolores tempora, ex voluptatum? Nulla fugiat nihil, iusto nostrum reiciendis consectetur. Nesciunt unde aut corporis iste atque nulla, illum consequatur facilis dolores dicta optio.",
        "therapist": 1
    }
    res = requests.post(
        url=f"{variables.BASE_URL}/api/restricted-blogs/",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json=payload
    )
    print("status Code:", res.status_code)
    print(res.text)
    assert res.status_code == 201
    assert res.json()["title"] == payload["title"]
    assert type(res.json()["id"]) == int
    blog_id = res.json()["id"]
    return blog_id, payload
