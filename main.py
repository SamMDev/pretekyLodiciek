import random
# objekt lode
from model.Boat import Boat
# predpisane cisla, ktore mozeme menit
from config import canvasConfig
from service.canvasService import CanvasService

# stara sa o canvas
canvasService = CanvasService()
# zoznam lodiek
boats = []

"""
Zisti maximalnu hodnotu x-ovych suradnic zo vsetkych lodi
"""


def getMaximumXValue(listOfBoats):
    maximumValue = 0
    for boat in listOfBoats:
        if float(boat.location[0]) > maximumValue:
            maximumValue = float(boat.location[0])

    return maximumValue


"""
Zisti index maximalnej hodnoty: zisti tym aj index prvej lode
"""


def getIndexOfMaxValue(listOfBoats):
    xLocations = []
    for boat in listOfBoats:
        xLocations.append(boat.location[0])

    return xLocations.index(getMaximumXValue(boats))


"""
Vygeneruje tretiu suradnicu pre vlajku, ktora bude nahodna
"""


def generateRandomFlag(locationOfBoatX, locationOfBoatY):
    return [
        random.randint(locationOfBoatX - 20, locationOfBoatX + 20),
        random.randint(locationOfBoatY - 20, locationOfBoatY)
    ]


"""
Vygeneruje nahodnu rychlost
"""


def generateRandomSpeed():
    return random.randint(1, 6)


"""
Prva pozicia lodiek
    loop: pre kazdu lodku
"""
for i in range(canvasConfig.numOfBoats):
    # Pozicia y pri konkretnych lodkach zavisi od indexu lode (su pod sebou)
    yPosition = (canvasConfig.height - 50) / canvasConfig.numOfBoats * (i + 1)

    # prida do zoznamu lodi konkretne objekty lodi, ktorym urci zaciatocne suradnice
    boats.append(
        Boat(
            # tretia suradnica pre vlajku (ostatne nam netreba, lebo sa daju vypocitat z polohy)
            generateRandomFlag(20, yPosition),
            # lokacia lode
            [20, yPosition],
            # Zaciatocna rychlost
            0
        )
    )

# aplikuje ich na canvas
for boat in boats:
    canvasService.createBoat(boat)
    canvasService.updateCanvas()


"""
Tu zacina zavod
"""
while getMaximumXValue(boats) < canvasConfig.finalLineXLocation - 20:

    # na zaciatku kazdeho dalsieho loopu vycisti canvas
    canvasService.deleteAll()

    # pre kazdu lodku
    for boat in boats:
        # vygeneruje jej novy rychlost
        boat.speed = generateRandomSpeed()
        # zvacsi jej x-ovu polohu v zavislosti od jej novej rychlosti
        boat.location[0] += boat.speed
        # vygeneruje novu polohy vejucej vlajky
        boat.flagThirdPointLocation = (generateRandomFlag(boat.location[0], boat.location[1]))

        # aplikuje ju na canvas
        canvasService.createBoat(boat)

    # pocka 50 milisekund
    canvasService.wait(50)
    # stale musi kreslit finalnu cieru (lebo stale mazeme canvas)
    canvasService.createFinalLine()
    # canvas sa aktualizuje a zobrazi s uz novymi udajmi
    canvasService.updateCanvas()

"""
Ak skonci loop (niektora z lodi dovrsila finalnu ciaru),
vypise sa vitaz
"""
canvasService.printWinner(getIndexOfMaxValue(boats))

canvasService.mainloop()
