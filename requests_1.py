import requests
import datetime

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
log = open(f'{datetime.datetime.now().strftime("%y-%m-%d")}.txt', 'a+')
url = input('please enter a site to check: ')
url = 'https://'+url

time = datetime.datetime.now().strftime('%H:%M:%S')
res = requests.get(url)

log.write(f'{time} {url} method : GET {res.status_code}\n')

