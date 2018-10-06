'''particle swarm optimization
    F(x.vector)
    1. find random vector(point) in multi-dimension
    2. let all the point approach the max

    Conditions
    1. v velocity
    2. pBest memorized the best position
    3. gBest the best position overall

    Biological sense
    1.personal
    2. meomrize
    3. society
'''
'''
vmax 
    class particle:
        def__int__(self, dimension, boundary(this is a list of list )):
            self.v  (ls) (||create vector class)
            self.x  (ls) (||create vector class)
            self.pBest  (ls) (||create vector class)
            self.dimension (int)
        def move(self):    

        def evaluate(self, function):


        def f(x):                           
            return 2 - x[0]**2
        // def f(a,b); return a + b;
        // def test(fun): return fun (1,2)
        // print test(f(1,2))

    if self += v not in boundary, stop them
    outside of class
    def pso(function, boundary, iteration)  //final function
'''
import random

class Particle:
    def __init__(self, dimVect, boundary):
        self.pos = []       # position (x) in vector
        self.v = []         # momentum in vector
        self.pBest= []
        self.dimension = len(boundary)
        self.boundary = boundary

        self.pos = dimVect     #initalized position
        self.pBest = self.pos

        for i in range(self.dimension - 1):     #initalizing velocityVecotr
            self.v.append(random.uniform(self.boundary[i][0], self.boundary[i][1]))

    def evaluate(self, func):
        # update pBest (vector)
        val = func(self.pos)
        bVal = func(self.pBest)

        if(bVal < val):
            self.pBest = self.pos

    def move(self):
        vmax = 0.5
        for i in range(self.dimension - 1):         #update velocity
            r1 = r2 = c1 = random.uniform(0, 1)
            c3 = c2 = random.uniform(0, 4)
            if(self.v[i] < vmax):
                self.v[i] = c1 * self.v[i] + c2 * r1 * (self.pBest[i] - self.v[i]) + c3 * r2 * (gBestVec[i] - self.v[i])
            else:
                self.v[i] = vmax
        for i in range(self.dimension - 1):         #update position
            if(self.pos[i] > self.boundary[i][0] and self.pos[i] < self.boundary[i][1]):
                self.pos[i] = self.pos[i] + self.v[i]
            elif(self.pos[i] < self.boundary[i][0]):
                self.pos[i] = self.boundary[i][0]
            elif(self.pos[i] > self.boundary[i][1]):
                self.pos[i] = self.boundary[i][1]


def pso(func, boundary):
    global gBestVec
    numParticles = 100
    numIterations = 5
    gBestVec = []
    particles = []
    dimension = len(boundary)
    gChange = 0

    for i in range(numParticles):   #setting number of particles in dimensions
        vect = []
        for vec in range(dimension):        #vector of one particle
            vect.append(random.uniform(boundary[vec][0], boundary[vec][1]))
            particles.append(Particle(vect, boundary))


    gBestVec = particles[0].pBest

    for i in range(numIterations):  #number of time i want to test
        for p in particles:         #update gBestVec

            p.evaluate(func)
            if(func(gBestVec) < func(p.pBest)):
                gBestVec = p.pBest
                gChange += 1
        for p in particles:
            p.move()
            p.evaluate(func)
            if(func(gBestVec) < func(p.pBest)):
                gBestVec = p.pBest

        if(gChange == numIterations - 10):
            return f(gBestVec)
    return f(gBestVec)


def f(x):
    return 2 - x[0]**1 + x[1]**2 + x[2]**1
print(pso(f, [[0, 2],[0,3], [1,2]]))