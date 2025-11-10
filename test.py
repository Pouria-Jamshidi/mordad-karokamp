class Game:
    programType = "Video game"

    def __init__(self, gameName, gameCategory, gameScore, gamePrice=0.0):
        self.name = gameName
        self.category = gameCategory
        self.score = gameScore
        self.price = gamePrice
        self.installed = False

    def __repr__(self):
        return f"enlarges the game icon"

    def callThegame(self):
        print(
            f"game's name is {self.name}, it is a {self.category} game with {self.score} points, only at affordable price of {self.price}$")

    def install(self):
        if self.installed == True:
            start = input("the game is already installed on your system, do you want to run the game? (y/n): ")
            if start == "y" or start == "Y":
                self.run()
        elif self.installed == False:
            while True:
                ins = input("do you want to install it? (y/n) ")
                if ins == "y" or ins == "Y":
                    print("installing game...")
                    self.installed = True
                    print(f"{self.name} is now installed on your pc")
                    break
                elif ins == "n" or ins == "N":
                    print("closing game...")
                    print(f"{self.name} is closed")
                    break
                else:
                    print("invalid input")
                    continue

    def run(self):
        if self.installed == False:
            print(
                "the game is corrently not installed on your pc, please install it first before trying to run the game!!")
            self.install()
        if self.installed == True:
            print(f"{self.name} has started running on background")


print(Game.programType)
silksong = Game("SilkSong", "metrovania", 9.8, 19.99)
print(silksong)
silksong.callThegame()
silksong.install()
silksong.install()