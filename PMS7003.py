# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:41:29 2023

@author: emmab
"""


import serial
import time
#Capteur de particules fines PMS7003

ser = serial.Serial(
        port='/dev/ttyAMA0',  # le port série sur lequel le capteur est connecté
        baudrate = 9600,   # la vitesse de transmission des données
        parity=serial.PARITY_NONE, # Le bit de parité est utilisé pour détecter les erreurs de transmission, mais il n'est pas nécessaire dans ce cas car le capteur PMS7003 ne l'utilise pas.
        stopbits=serial.STOPBITS_ONE, #cela indique qu'il y a un seul bit de stop dans la communication série. Le bit de stop est utilisé pour indiquer la fin d'un octet de données.
        bytesize=serial.EIGHTBITS, # cela indique que chaque octet de données est codé sur 8 bits. Le capteur PMS7003 envoie des données sur 32 octets, donc chaque octet doit être lu sur 8 bits.
        timeout=1 #cela indique le temps d'attente maximal en secondes pour la lecture des données envoyées par le capteur. Si aucune donnée n'est reçue pendant ce temps, la lecture s'arrête et le programme passe à l'étape suivante. Cela permet d'éviter que le programme ne reste bloqué à attendre des données qui ne viendront jamais. 
)

while True:
    # Lecture des données envoyées par le capteur
    data = ser.read(32)

    # Vérification de la longueur des données
    if len(data) >= 14:  # Vérifie si au moins 14 octets sont reçus
        # Extraction des valeurs de taux de particules fines
        pm25_high = data[10]
        pm25_low = data[11]
        pm25 = (pm25_high << 8) + pm25_low

        pm10_high = data[12]
        pm10_low = data[13]
        pm10 = (pm10_high << 8) + pm10_low

        # Affichage des valeurs lues
        print("Taux de particules fines PM2.5 : ", pm25)
        print("Taux de particules fines PM10 : ", pm10)
    elif(len(data)==0):
        print("ERRREUR PAS DE DATA")
    else:
        print("Données insuffisantes")

    # Attente de 2 secondes avant la prochaine lecture
    time.sleep(2)

