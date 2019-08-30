# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:52:17 2019

@author: User
"""
import pandas as pd
import numpy as np
import math as math
import funcoes as f
from scipy import stats
import matplotlib.pyplot as plt

def grafico_241():
    plt.figure(figsize=(15,10))
    #Todos os Países
    all_country = paises_desemprego.drop("entrance",axis=1)
    all_country = all_country.drop("Pertence a OCDE",axis=1)
    y = all_country.mean()
    x = y.index

    plt.plot(x,y, label = "Média Mundial",color='black')
    plt.legend()

    #Países Que pertecem a Organização
    data_members = paises_desemprego[paises_desemprego["Pertence a OCDE"] == "sim"]
    data_members = data_members.drop("entrance",axis=1)
    data_members = data_members.drop("Pertence a OCDE",axis=1)
    y = data_members.mean()
    x = y.index

    plt.scatter(x,y,label="Membros da OCDE",color='b')
    plt.legend()

    #Países que não pertencem a organização
    data = paises_desemprego[paises_desemprego["Pertence a OCDE"] == "não"]
    data = data.drop("entrance",axis=1)
    data = data.drop("Pertence a OCDE",axis=1)
    y = data.mean()
    x = y.index

    plt.scatter(x,y,label="Países que não pertencem a OCDE",color = 'r')
    plt.legend()
    plt.ylabel("Taxa de Desemprego")
    plt.xlabel("Anos")
    plt.title("Gráfico da Média da Taxa de Desemprego de Países que pertencem a OCDE (em azul) versus Países que Não pertencem a OCDE (vermelho)")
    
