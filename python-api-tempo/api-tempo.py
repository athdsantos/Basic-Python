from requests import get
from json import loads
from pprint import pprint

def get_request():
  try:
    req = get('http://api.openweathermap.org/data/2.5/weather?q=Brasilia&appid=29a246b1b59f2718d4e4c81c23a8e5a9')
    if 200 >= req.status_code <= 299:
      return_request()
    else:
      print('ERRO! A requisição falhou!')
  except Exception as erro:
    print(f'ERRO! {erro}')

def return_request():
  try:
    cidade = str(input('Cidade: ').capitalize())
    req = get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=29a246b1b59f2718d4e4c81c23a8e5a9')
    # print(req.status_code)
    for_dict = loads(req.text)
    # pprint(for_dict)
    print(f'Coord [long]: {for_dict["coord"]["lon"]}')
    print(f'Coord [lat]: {for_dict["coord"]["lat"]}')
    print(f'Weather main: {for_dict["weather"][0]["main"]}')
    print(f'Weather description: {for_dict["weather"][0]["description"]}')
    print(f'Main Temp: {float(for_dict["main"]["temp"]) - 273.15:.1f} ºC')
    print(f'Main temp min: {float(for_dict["main"]["temp_min"]) - 273.15:.1f} ºC')
    print(f'Main temp max: {float(for_dict["main"]["temp_max"]) - 273.15:.1f} ºC')
    print(f'Humidity: {for_dict["main"]["humidity"]}%')
    #for chave, valor in for_dict.items():
      #print(f'{chave} : {valor}')
  except Exception as erro:
    print(f'ERRO! {erro}')


get_request()