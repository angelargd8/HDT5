"""
    Hoja de trabajo 5
    Autores:
            - Carlos Valladares #221164
            - Alejandro Ortega #18248
            - Angela García #22869
    fecha de entrega: 27/02/2023

"""
# "Formulario"
# https://simpy.readthedocs.io/en/latest/topical_guides/resources.html#res-type-container

#modulos
import simpy
import random
import os

programas=10
RANDOM_SEED = 10
intervalo= 10
procesos= random.expovariate(1.0/intervalo)
cantidad_de_instrucciones=3 #por ciclo
# La velocidad del cpu se modela con que atiende en una unidad de tiempo q permite realizar 3 intrucciones

#funciones
    
def programa(name, env, tiempo_llegada, cant_memoria, cant_instrucciones, ram, cpu):
    
    # NEW
    
    yield env.timeout(tiempo_llegada)
    print(f"{name} llegó al sistema en el tiempo {tiempo_llegada}")
    
    # Pedir memoria RAM
    cant_memoria= random.randint(0, 10)

    print(f"{name} pidió {cant_memoria} de memoria RAM")
    memoria=ram.get(cant_memoria)
    yield ram.get(cant_memoria)
    print(f"{name} obtuvo {cant_memoria} de memoria RAM")
    #print(memoria)
    # Si hay memoria, pasar a READY
    if (memoria>0):
        env.process(memoria.ready())
    else:
        pass
    # Si no, permanece en cola
        
    # READY  
    # Esperar a ser atendido por el CPU
    with cpu.request() as req:
        yield req
        
    # estado cpu
    
    
    #RUNNING
    #atiende el CPU x tiempo limitado x 3 intrucciones

    #Cuando se termina el tiempo de atencion  el proceso es retirado del CPU
    # actualizar el contador
    # disminuyen 3  intrucciones (Ciclo completo)
        # terminated
        # Waiting
        # Ready
    


        
    # Contador de instrucciones totales
    contador_instrucciones= 0
    #entra a la cola1
    tiempo_entrada= env.now()

    #Proceso:  ejecuta el programa 

def menu():
    print("Bienvenido al simulador de corrida de programas en un S.O. de tiempo compartido.")


#objetos
#environment
env = simpy.Environment() #ambiente de simulación
cpu = simpy.Resource(env, capacity = 1)
ram = simpy.Container(env, init=100, capacity=100)
random.seed(RANDOM_SEED)


def crear_programas(env, programas):
    for i in range(programas): #name, env, tiempo_llegada, cant_memoria, cant_instrucciones, ram, cpu
        env.process(programa(i, env,  random.expovariate(1.0/intervalo), random.randint(0,10)), cantidad_de_instrucciones, ram , cpu)

#correr la simulacion
env.run()

