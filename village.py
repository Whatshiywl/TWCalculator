from building import Building

buildTimeFactor = 1.2
pointFactor = 1.2
productionFactor = 1.16312
populationFactor = 1.1721
capacityFactor = 1.2295


class Village:

    def __init__(self):
        self.hq = Building({
            'level': 1,
            'name': 'hq',
            'maxLevel': 30,  # 30,
            'cost': [90, 80, 70, 5],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 7*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 10,
            'pointFactor': pointFactor,
        })

        self.woodMine = Building({
            'level': 1,
            'name': 'wm',
            'maxLevel': 30,  # 30,
            'cost': [50, 60, 40, 5],
            'costFactor': [1.25, 1.275, 1.245, 1.155],
            'buildTime': 7*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 6,
            'pointFactor': pointFactor,
            'production': 30,
            'productionFactor': productionFactor
        })

        self.clayMine = Building({
            'level': 1,
            'name': 'cm',
            'maxLevel': 30,  # 30,
            'cost': [65, 50, 40, 10],
            'costFactor': [1.27, 1.265, 1.24, 1.14],
            'buildTime': 7*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 6,
            'pointFactor': pointFactor,
            'production': 30,
            'productionFactor': productionFactor
        })

        self.ironMine = Building({
            'level': 1,
            'name': 'im',
            'maxLevel': 30,  # 30,
            'cost': [75, 65, 70, 10],
            'costFactor': [1.252, 1.275, 1.24, 1.17],
            'buildTime': 9*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 6,
            'pointFactor': pointFactor,
            'production': 30,
            'productionFactor': productionFactor
        })

        self.farm = Building({
            'level': 1,
            'name': 'fm',
            'maxLevel': 30,  # 30,
            'cost': [45, 40, 30, 0],
            'costFactor': [1.3, 1.32, 1.29, 1],
            'buildTime': 10*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 5,
            'pointFactor': pointFactor,
            'population': 240,
            'populationFactor': populationFactor
        })

        self.warehouse = Building({
            'level': 1,
            'name': 'wh',
            'maxLevel': 30,  # 30,
            'cost': [60, 50, 40, 0],
            'costFactor': [1.265, 1.27, 1.245, 1.15],
            'buildTime': 8*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 6,
            'pointFactor': pointFactor,
            'capacity': 1000,
            'capacityFactor': capacityFactor
        })

        self.barracks = Building({
            'level': 0,
            'name': 'br',
            'maxLevel': 25,  # 25,
            'cost': [200, 170, 90, 7],
            'costFactor': [1.26, 1.28, 1.26, 1.17],
            'buildTime': 15*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 16,
            'pointFactor': pointFactor
        })

        self.stable = Building({
            'level': 0,
            'name': 'sb',
            'maxLevel': 20,  # 20,
            'cost': [270, 240, 260, 8],
            'costFactor': [1.26, 1.28, 1.26, 1.17],
            'buildTime': 50*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 20,
            'pointFactor': pointFactor
        })

        self.garage = Building({
            'level': 0,
            'name': 'gr',
            'maxLevel': 15,
            'cost': [300, 240, 260, 8],
            'costFactor': [1.26, 1.28, 1.26, 1.17],
            'buildTime': 50*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 24,
            'pointFactor': pointFactor
        })

        self.snob = Building({
            'level': 0,
            'name': 'SN',
            'maxLevel': 1,
            'cost': [15000, 25000, 10000, 80],
            'costFactor': [2, 2, 2, 1.17],
            'buildTime': 4890*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 512,
            'pointFactor': pointFactor
        })

        self.smith = Building({
            'level': 0,
            'name': 'sm',
            'maxLevel': 20,
            'cost': [220, 180, 240, 20],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 50*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 19,
            'pointFactor': pointFactor
        })

        self.place = Building({
            'level': 1,
            'name': 'pl',
            'maxLevel': 1,
            'cost': [10, 40, 30, 0],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 90*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 0,
            'pointFactor': pointFactor
        })

        self.statue = Building({
            'level': 0,
            'name': 'st',
            'maxLevel': 1,
            'cost': [220, 220, 220, 10],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 12*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 24,
            'pointFactor': pointFactor
        })

        self.market = Building({
            'level': 0,
            'name': 'mk',
            'maxLevel': 25,
            'cost': [100, 100, 100, 20],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 22*60+30,
            'buildTimeFactor': buildTimeFactor,
            'points': 10,
            'pointFactor': pointFactor
        })

        self.hide = Building({
            'level': 0,
            'name': 'hd',
            'maxLevel': 10,
            'cost': [50, 60, 50, 2],
            'costFactor': [1.25, 1.25, 1.25, 1.17],
            'buildTime': 15*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 5,
            'pointFactor': pointFactor
        })

        self.wall = Building({
            'level': 0,
            'name': 'wl',
            'maxLevel': 20,
            'cost': [50, 100, 20, 5],
            'costFactor': [1.26, 1.275, 1.26, 1.17],
            'buildTime': 30*60,
            'buildTimeFactor': buildTimeFactor,
            'points': 8,
            'pointFactor': pointFactor
        })

        self.buildings = []
        self.buildings += [self.hq]
        self.buildings += [self.woodMine]
        self.buildings += [self.clayMine]
        self.buildings += [self.ironMine]
        self.buildings += [self.farm]
        self.buildings += [self.warehouse]
        self.buildings += [self.barracks]
        self.buildings += [self.stable]
        self.buildings += [self.garage]
        self.buildings += [self.snob]
        self.buildings += [self.smith]
        self.buildings += [self.place]
        self.buildings += [self.statue]
        self.buildings += [self.market]
        self.buildings += [self.hide]
        self.buildings += [self.wall]

    def get_buildings(self):
        return self.buildings

    def get_wood_yield(self):
        return self.woodMine.get_production()

    def get_clay_yield(self):
        return self.clayMine.get_production()

    def get_iron_yield(self):
        return self.ironMine.get_production()

    def get_yield(self, i):
        if i == 0:
            return self.get_wood_yield()
        elif i == 1:
            return self.get_clay_yield()
        elif i == 2:
            return self.get_iron_yield()

    def get_population(self):
        return sum(map(lambda b: b.get_population(), self.buildings))

    def get_pop_limit(self):
        return self.farm.get_population()

    def get_capacity(self):
        return self.warehouse.get_capacity()
