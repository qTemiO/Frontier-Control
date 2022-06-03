from django.test import TestCase

import requests, json

# requests.post(
#     'http://127.0.0.1:8000/filter/recommend/', 
#     json={'data': 'КОЛЛАЖИ'}
#     )
# requests.post(
#     'http://127.0.0.1:8000/filter/recommend/', 
#     json={'data': 'РИСУНКИ, РОССИЯ, САНКТ-ПЕТЕРБУРГ'}
#     )
# requests.post(
#     'http://127.0.0.1:8000/filter/recommend/', 
#     json={'data': 'живописная работа картина современного художника соловьева холст масло россия санкт-петербург 2018'}
#     )

requests.get('http://127.0.0.1:8000/filter/recommendUser/$query=123/')