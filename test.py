import requests
new_cat = {'name':'skillfactory-check-1'}
new_post = {'title':'Название поста', 'status':'P','content':'Содержание поста', 'category':1}
requests.post('http://127.0.0.1:8000/categories/', data=new_cat)
requests.post('http://127.0.0.1:8000/', data=new_post)