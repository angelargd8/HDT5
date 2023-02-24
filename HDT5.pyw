"""
    Hoja de trabajo 5
    Autores:
            - Carlos Valladares #
            - Alejandro Ortega # 
            - Angela García #
    fecha de entrega: 27/02/2023

"""
#modulos
import simpy
import random
import os

#funciones
def programas(env, tiempo_de_cola, cpu):
    
    yield env.timeout(tiempo_de_cola)

    #entra a la cola
    tiempo_entrada= env.now()

    #Proceso:  ejecuta el programa 


def menu():
    pass


#objetos
#environment
env = simpy.Environment() #ambiente de simulación
cpu = simpy.Resource(env,capacity = 1)

