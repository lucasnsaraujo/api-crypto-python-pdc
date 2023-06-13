import requests
import json

API_KEY = '3694fcdc20d319a2d6b81a59'
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

def fetch_exchange_rate(rate):
  url = API_URL + rate

  response = requests.get(url)
  data = response.json()

  if response.status_code == 200:
    rates = data['conversion_rates']
    print(f"1 {rate} = {rates['BRL']:.2f} BRL (reais brasileiros)")
    print(f"1 {rate} = {rates['EUR']:.2f} EUR (euros)")
    print(f"1 {rate} = {rates['JPY']:.2f} JPY (ienes japoneses)")
  else:
      print("Ocorreu um erro ao obter as taxas de câmbio.")

fetch_exchange_rate('USD')