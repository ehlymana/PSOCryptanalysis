from cryptoPSO import *
import time

strings = ["A", "TO", "THE", "STAR", "APRIL", "BIRDIE", "SOMEDAY", "COMPUTER", "YESTERDAY"]

largeStrings = ["BEPEACEFUL", "SHAKESPEARE", "THEGOLDENSUN", "CONSTELLATION", "SPENDINGMYTIME", "SEAGULLJONATHAN"]

iterations = [1, 10, 25, 50, 100, 250, 500, 1000]

numberOfParticles = [1, 2, 5, 10, 25, 50, 100, 125, 150]

informants = [1, 2, 3, 4, 5, 10, 25]

f = open("Tests/tests1.txt", "a+")

# tests for different string lenghts
f.write("* * * * * * * * * * * DIFFERENT MESSAGE LENGTHS * * * * * * * * * * *\n")
for i in range(0, len(strings)):
    f.write("String: " + strings[i] + "\n")
    print("****String: {}".format(strings[i]))
    start = time.time()
    for j in range(0, 10):
        print("****Iteration: {}".format(j + 1))
        swarm = SwarmOfParticles(40, strings[i], 4, 0, 25)
        iteration = 0
        for k in range(0, 50):
            canMove = swarm.moveAllParticles()
            if not canMove:
                iteration = k
                break
        f.write("Iteration: {} Decoded message: {} Mistake: {} Iterations necessary to solve: {}\n"
                .format(j + 1, toString(swarm.bestCoordinates), swarm.bestValue, iteration))
        swarm = None
    end = time.time()
    f.write("Execution time: {}\n".format(end - start))
    print("Execution time: {}\n".format(end - start))

for i in range(0, len(largeStrings)):
    f.write("String: " + largeStrings[i] + "\n")
    print("****String: {}".format(largeStrings[i]))
    start = time.time()
    swarm = SwarmOfParticles(40, largeStrings[i], 4, 0, 25)
    iteration = 0
    for k in range(0, 50):
        print("****Iteration: {}".format(k + 1))
        canMove = swarm.moveAllParticles()
        if not canMove:
            iteration = k
            break
    f.write("Decoded message: {} Mistake: {} Iterations necessary to solve: {}\n"
            .format(toString(swarm.bestCoordinates), swarm.bestValue, iteration))
    swarm = None
    end = time.time()
    f.write("Execution time: {}\n".format(end - start))
    print("Execution time: {}\n".format(end - start))

f.close()
f = open("Tests/tests2.txt", "a+")

# tests for different numbers of iterations
f.write("* * * * * * * * * * * DIFFERENT ITERATION NUMBERS * * * * * * * * * * *\n")
for i in range(0, len(iterations)):
    f.write("Number of iterations: {}\n".format((iterations[i])))
    print("****Number of iterations: {}".format((iterations[i])))
    start = time.time()
    for j in range(0, 10):
        print("****Iteration: {}".format(j + 1))
        swarm = SwarmOfParticles(40, strings[6], 4, 0, 25)
        for k in range(0, iterations[i]):
            canMove = swarm.moveAllParticles()
            if not canMove:
                break
        f.write("Iteration: {} Decoded message: {} Mistake: {}\n".format(j + 1, toString(swarm.bestCoordinates), swarm.bestValue))
    end = time.time()
    f.write("Execution time: {}\n".format(end - start))
    print("Execution time: {}\n".format(end - start))

f.close()
f = open("Tests/tests3.txt", "a+")

# tests for different numbers of particles
f.write("* * * * * * * * * * * DIFFERENT PARTICLE NUMBERS * * * * * * * * * * *\n")
for i in range(0, len(numberOfParticles)):
    f.write("Number of particles: {}\n".format(numberOfParticles[i]))
    print("****Number of particles: {}".format(numberOfParticles[i]))
    start = time.time()
    for j in range(0, 10):
        print("****Iteration: {}".format(j + 1))
        swarm = SwarmOfParticles(numberOfParticles[i], strings[6], 4, 0, 25)
        for k in range(0, 50):
            canMove = swarm.moveAllParticles()
            if not canMove:
                break
        f.write("Iteration: {} Decoded message: {} Mistake: {}\n".format(j + 1, toString(swarm.bestCoordinates), swarm.bestValue))
    end = time.time()
    f.write("Execution time: {}\n".format(end - start))
    print("Execution time: {}\n".format(end - start))

f.close()
f = open("Tests/tests4.txt", "a+")

# tests for different numbers of informants
f.write("* * * * * * * * * * * DIFFERENT INFORMANT NUMBERS * * * * * * * * * * *\n")
for i in range(0, len(informants)):
    f.write("Number of informants: {}\n".format(informants[i]))
    print("****Number of informants: {}".format(informants[i]))
    start = time.time()
    for j in range(0, 10):
        print("****Iteration: {}".format(j + 1))
        swarm = SwarmOfParticles(40, strings[6], informants[i], 0, 25)
        for k in range(0, 50):
            canMove = swarm.moveAllParticles()
            if not canMove:
                break
        f.write("Iteration: {} Decoded message: {} Mistake: {}\n".format(j + 1, toString(swarm.bestCoordinates), swarm.bestValue))
    end = time.time()
    f.write("Execution time: {}\n".format(end - start))
    print("Execution time: {}\n".format(end - start))

f.close()