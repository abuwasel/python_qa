import requests
import datetime
import time

# ------- copy the content of the html pages ------
# response = requests.get('https://www.google.com')
# sc = response.status_code
# if sc <= 400:
#     print('passed')
#     file = open('google.html', 'w+')
#     file.write(response.text)
# else:
#     print('failed')

# ------ log file to http request module ---------
# log = open(f'{datetime.datetime.now().strftime("%y-%m-%d")}.txt', 'a+')
# url = input('please enter a site to check: ')
# url = 'https://'+url
#
# time = datetime.datetime.now().strftime('%H:%M:%S')
# res = requests.get(url)
#
# log.write(f'{time} {url} method : GET {res.status_code}\n')

#---------------------
# start_time = time.time()
# res = requests.get('https://ynet.co.il')
# end_time = time.time()
#
# print(end_time - start_time)


# url = 'https://jsonplaceholder.typicode.com/users/1'
# res = requests.get(url)
# data = res.json()
#
# print(data['name'])
# print(data['address']['geo']['lat'])


url = 'https://jsonplaceholder.typicode.com/users'
res = requests.get(url)
users = res.json()

print(f'You have {len(users)} users')
i =0
for user in users:
    i += 1
    print(f'{i}- {user["name"]}')


