# -*- coding: utf-8 -*-
'''

@author: Samuel Buzon Gil

ÚLTIMA MODIFICACIÓN: 06/12/2020

Archivo con pruebas para el proyecto de Youtube_data
'''
from sambuzgil import *

################################################################
#  Funciones auxiliares
################################################################
def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 
################################################################
#  Funciones de test
################################################################
def test_lee_registros():
    print("Leidos " , len (REGISTROS), "datos de youtube")

    #print(REGISTROS[0])
    #mostrar_numerado(POBLACIONES)    
 
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    REGISTROS = lee_registros(r'sambuzgil\data\YouTube_data.csv\YouTube_data.csv')
    test_lee_registros()

    