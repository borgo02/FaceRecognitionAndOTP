import requests

code = 668023
r = requests.get(f'https://pyotp-service.azurewebsites.net/api/http_trigger?code={code}')
print(r.status_code)
print(r.headers)
print(r.text[0:1000])