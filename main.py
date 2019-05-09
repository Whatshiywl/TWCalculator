from sim import Simulation
from village import Village
import random
from numba import cuda, jit

def gen_queue(village_cls):
    village = village_cls()
    initial = []
    queue = []
    for i in range(len(village.get_buildings())):
        q = village.get_buildings()[i]
        n = q.get_max_level() - q.get_level()
        queue += [i] * n
    r = initial + random.sample(queue, len(queue))
    # print pr(r)
    return r

    
def mutate(ind, d):
    l = len(ind)
    i = random.randint(0, l - 1)
    m = random.randint(0, 2)
    if m == 0:
        dj = 0
        while dj == 0:
            dj = random.randint(int(-d), int(d)) 
        j = i + dj
        j = j % l
        temp = ind[i] 
        ind[i] = ind[j] 
        ind[j] = temp
    elif m == 1:
        b = random.sample(range(max(ind)*int(d)), random.randint(1, int(d)))
        ind = ind[:i] + b + ind[i:]
    elif m == 2:
        j = max(i+d, len(ind)-1)
        ind = ind[:int(i)] + ind[int(j):]
    return ind


def mutate2(ind):
    i, j = random.sample(range(len(ind)), 2)
    temp = ind[i] 
    ind[i] = ind[j] 
    ind[j] = temp
    return ind


def crossover(ch1, ch2):
    i = random.randint(0, min(len(ch1), len(ch2))-1) 
    temp = ch1[:i]
    ch1[:i] = ch2[:i] 
    ch2[:i] = temp


# @cuda.jit
def simulate(ind):
    return Simulation().simulate(ind)


def pr(ind):
    s = '|'
    ch = ''
    n = 0
    for b in ind:
        bch = str(b)
        if bch != ch:
            if n > 1:
                s += str(n) + '.' + ch + '|'
            elif n > 0:
                s += ch + '|'
            ch = bch
            n = 1
        else:
            n += 1
    return s


def pr2(ind):
    village = Village()
    s = '|'
    for b in ind:
        building = village.get_buildings()[b]
        building.level_up()
        s += building.get_name() + ('%02d' % building.get_level()) + "|"
    return s


def init_toolbox():
    creator.create("FitnessMax", base.Fitness, weights=(1.0, 1E-10))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("genQueue", gen_queue, Village)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.genQueue)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    return toolbox


POP = 100
N_GEN = 10000
PRINT = N_GEN / 100
CXPB = 0.0
MUTPB = 0.8

TOP_POP = 0.1
MUT_POP = 0.9
RND_POP = 0.0

POOLS = 8


def evolve():
    print ("setup")

    toolbox = init_toolbox()

    # times = [0] * 9
    
    pop = toolbox.population(POP)
    pool = Pool(POOLS) if POOLS else 0
    print ("start")
    g = 0
    n = 0
    while g < N_GEN:
        n += 1
        # t = time() 
        # Select the next generation individuals
        offspring = tools.selTournament(pop, int(len(pop) * TOP_POP), int(len(pop) / 10))
        # times[0] += time()-t 
        
        # t = time() 
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        # times[1] += time()-t
    
        # t = time() 
        # Apply crossover on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                crossover(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        # times[2] += time()-t
    
        # t = time() 
        # Apply mutation on the offspring
        # for mutant in offspring:
        for i in range(int(POP * MUT_POP)):
            ind = random.sample(offspring, 1)[0]
            mutant = toolbox.clone(ind)
            while random.random() < MUTPB:
            # if random.random() < MUTPB:
                mutate(mutant, len(mutant) / 2)
                # mutate2(mutant)
            del mutant.fitness.values
            offspring += [mutant] 
        # times[3] += time()-t 
        
        # t = time() 
        for i in range(int(POP * RND_POP)):
            offspring += [toolbox.individual()] 
        # times[4] += time()-t
    
        # t = time() 
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        queues = [ind[:] for ind in invalid_ind]
        # times[5] += time()-t
        
        # t = time() 
        mp = map if not pool else pool.map
        fitnesses = list(mp(simulate, queues))
        # times[6] += time()-t
        
        # t = time() 
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        # times[7] += time()-t 
        
        best = tools.selBest(offspring, 1)[0]
        fit = best.fitness.values
        if math.isinf(fit[0]):
            if n % 1 == 0:
                print ('try again', n)
            pop = toolbox.population(POP)
            continue

        # t = time() 
        # The population is entirely replaced by the offspring
        pop[:] = offspring
        # times[8] += time()-t
        if g % (N_GEN / PRINT) == 0 or g == N_GEN - 1:
            best = tools.selBest(pop, 1)[0]
            fit = best.fitness.values[:]
            if math.isinf(fit[0]):
                fit = (-1, -1)
            else:
                fit = (int(-fit[0]), int(fit[1]))
            print (g, len(offspring), fit, pr2(best))
            # print (times)
            # times = [0]*9
        g += 1        
    print ("done") 


if __name__ == '__main__':
    # from time import time
    from deap import base, creator, tools
    import math
    from multiprocessing import Pool
    evolve()
