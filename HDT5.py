"""
    Hoja de trabajo 5
    Autores:
            - Carlos Valladares #
            - Alejandro Ortega #18248
            - Angela García #
    fecha de entrega: 27/02/2023

"""
#modulos
import simpy
import random
import os

RANDOM_SEED = 10

#funciones
def programas(env, cant_instrucciones, cant_memoria, ram, cpu):
    
    # NEW
    # Pedir memoria RAM
    # Si hay memoria, pasar a READY
    # Si no, permanece en cola
        
    # READY  
    # Esperar a ser atendido por el CPU
    with cpu.request() as req:
        yield req
        
    # estado cpu
    
    #RUNNING
    
        
    # Contador de instrucciones totales
    #entra a la cola1
    tiempo_entrada= env.now()

    #Proceso:  ejecuta el programa 


def menu():
    pass


#objetos
#environment
env = simpy.Environment() #ambiente de simulación
cpu = simpy.Resource(env, capacity = 3)
ram = simpy.Container(env, init=100, capacity=100)
random.seed(RANDOM_SEED)



