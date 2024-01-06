import requests
from variables import BASE_URL
from login import login
from restricted_blogs.restricted_blogs_get import restricted_blogs_get
from restricted_blogs.restricted_blogs_post import restricted_blogs_post
from restricted_blogs.restricted_blogs_id_get import restricted_blogs_id_get
from restricted_blogs.restricted_blogs_put import restricted_blogs_put


token = login()
restricted_blogs_get(access_token=token)
new_blog_id, data = restricted_blogs_post(access_token=token)
restricted_blogs_id_get (access_token= token, created_blog_id=new_blog_id, blog_data = data)
restricted_blogs_put(access_token=token, created_blog_id=new_blog_id)





