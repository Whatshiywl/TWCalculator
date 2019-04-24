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

    def setPop(self, p):
        self.pop = p

    def consumeResources(self, cost):
        for i in range(len(self.res)):
            self.res[i] -= cost[i]

    def calcTime(self, dt, w=False):
        self.time += dt
        if w:
            self.wait += dt
        capacity = self.village.getCapacity()
        for i in range(len(self.res)):
            self.res[i] = min([capacity, self.res[i] + self.village.getYield(i)*dt])
        
    def getTime(self):
        return self.time
        
    def getWait(self):
        return self.wait

    def hasResources(self, target):
        return self.res[0] >= target[0] and self.res[1] >= target[0] and self.res[2] >= target[2]

    def hasPopulation(self, target):
        return self.village.getPopulation() <= self.village.getPopLimit()

    def build(self, item):
        nextFromQueue = self.village.getBuildings()[item]
        if(nextFromQueue.getLevel() >= nextFromQueue.getMaxLevel()):
            print "tried raise " + str(item) + " to level " + str(nextFromQueue.getLevel())
            return False
        nextCost = nextFromQueue.getCost()
        if max(nextCost) > self.village.getCapacity():
            # print "res fail", nextCost, self.village.getCapacity()
            return False
        if not self.hasResources(nextCost):
            maxTime = 0
            for i in range(len(self.res)):
                diff = nextCost[i] - self.res[i] 
                prod = self.village.getYield(i)
                t = diff/prod
                if t > maxTime:
                    maxTime = t
            self.calcTime(maxTime, True)
        self.consumeResources(nextCost)
        baseTime = nextFromQueue.getBuildTime()
        dt = baseTime*1.05**(-self.village.hq.getLevel())
        self.calcTime(dt) 
        nextFromQueue.levelUp()
        if not self.hasPopulation(nextCost):
            # print "pop fail", self.village.getPopulation(), self.village.getPopLimit(), nextFromQueue().getLevel()
            return False
        self.points = sum(map(lambda b: b.getPoints(), self.village.getBuildings()))
        return True
    
    def simulate(self, q):
        for item in q:
            if not self.build(item):
                self.calcTime(float('inf'), True)
                # self.calcTime(365*24*60*60, True)
                break
        return self.getTime(), self.getWait()
