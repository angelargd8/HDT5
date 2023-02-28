import simpy
import random

INSTRUCTIONS_PER_CYCLE = 3
RANDOM_SEED = 10
RAM_CAPACITY= 100

def program(name, env, arrival_time, memory_amount, instruction_amount, ram, cpu):
    yield env.timeout(arrival_time)
    print(f"\"{name}\" Program arriving at {env.now:.3f}\n")
    #request ram
    print(f"\"{name}\" Program requesting {memory_amount} units of memory at {env.now:.3f}\n")
    yield ram.get(memory_amount)
    instructions_remaining = instruction_amount
    #READY : 
    #while instructions remainig is != 0 then:
    while instructions_remaining > 0:
        print(f"\"{name}\" Program requesting cpu for {instructions_remaining} instructions at {env.now:.3f}\n")
        #attended by cpu
        with cpu.request() as req:
            print(f"\"{name}\" Program was granted cpu access at {env.now:.3f}\n")
            yield req
            #cpu executed instructions
            # discount instruccion
            instructions_remaining -= INSTRUCTIONS_PER_CYCLE
    #print execution intruccion        
    print(f"\"{name}\" Program releasing {memory_amount} units of memory at {env.now:.3f}\n")
    #free ram
    yield ram.put(memory_amount)
    
    #print end of the program
    print(f"\"{name}\" Program finished execution at {env.now:.3f}\n")

#Initialize simulation
env = simpy.Environment()
cpu = simpy.Resource(env, capacity=1)
ram = simpy.Container(env, init=100, capacity=RAM_CAPACITY)

random.seed(RANDOM_SEED)

#create programs
env.process(program("test1", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))
env.process(program("test2", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))
env.process(program("test3", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))
#run simulation
env.run()