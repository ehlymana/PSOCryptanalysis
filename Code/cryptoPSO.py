import random
import copy

SIMILARITY = 0.001
MESSAGE = "SOMEDAY"

# find frequencies of characters in a message
def findFrequenciesCharacters(x, characters):
    for i in range(0, 26):
        characters.append(0)
    for i in range(0, len(x)):
        characters[x[i]] += 1
    for i in range(0, 26):
        characters[i] /= len(x)


# find frequencies of bigrams in a message
def findFrequenciesBigrams(x, bigrams):
    for i in range(0, 26):
        bigrams.append([])
        for j in range(0, 26):
            bigrams[i].append(0)
    for i in range(0, len(x)):
        if i < len(x) - 1:
            bigrams[x[i]][x[i + 1]] += 1
    for i in range(0, 26):
        for j in range(0, 26):
            bigrams[i][j] /= len(x)


# find frequencies of trigrams in a message
def findFrequenciesTrigrams(x, trigrams):
    for i in range(0, 26):
        trigrams.append([])
        for j in range(0, 26):
            trigrams[i].append([])
            for k in range(0, 26):
                trigrams[i][j].append(0)
    for i in range(0, len(x)):
        if i < len(x) - 2:
            trigrams[x[i]][x[i + 1]][x[i + 2]] += 1
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                trigrams[i][j][k] /= len(x)


# find frequencies of quadgrams in a message
def findFrequenciesQuadgrams(x, quadgrams):
    for i in range(0, 26):
        quadgrams.append([])
        for j in range(0, 26):
            quadgrams[i].append([])
            for k in range(0, 26):
                quadgrams[i][j].append([])
                for l in range(0, 26):
                    quadgrams[i][j][k].append(0)
    for i in range(0, len(x)):
        if i < len(x) - 3:
            quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] += 1
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                for l in range(0, 26):
                    quadgrams[i][j][k][l] /= len(x)


# turn coordinates to string message
def toString(position):
    stringMessage = ""
    for i in range(0, len(position)):
        stringMessage += chr(position[i] + ord('A'))
    return stringMessage


# make a random transpozition of the message
def transpozition(message):
    characters = []
    frequencies = []
    for i in range(0, 26):
        characters.append(0)
        frequencies.append(0)
    for i in range(0, len(message)):
        characters[ord(message[i]) - ord('A')] += 1
    for i in range(0, 26):
        frequencies[i] = characters[i] / len(message)
    codedMessage = []
    for i in range(0, len(message)):
        character = random.randint(0, 25)
        while characters[character] == 0:
            character = random.randint(0, 25)
        codedMessage.append(character)
        characters[character] -= 1
    stringMessage = ""
    for i in range(0, len(codedMessage)):
        stringMessage += chr(codedMessage[i] + ord('A'))
    return codedMessage


# make a random Caesar code of the message
def CaesarCode(message):
    key = random.randint(0, 25)
    newMessage = ""
    for i in range(0, len(message)):
        character = ord(message[i]) + key
        if character > ord('Z'):
            character -= 25
        newMessage += chr(character)
    return newMessage


def CaesarDecode(message):
    characters = []
    x = []
    for i in range(0, len(message)):
        x.append(ord(message[i]) - ord('A'))
    findFrequenciesCharacters(x, characters)
    leastDifference = abs(messageCharacters[0] - characters[0])
    index = [0, 0]
    for i in range(0, 26):
        for j in range(0, 26):
            if messageCharacters[i] != 0 and abs(messageCharacters[i] - characters[j]) < leastDifference:
                leastDifference = messageCharacters[i] - characters[j]
                index = [i, j]
    caesarKey = index[1] - index[0]
    newMessage = ""
    for i in range(0, len(message)):
        character = ord(message[i]) + caesarKey
        if character > ord('Z'):
            character -= 25
        elif character < ord('A'):
            character += 25
        newMessage += chr(character)
    return newMessage


# calculate similarity between message monogram and bigram frequency and natural frequency
def criterionFunctionBigrams(x):
    bigrams = []
    findFrequenciesBigrams(x, bigrams)
    f = 0
    for i in range(0, len(bigrams)):
        for j in range(0, len(bigrams[i])):
            if bigrams[i][j] != 0 and abs(bigrams[i][j] - messageBigrams[i][j]) > SIMILARITY:
                f += 1
    return f


def criterionFunctionTrigrams(x):
    trigrams = []
    findFrequenciesTrigrams(x, trigrams)
    f = 0
    for i in range(0, len(trigrams)):
        for j in range(0, len(trigrams[i])):
            for k in range(0, len(trigrams[i][j])):
                if trigrams[i][j][k] != 0 and abs(trigrams[i][j][k] - messageTrigrams[i][j][k]) > SIMILARITY:
                    f += 1
    return f


def criterionFunctionQuadgrams(x):
    quadgrams = []
    findFrequenciesQuadgrams(x, quadgrams)
    f = 0
    for i in range(0, len(quadgrams)):
        for j in range(0, len(quadgrams[i])):
            for k in range(0, len(quadgrams[i][j])):
                for l in range(0, len(quadgrams[i][j][k])):
                    if quadgrams[i][j][k][l] != 0 and abs(quadgrams[i][j][k][l] - messageQuadgrams[i][j][k][l]) > SIMILARITY:
                        f += 1
    return f

# find any bigrams that are at the correct position
def findCorrectBigrams(x, velocity):
    bigrams = []
    velocityChanged = []
    for i in range(0, len(x)):
        velocityChanged.append(False)
    findFrequenciesBigrams(x, bigrams)
    f = criterionFunctionBigrams(x)
    # if a bigram is correct, it needs to stay in its position, therefore its velocity becomes zero
    for i in range(0, len(x) - 1):
        error = abs(bigrams[x[i]][x[i + 1]] - messageBigrams[x[i]][x[i + 1]])
        if bigrams[x[i]][x[i + 1]] > 0 and error <= f * SIMILARITY:
            velocity[i] = False
            velocityChanged[i] = True
            velocity[i + 1] = False
            velocityChanged[i + 1] = True
        elif bigrams[x[i]][x[i + 1]] > 0 and error > f * SIMILARITY:
            if not velocityChanged[i]:
                velocity[i] = True
            if not velocityChanged[i + 1]:
                velocity[i + 1] = True


# find any trigrams that are at the correct position
def findCorrectTrigrams(x, velocity):
    trigrams = []
    velocityChanged = []
    for i in range(0, len(x)):
        velocityChanged.append(False)
    findFrequenciesTrigrams(x, trigrams)
    f = criterionFunctionTrigrams(x)
    # if a trigram is correct, it needs to stay in its position, therefore its velocity becomes zero
    for i in range(0, len(x) - 2):
        error = abs(trigrams[x[i]][x[i + 1]][x[i + 2]] - messageTrigrams[x[i]][x[i + 1]][x[i + 2]])
        if trigrams[x[i]][x[i + 1]][x[i + 2]] > 0 and error <= f * SIMILARITY:
            velocity[i] = False
            velocityChanged[i] = True
            velocity[i + 1] = False
            velocityChanged[i + 1] = True
            velocity[i + 2] = False
            velocityChanged[i + 2] = True
        elif trigrams[x[i]][x[i + 1]][x[i + 2]] > 0 and error > f * SIMILARITY:
            if not velocityChanged[i]:
                velocity[i] = True
            if not velocityChanged[i + 1]:
                velocity[i + 1] = True
            if not velocityChanged[i + 2]:
                velocity[i + 2] = True


# find any quadgrams that are at the correct position
def findCorrectQuadgrams(x, velocity):
    quadgrams = []
    velocityChanged = []
    for i in range(0, len(x)):
        velocityChanged.append(False)
    findFrequenciesQuadgrams(x, quadgrams)
    f = criterionFunctionQuadgrams(x)
    # if a quadgram is correct, it needs to stay in its position, therefore its velocity becomes zero
    for i in range(0, len(x) - 3):
        error = abs(quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] - messageQuadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]])
        if quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] > 0 and error <= f * SIMILARITY:
            velocity[i] = False
            velocityChanged[i] = True
            velocity[i + 1] = False
            velocityChanged[i + 1] = True
            velocity[i + 2] = False
            velocityChanged[i + 2] = True
            velocity[i + 3] = False
            velocityChanged[i + 3] = True
        elif quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] > 0 and error > f * SIMILARITY:
            if not velocityChanged[i]:
                velocity[i] = True
            if not velocityChanged[i + 1]:
                velocity[i + 1] = True
            if not velocityChanged[i + 2]:
                velocity[i + 2] = True
            if not velocityChanged[i + 3]:
                velocity[i + 3] = True


# this function finds the index of the specified incorrectly positioned bigram
def findIncorrectBigram(x, skip = 0):
    bigrams = []
    findFrequenciesBigrams(x, bigrams)
    f = criterionFunctionBigrams(x)
    skipping = 0
    for i in range(0, len(x) - 1):
        error = abs(bigrams[x[i]][x[i + 1]] - messageBigrams[x[i]][x[i + 1]])
        if bigrams[x[i]][x[i + 1]] > 0 and error > f * SIMILARITY:
            if skipping < skip:
                skipping += 1
                continue
            else:
                return i
    return len(x) - 1


# this function finds the index of the specified incorrectly positioned trigram
def findIncorrectTrigram(x, skip = 0):
    trigrams = []
    findFrequenciesTrigrams(x, trigrams)
    f = criterionFunctionTrigrams(x)
    skipping = 0
    for i in range(0, len(x) - 2):
        error = abs(trigrams[x[i]][x[i + 1]][x[i + 2]] - messageTrigrams[x[i]][x[i + 1]][x[i + 2]])
        if trigrams[x[i]][x[i + 1]][x[i + 2]] > 0 and error > f * SIMILARITY:
            if skipping < skip:
                skipping += 1
                continue
            else:
                return i
    return len(x) - 2


# this function finds the index of specified incorrectly positioned quadgram
def findIncorrectQuadgram(x, skip = 0):
    quadgrams = []
    findFrequenciesQuadgrams(x, quadgrams)
    f = criterionFunctionQuadgrams(x)
    skipping = 0
    for i in range(0, len(x) - 3):
        error = abs(quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] - messageQuadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]])
        if quadgrams[x[i]][x[i + 1]][x[i + 2]][x[i + 3]] > 0 and error > f * SIMILARITY:
            if skipping < skip:
                skipping += 1
                continue
            else:
                return i
    return len(x) - 3

class Particle:
    def __init__(self, coordinates, initialVelocity, lowerBound, upperBound):
        self.criterionFunction = criterionFunctionBigrams
        self.findCorrectFrequencies = findCorrectBigrams
        self.findFirstIncorrectFrequency = findIncorrectBigram
        self.mode = 2
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.position = coordinates
        self.velocity = initialVelocity
        self.bestSolution = self.criterionFunction(self.position)
        self.coordinatesOfBestSolution = self.position
        self.message = toString(self.coordinatesOfBestSolution)
        self.informants = []
        self.forbidden = False
        # initialize the weight factor
        self.weight_factor = []
        for i in range(0, len(self.position)):
            self.weight_factor.append(random.uniform(0, 1))
    def move(self):
        # find the best informant
        self.bestInformant = self.informants[0]
        for j in range(1, len(self.informants)):
            if self.criterionFunction(self.informants[j].position) < self.criterionFunction(self.bestInformant.position):
                self.bestInformant = self.informants[j]
        # calculate the new velocity
        self.findCorrectFrequencies(self.position, self.velocity)
        # calculate the new particle based on velocity information
        permute = []
        for i in range(0, len(self.position)):
            if self.velocity[i]:
                permute.append(self.position[i])
        # can't have progress by looking at currently defined blocks anymore - we need to move a step further
        if not (True in self.velocity):
            if self.mode == 2:
                self.mode = 3
                self.criterionFunction = criterionFunctionTrigrams
                self.findCorrectFrequencies = findCorrectTrigrams
                self.findFirstIncorrectFrequency = findIncorrectTrigram
            elif self.mode == 3:
                self.mode = 4
                self.criterionFunction = criterionFunctionQuadgrams
                self.findCorrectFrequencies = findCorrectQuadgrams
                self.findFirstIncorrectFrequency = findIncorrectQuadgram
            # exhausted all options - the string's accuracy cannot improve anymore
            else:
                self.forbidden = True
                return
            for i in range(0, len(self.velocity)):
                self.velocity[i] = True
        # check if the particle can't move anymore
        elif len(permute) == 0:
            self.forbidden = True
            return
        # special case - if only one character is in wrong place, we need to permute the string in a different way
        elif len(permute) < self.mode:
            for i in range(0, len(self.velocity)):
                if self.velocity[i]:
                    characters = 0
                    k = i + 1
                    while k < len(self.velocity) and self.velocity[k]:
                        characters += 1
                        k += 1
                    if i == len(self.position) - 1:
                        self.position = self.position[i:] + self.position[:i]
                    else:
                        counter = 0
                        j = self.findFirstIncorrectFrequency(self.position, counter)
                        while j < i + self.mode - 1:
                            counter += 1
                            j = self.findFirstIncorrectFrequency(self.position, counter)
                            if counter == len(self.position) - 1:
                                j = len(self.position) - 1
                                break
                        if i == 0:
                            self.position = self.position[i + characters + 1:j + 1] + self.position[0:i + characters + 1] + self.position[j + 1:]
                        else:
                            self.position = self.position[0:i] + self.position[i + characters + 1:j + 1] + self.position[i:i + characters + 1] + self.position[j + 1:]
                    break
        # more than one character in wrong place - default case
        else:
            informant = True
            for i in range(0, len(self.position)):
                # no velocity - this letter will not be changed
                if not self.velocity[i]:
                    continue
                randomNumber = random.uniform(0, self.weight_factor[i])
                # 50% posibility that the new character will be from the new permutation
                if not informant or randomNumber < self.weight_factor[i]:
                    randomIndex = random.randint(0, len(permute) - 1)
                    while randomIndex == i:
                        randomIndex = random.randint(0, len(permute) - 1)
                    self.position[i] = permute.pop(randomIndex)
                # 50% possibility that the new character will be from the best informant
                else:
                    j = i
                    potentialCharacter = self.bestInformant.position[j]
                    while potentialCharacter not in permute or potentialCharacter == self.position[i]:
                        j += 1
                        if j == len(self.bestInformant.position):
                            j = 0
                        potentialCharacter = self.bestInformant.position[j]
                        # this should never happen, but just in case - if no character is in the list
                        # of characters that can be transposed, then we simply stop using that informant
                        # and just randomly transpose the existing characters
                        if j == i:
                            informant = False
                            break
                    if not informant:
                        i -= 1
                        continue
                    self.position[i] = potentialCharacter
                    for k in range(0, len(permute)):
                        if permute[k] == potentialCharacter:
                            permute.pop(k)
                            break
        # check if the particle moved to a better position
        if not self.forbidden and self.criterionFunction(self.position) < self.bestSolution:
            self.coordinatesOfBestSolution = self.position
            self.bestSolution = self.criterionFunction(self.position)
        self.message = toString(self.coordinatesOfBestSolution)


class SwarmOfParticles:
    def __init__(self, numberOfParticles, message, numberOfInformants, lowerBound, upperBound):
        calculateMessageFrequencies(MESSAGE)
        self.generation = 0
        self.canMove = True
        self.numberOfParticles = numberOfParticles
        self.dimensionality = len(message)
        self.numberOfInformants = numberOfInformants
        self.particles = []
        # initialize all particles in the swarm
        for i in range(0, numberOfParticles):
            coordinates = transpozition(MESSAGE)
            initialVelocity = []
            for j in range(0, len(message)):
                initialVelocity.append(True)
            self.particles.append(Particle(coordinates, initialVelocity, lowerBound, upperBound))
        # initialize the best values
        self.bestValue = self.particles[0].bestSolution
        self.bestCoordinates = self.particles[0].coordinatesOfBestSolution
        for i in range(1, numberOfParticles):
            if self.particles[i].bestSolution < self.bestValue:
                self.bestValue = self.particles[i].bestSolution
                self.bestCoordinates = self.particles[i].coordinatesOfBestSolution
    def moveAllParticles(self):
        change = True
        # initialize the informants of particles
        for i in range(0, self.numberOfParticles):
            informants = []
            for j in range(0, self.numberOfInformants):
                informants.append(self.particles[random.randint(0, self.numberOfParticles - 1)])
            if i >= self.numberOfParticles:
                break
            self.particles[i].informants = informants
            # change the velocities of particles and change their positions
            print("Particle no. {} is in mode {}. Difference: {}. Message: {}.".format(i + 1, self.particles[i].mode, self.particles[i].bestSolution, self.particles[i].message))
            self.particles[i].move()
            # check if the particle cannot move anymore - if so, delete it
            if self.particles[i].forbidden:
                self.particles.pop(i)
                self.numberOfParticles -= 1
                i -= 1
                continue
            # check if a better solution has been found
            elif self.particles[i].bestSolution < self.bestValue and \
                    abs(self.particles[i].bestSolution - self.bestValue) > 0.00000001:
                self.bestValue = self.particles[i].bestSolution
                self.bestCoordinates = self.particles[i].coordinatesOfBestSolution
            # reached the natural message - error is zero
            if self.bestValue == 0:
                change = False
                self.canMove = False
                return change
        self.generation += 1
        return change


messageCharacters = []
messageBigrams = []
messageTrigrams = []
messageQuadgrams = []
intMessage = []

# calculate frequencies in the message - for test purposes
def calculateMessageFrequencies(message):
    for i in range(0, len(message)):
        intMessage.append(ord(message[i]) - ord('A'))
    findFrequenciesCharacters(intMessage, messageCharacters)
    findFrequenciesBigrams(intMessage, messageBigrams)
    findFrequenciesTrigrams(intMessage, messageTrigrams)
    findFrequenciesQuadgrams(intMessage, messageQuadgrams)


''''# calculate monogram frequencies
text_file = open("monograms.txt", "r")
lines = text_file.read().split("\n")
text_file.close()
characters = []
for i in range(0, len(lines)):
    characters.append(lines[i].split(" "))
characters.sort(key=lambda x: x[0])
sum = 0
for c in characters:
    sum += int(c[1])
for c in characters:
    messageCharacters.append(int(c[1]) / sum)
    sortedCharacterFrequencies.append(int(c[1]) / sum)

# calculate bigram frequencies
text_file = open("bigrams.txt", "r")
lines = text_file.read().split("\n")
text_file.close()
bigrams = []
for i in range(0, len(lines)):
    bigrams.append(lines[i].split(" "))
bigrams.sort(key=lambda x: x[0])
sum = 0
for b in bigrams:
    sum += int(b[1])
for i in range(0, len(bigrams)):
    if i % 26 == 0:
        messageBigrams.append([])
        sortedBigramFrequencies.append([])
    messageBigrams[int(i / 26)].append(int(bigrams[i][1]) / sum)
    sortedBigramFrequencies[int(i / 26)].append(int(bigrams[i][1]) / sum)
sortedCharacterFrequencies.sort()
for i in range(0, len(sortedBigramFrequencies)):
    sortedBigramFrequencies[i].sort()'''