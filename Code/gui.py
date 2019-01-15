from tkinter import *
from cryptoPSO import *
from threading import *
import time

swarm = None
stop = False

def cryptoPSOStop ():
    stop = True

def cryptoPSOStart ():
    # define all GUI components for algorithm execution
    executionLabel = Label(root, text="Algorithm execution", font='Verdana 16 bold')
    iterationNumberLabel = Label(root, text = "Iteration number:", font = 'Verdana 14')
    iterationLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
    activeParticlesLabel = Label(root, text = "Active particles:", font = 'Verdana 14')
    activeLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
    bestSolutionLabel = Label(root, text = "Best solution:", font = 'Verdana 14')
    solutionLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
    errorRateLabel = Label(root, text="Error:", font = 'Verdana 14')
    errorLabel = Label(root, text="", font='Verdana 14 bold', fg = 'Blue')
    stop = Button(root, text = "Stop", font = 'Verdana 14', command = cryptoPSOStop, width = 25)

    executionLabel.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 10)
    iterationNumberLabel.grid(row = 2, column = 4, padx = 5, pady = 10, sticky = "W")
    iterationLabel.grid(row = 2, column = 5, padx = 5, pady = 10, sticky = "W")
    activeParticlesLabel.grid(row = 3, column = 4, padx = 5, pady = 10, sticky = "W")
    activeLabel.grid(row = 3, column = 5, padx = 5, pady = 10, sticky = "W")
    bestSolutionLabel.grid(row = 4, column = 4, padx = 5, pady = 10, sticky = "W")
    solutionLabel.grid(row = 4, column = 5, padx = 5, pady = 10, sticky = "W")
    errorRateLabel.grid(row = 5, column = 4, padx = 5, pady = 10, sticky = "W")
    errorLabel.grid(row = 5, column = 5, padx = 5, pady = 10, sticky = "W")
    stop.grid(row = 6, column = 4, columnspan = 2, padx = 10, pady = 10)

    # start execution
    noOfParticles = int(particlesEntry.get())
    message = messageEntry.get()
    noOfInformants = int(informantsEntry.get())
    noOfIterations = int(iterationsEntry.get())
                              # particles,     message,        informants,    lowerBound, upperBound
    swarm = SwarmOfParticles(noOfParticles,     message,      noOfInformants,       0,          25)

    # initializing swarm solutions
    iterationLabel.config(text = "Initialization")
    activeLabel.config(text = noOfParticles)
    solutionLabel.config(text = toString(swarm.bestCoordinates))
    errorLabel.config(text = swarm.bestValue)
    stop = False

    # starting iterations
    for i in range(0, noOfIterations):
        canMoveOn = swarm.moveAllParticles()
        if not canMoveOn or stop:
            break
        iterationLabel.config(text = i + 1)
        activeLabel.config(text = len(swarm.particles))
        solutionLabel.config(text = toString(swarm.bestCoordinates))
        errorLabel.config(text = swarm.bestValue)
        root.update()
        time.sleep(1)

    # print final solution
    iterationLabel.config(text = "Final solution")
    activeLabel.config(text = len(swarm.particles))
    solutionLabel.config(text = toString(swarm.bestCoordinates))
    errorLabel.config(text = swarm.bestValue)

root = Tk()

# define all GUI components for parameter setup
parametersLabel = Label(root, text = "Parameters Setup", font = 'Verdana 16 bold')
particlesLabel = Label(root, text = "Number of particles:", font = 'Verdana 14')
particlesEntry = Entry(root, width = 10)
informantsLabel = Label(root, text = "Number of informants:", font = 'Verdana 14')
informantsEntry = Entry(root, width = 10)
iterationsLabel = Label(root, text = "Number of iterations:", font = 'Verdana 14')
iterationsEntry = Entry(root, width = 10)
messageLabel = Label(root, text = "Message:", font = 'Verdana 14')
messageEntry = Entry(root, width = 21)
start = Button(root, text="Start", font = 'Verdana 14', command=cryptoPSOStart, width = 25)

parametersLabel.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 10)
particlesLabel.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 10, sticky = "W")
particlesEntry.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = "W")
informantsLabel.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 10, sticky = "W")
informantsEntry.grid(row = 3, column = 3, padx = 10, pady = 10, sticky = "W")
iterationsLabel.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 10, sticky = "W")
iterationsEntry.grid(row = 4, column = 3, padx = 10, pady = 10, sticky = "W")
messageLabel.grid(row = 5, column = 1, padx = 5, pady = 10, sticky = "W")
messageEntry.grid(row = 5, column = 2, columnspan = 2, padx = 10, pady = 10, sticky = "W")
start.grid(row = 6, column = 1, columnspan = 3, padx = 10, pady = 10)

root.mainloop()
