# -*- coding: utf-8 -*-

''' 

@author: Samuel Buzon Gil

ÚLTIMA MODIFICACIÓN: 06/12/2020

Archivo con pruebas para el proyecto de Youtube_data


'''
import csv
# from matplotlib import pyplot as plt
from collections import namedtuple
import datetime

Registro = namedtuple('Registro', 'url,Timestamp,Title,Views,upload_date,Likes,Dislikes,Comments')
########################################################################################
def lee_registros(fichero):
    ''' Lectura del fichero y carga y devolución de una lista con todos los registros leídos.
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de tuplas (url,Timestamp,Title,Views,upload_date,Likes,Dislikes,Comments) -> 
                            -> [(str, dateTime, str, int, dateTime, int, int, str)]

    datetime.datetime.strptime(upload_date, '%d %m %Y')
    '''
    with open(fichero, encoding='utf-8') as f:

        lectura = csv.reader(f)
    
        for i in lectura:
            Registros = [Registro(url,datetime.datetime.strptime(Timestamp, '%d/%m/%Y %H:%M:%S'),Title,Views
            ,upload_date,Likes,Dislikes,Comments)
             for url,Timestamp,Title,Views,upload_date,Likes,Dislikes,Comments in lectura]
            print(Registros)
        return Registros

        

