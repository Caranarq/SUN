# -*- coding: utf-8 -*-
"""
DESCRIPCION: Script para asignar claves y nombres de ciudades de acuerdo con el Sistema Urbano Nacional
Fuente de la información: Catálogo del Sistema Urbano Nacional
Started on Fri Aug  4 12:54:13 2017

@author: carlos.arana
"""
'''
Espera los siguientes parametros:
dataframe: pandas dataframe al que se desean asignar claves geoestadisticas
CVE_MUN: str, Nombre de la columna en dataframe que contiene la clave geoestadística a nivel municipal (5 DIGITOS)
cols = [list] columnas del catalogo geoestadístico que se unirán.

Crea las siguientes columnas:
CVE_SUN: Clave de 3 digitos del SUN
NOM_MUN: Nombre de la ciudad a la que pertenece el municipio, de acuerdo con el SUN
TIPO_SUN: Tipo de ciudad, de acuerdo con la clasificacion definida en el SUN
'''

from pandas import read_csv as rcsv

def asignar_sun(dataframe, CVE_MUN = 'CVE_MUN', vars = ['CVE_MUN', 'CVE_SUN', 'NOM_SUN']):
    geo = rcsv(r'D:\PCCS\01_Analysis\01_DataAnalysis\00_Parametros\sun.csv',
                      dtype={'CVE_SUN': str, 'CVE_ENT': str, 'CVE_MUN': str, 'CVE_LOC': str},
                      encoding='UTF-8',
                      )
    print('Catalogo de variables. Default vars = {}'.format(defaultcols))
    print(list(geo))
    if 'CVE_MUN' not in vars: vars.append('CVE_MUN')

    dataframe.rename(columns={CVE_MUN : 'CVE_MUN'}, inplace = True) # Estandariza el nombre de la columna de clave geoestadistica
    geo = geo[vars]
    dataframe = pd.merge(dataframe, geo, on='CVE_MUN')
    return dataframe