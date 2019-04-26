from village import Village


class Simulation:
    time = 0
    wait = 0
    res = [0, 0, 0]
    points = 0
    queue = []
    village = 0

    def __init__(self):
        self.village = Village()

    def consume_resources(self, cost):
        for i in range(len(self.res)):
            self.res[i] -= cost[i]

    def calc_time(self, dt, w=False):
        self.time += dt
        if w:
            self.wait += dt
        capacity = self.village.get_capacity()
        for i in range(len(self.res)):
            self.res[i] = min([capacity, self.res[i] + self.village.get_yield(i) * dt])
        
    def get_time(self):
        return self.time / 3600.0 / 24.0
        
    def get_wait(self):
        return self.wait

    def has_resources(self, target):
        return self.res[0] >= target[0] and self.res[1] >= target[0] and self.res[2] >= target[2]

    def has_population(self, target):
        return self.village.get_population() <= self.village.get_pop_limit()

    def build(self, item):
        next_from_queue = self.village.get_buildings()[item]
        if next_from_queue.get_level() >= next_from_queue.get_max_level():
            print "tried raise " + str(item) + " to level " + str(next_from_queue.get_level())
            return False
        next_cost = next_from_queue.get_cost()
        if max(next_cost) > self.village.get_capacity():
            # print "res fail", next_cost, self.village.getCapacity()
            return False
        if not self.has_resources(next_cost):
            max_time = 0
            for i in range(len(self.res)):
                diff = next_cost[i] - self.res[i]
                prod = self.village.get_yield(i)
                t = diff / prod
                if t > max_time:
                    max_time = t
            self.calc_time(max_time, True)
        self.consume_resources(next_cost)
        base_time = next_from_queue.get_build_time()
        dt = base_time * 1.05 ** (-self.village.hq.get_level())
        self.calc_time(dt)
        next_from_queue.level_up()
        if not self.has_population(next_cost):
            # print "pop fail", self.village.getPopulation(), self.village.getPopLimit(), next_from_queue().getLevel()
            return False
        self.points = sum(map(lambda b: b.get_points(), self.village.get_buildings()))
        return True
    
    def simulate(self, q):
        for item in q:
            if not self.build(item):
                self.calc_time(float('inf'), True)
                # self.calcTime(365 * 24 * 60 * 60, True)
                break
        return -self.get_time(), self.points  # , -self.getWait()

