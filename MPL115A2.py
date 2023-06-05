# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:42:33 2023

@author: emmab
"""


import adafruit_mpl115a2
import math
import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)
# Initialisez le capteur.
sensor = adafruit_mpl115a2.MPL115A2(i2c)

# Récupérez les données de pression.
pressure = sensor.pressure

# Affichez les données de pression.
print('Pression = ' ,pressure,'Pa')

P0 = 101400  # pression atmosphérique standard en pascal
R = 287.058  # constante des gazs parfaits en J/(kg*K)
temperature = 25  # Température en degrés Celsius (remplace cette valeur par la température réelle)
Tk = 273.15 + temperature  # Température en Kelvin
P = pressure
rho = (P / (R * Tk))  # densité de l'air kg/m^3
V = (math.sqrt(2 * (P0 - P) / rho) * 3.6)/1000 # vitesse du vent en m/s
print(V)


