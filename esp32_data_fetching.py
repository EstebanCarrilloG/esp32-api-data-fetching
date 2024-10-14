import network
import gc
import time
import urequests as requests
import json
from machine import Pin, PWM

gc.collect()

pwm0 = PWM(Pin(0), freq=500, duty=0)
pwm1 = PWM(Pin(2), freq=500, duty=0)
pwm2 = PWM(Pin(4), freq=500, duty=0)

SSID = ''
PASSWORD = ''
URL_API = 'https://example.com/api/data'

def connectWifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        print('Conectando...')
        time.sleep(1)
    print('Conexión establecida. Dirección IP:', station.ifconfig()[0])
    print(f'Conexión exitosa a {ssid}')

def fetchApi(api_url, timeout=20):
    try:
        response = requests.get(api_url, timeout=timeout)
        if response.status_code == 200:
            # print('Respuesta de la API:', response.text)
            return response.text
        else:
            print('Error en la solicitud. Código de respuesta HTTP:', response.status_code)
            return None
    except Exception as e:
        print('Error en la solicitud:', str(e))
        return None

connectWifi(SSID, PASSWORD)

def map_range(x, in_max = 255, out_max = 1023):
  return x * out_max // in_max

while True:
    
    data = fetchApi(URL_API)
   
    if data == "[]": 
        break

    data1 = json.loads(data)

    pwm0.duty(map_range(data1[0].get("output1") ))
    pwm1.duty(map_range(data1[0].get("output2") ))
    pwm2.duty(map_range(data1[0].get("output3") ))

    print(map_range(data1[0].get("output1")))
     
    time.sleep(1)
    print(data1[0])

print("Error")