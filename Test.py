import simpy
import random

INSTRUCTIONS_PER_CYCLE = 3

def program(name, env, arrival_time, memory_amount, instruction_amount, ram, cpu):
    yield env.timeout(arrival_time)
    print(f"\"{name}\" Program arriving at {env.now:.3f}")
    print(f"\"{name}\" Program requesting {memory_amount} units of memory at {env.now:.3f}")
    yield ram.get(memory_amount)
    
    instructions_remaining = instruction_amount
    while instructions_remaining > 0:
        print(f"\"{name}\" Program requesting cpu for {instructions_remaining} instructions at {env.now:.3f}")
        with cpu.request() as req:
            print(f"\"{name}\" Program was granted cpu access at {env.now:.3f}")
            yield req
            instructions_remaining -= INSTRUCTIONS_PER_CYCLE
            
    print(f"\"{name}\" Program releasing {memory_amount} units of memory at {env.now:.3f}")
    yield ram.put(memory_amount)
    
    print(f"\"{name}\" Program finished execution at {env.now:.3f}")
            
env = simpy.Environment()
cpu = simpy.Resource(env, capacity=1)
ram = simpy.Container(env, init=100, capacity=100)

random.seed(10)

env.process(program("test1", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))
env.process(program("test2", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))
env.process(program("test3", env, random.expovariate(1.0/10), random.randint(1,10), random.randint(1,10), ram, cpu))

env.run()