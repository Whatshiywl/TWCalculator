class Building:
    level = 0
    name = ''
    maxLevel = 0
    cost = []
    costFactor = []
    buildTime = 0
    buildTimeFactor = 0
    points = 0
    pointFactor = 0
    production = 0
    productionFactor = 0
    population = 0
    populationFactor = 0
    capacity = 0
    capacityFactor = 0
    initState = dict()

    def __init__(self, options):
        self.level = options['level']
        self.name = options['name']
        self.maxLevel = options['maxLevel']
        self.cost = options['cost']
        self.costFactor = options['costFactor']
        self.buildTime = options['buildTime']
        self.buildTimeFactor = options['buildTimeFactor']
        self.points = options['points']
        self.pointFactor = options['pointFactor']
        if 'production' in options:
            self.production = options['production']/3600.0
            self.productionFactor = options['productionFactor']
        if 'population' in options:
            self.population = options['population']
            self.populationFactor = options['populationFactor']
        if 'capacity' in options:
            self.capacity = options['capacity']
            self.capacityFactor = options['capacityFactor']
        self.initState = options

    def get_level(self):
        return self.level
    
    def get_name(self):
        return self.name
    
    def get_max_level(self):
        return self.maxLevel
    
    def get_cost(self):
        return map(lambda t: round(t[0]*t[1]**self.level), zip(self.cost, self.costFactor))
    
    def get_build_time(self):
        return self.buildTime*self.buildTimeFactor**self.level

    def get_points(self):
        if self.level > 0:
            return round(self.points*self.pointFactor**(self.level - 1))
        else:
            return 0
    
    def get_production(self):
        return self.production*self.productionFactor**(self.level-1)
    
    def get_population(self):
        if self.level == 0:
            return 0
        else:
            return round(self.population*self.populationFactor**(self.level-1))
    
    def get_capacity(self):
        return round(self.capacity*self.capacityFactor**(self.level-1))

    def level_up(self):
        self.level += 1

    def reset(self):
        self.level = self.initState['level']