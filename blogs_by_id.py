import requests

res_blog_id = requests.get('https://deyal-service.zayedabdullah.com/api/blogs/2970/')
print("show the blogs id:",res_blog_id.json())
print("Status code:",res_blog_id.status_code)
assert res_blog_id.status_code == 200
