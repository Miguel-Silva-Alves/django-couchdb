import requests
import random

URL = 'http://127.0.0.1:8000/'

# for __ in range(10):




# #================================== POST DATA ========================================
# value = random.uniform(1.0, 40.0)
# print(value)
# data = {
#     'dado':round(value, 2),
#     'id_dispositivo_ip':'bunda'
# }

# request = requests.post(URL+'telemetria/', data=data)
# print(request.json())

# ================================== GET DATA ========================================

data = {
    'busca':'id_dispositivo_ip',
    'valor':'bunda'
}

request = requests.get(URL+'telemetria/', data=data)
print(request.json())

