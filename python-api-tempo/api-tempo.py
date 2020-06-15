from requests import get
from json import loads
from pprint import pprint

def get_request():
  try:
    req = get('http://api.openweathermap.org/data/2.5/weather?q=Brasilia&appid=your_id')
    if 200 >= req.status_code <= 299:
      return_request()
    else:
      print('ERROR! The site is down!')
  except Exception as error:
    print(f'ERROR! {error}')

def return_request():
  try:
    city = str(input('City: ').capitalize())
    req = get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=your_id')
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
  except Exception as error:
    print(f'ERROR! {error}')


get_request()
