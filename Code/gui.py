from tkinter import *
from cryptoPSO import *
from threading import Thread
import time

class Threads:

    def __init__(self, master):
        self.master = master
        self.maximumIteration = 0

    def start(self):
        noOfParticles = int(particlesEntry.get())
        message = messageEntry.get()
        noOfInformants = int(informantsEntry.get())
        self.maximumIteration = int(iterationsEntry.get())

        # particles,     message,        informants,    lowerBound, upperBound
        self.swarm = SwarmOfParticles(noOfParticles, message, noOfInformants, 0, 25)

        # initializing swarm solutions
        iterationLabel.config(text="Initialization")
        activeLabel.config(text=noOfParticles)
        solutionLabel.config(text=toString(self.swarm.bestCoordinates))
        errorLabel.config(text=self.swarm.bestValue)
        ThreadedTask(self.swarm, self.maximumIteration).start()
        self.master.after(1, self.process_queue)

    def stop(self):
        self.swarm.generation = self.maximumIteration
        self.swarm.canMove = False

    def process_queue(self):
        # print current solution
        iterationLabel.config(text = self.swarm.generation + 1)
        activeLabel.config(text = len(self.swarm.particles))
        solutionLabel.config(text = toString(self.swarm.bestCoordinates))
        errorLabel.config(text = self.swarm.bestValue)
        if self.swarm.generation < self.maximumIteration:
            self.master.after(1, self.process_queue)

        # print final solution
        if self.swarm.generation >= self.maximumIteration or not self.swarm.canMove:
            iterationLabel.config(text = "Final solution")
            activeLabel.config(text = len(self.swarm.particles))
            solutionLabel.config(text = toString(self.swarm.bestCoordinates))
            errorLabel.config(text = self.swarm.bestValue)


class ThreadedTask(Thread):

    def __init__(self, swarm, maximumIteration):
        Thread.__init__(self)
        self.swarm = swarm
        self.maximumIteration = maximumIteration

    def run(self):
        while self.swarm.canMove and self.swarm.generation < self.maximumIteration:
            time.sleep(0.5)
            self.swarm.canMove = self.swarm.moveAllParticles()


root = Tk()
threads = Threads(root)

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
start = Button(root, text="Start", font = 'Verdana 14', command=threads.start, width = 25)

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

# define all GUI components for algorithm execution
executionLabel = Label(root, text = "Algorithm execution", font = 'Verdana 16 bold')
iterationNumberLabel = Label(root, text = "Iteration number:", font = 'Verdana 14')
iterationLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
activeParticlesLabel = Label(root, text = "Active particles:", font = 'Verdana 14')
activeLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
bestSolutionLabel = Label(root, text = "Best solution:", font = 'Verdana 14')
solutionLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
errorRateLabel = Label(root, text = "Error:", font = 'Verdana 14')
errorLabel = Label(root, text = "", font = 'Verdana 14 bold', fg = 'Blue')
stop = Button(root, text = "Stop", font = 'Verdana 14', command = threads.stop, width = 25)

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

root.mainloop()
