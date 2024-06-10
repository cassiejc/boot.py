

import time
from simple import MQTTClient
import ubinascii
import machine
import micropython
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'IoT_Dev'
password = 'elektro234'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,password)

while station.isconnected() == False:
  pass
  
print("CONNECTED")
print(station.ifconfig())




mqtt_server = '192.168.41.106'

client_id = ubinascii.hexlify(machine.unique_id())



