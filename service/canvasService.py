import tkinter
from config import canvasConfig


class CanvasService:

    def __init__(self):
        self.canvas = tkinter.Canvas(width=canvasConfig.width, height=canvasConfig.height, bg="white")
        self.canvas.pack()

    """Vytvori lod na canvase"""
    def createBoat(self, boat):
        # vytvori telo lode
        self.createBoatBody(boat.location[0], boat.location[1])
        # vytvori vlajku lode
        self.createBoatFlag(boat.location[0], boat.location[1], boat.flagThirdPointLocation)

    """Vytvori telo lode"""
    def createBoatBody(self, locationX, locationY):
        self.canvas.create_polygon(
            locationX - 20, locationY,
            locationX + 20, locationY,
            locationX + 10, locationY + 10,
            locationX - 10, locationY + 10

        )

    """Vytvori vlajku lode"""
    def createBoatFlag(self, locationX, locationY, thirdPoint):
        self.canvas.create_polygon(
            locationX, locationY,
            locationX, locationY - 20,
            thirdPoint[0], thirdPoint[1],
            fill="white",
            outline="black"
        )

    """Pocka danny pocet milisekund"""
    def wait(self, miliseconds):
        self.canvas.after(miliseconds)

    """Aktualizacia canvasu"""
    def updateCanvas(self):
        self.canvas.update()
        self.canvas.pack()

    def text(self, text):
        self.canvas.create_text(200, 200, text=text)

    """Vypise vyhercu"""
    def printWinner(self, index):
        self.canvas.delete("all")
        self.canvas.create_text(canvasConfig.width/2, canvasConfig.height/2, text="VYHRAL: {}".format(index + 1), font=("Purisa", 18))

    """Vycisti canvas"""
    def deleteAll(self):
        self.canvas.delete("all")

    """Kresli cielovu ciaru"""
    def createFinalLine(self):
        self.canvas.create_line(
            canvasConfig.finalLineXLocation, 0,
            canvasConfig.finalLineXLocation, canvasConfig.height
        )

    def mainloop(self):
        self.canvas.mainloop()
