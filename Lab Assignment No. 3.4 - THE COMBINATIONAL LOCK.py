class ComboLock:
    def __init__(self, secret1: int, secret2: int, secret3: int):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
        self.checkpoint = 0
        self.positionpointer = 0


    def reset(self):
        self.positionpointer = 0
        self.checkpoint = 0
        print(f"You resetted: Current position: {self.positionpointer}, Current state: {self.checkpoint}")

    def turnRight(self, ticks):


        if self.positionpointer == self.secret2 and self.checkpoint == 2:
            self.checkpoint = 3

        elif self.positionpointer != self.secret2 and self.checkpoint == 2:
            self.checkpoint = 0
        self.positionpointer = (self.positionpointer + ticks) % 40


        if self.positionpointer == self.secret1 and self.checkpoint == 0:
            self.checkpoint = 1

        elif self.checkpoint == 1:
            self.checkpoint = 0

        print(f"Current position: {self.positionpointer}, Current state: {self.checkpoint}")

    def turnLeft(self, ticks):
        self.positionpointer = (self.positionpointer-ticks) % 40
        if  self.checkpoint == 1:
            self.checkpoint = 2


        elif self.positionpointer == self.secret1 and self.checkpoint == 3:
            self.checkpoint = 2
        elif self.positionpointer != self.secret1 and self.checkpoint == 3:
            self.checkpoint = 0



        print(f"Current position: {self.positionpointer}, Current state: {self.checkpoint}")


    def open(self):
        if self.positionpointer == self.secret3 and self.checkpoint == 3:
            print("You unlocked the combinational lock")
        else:
            print("You are unable to unlock the combinational lock")

lock= ComboLock(38, 4, 0)
lock.turnRight(38)
lock.turnLeft(31)
lock.turnLeft(3)
lock.turnLeft(1)
lock.turnLeft(39)
lock.turnRight(36)
lock.turnRight(1)
lock.turnRight(39)

lock.reset()

lock.turnRight(38)
lock.turnLeft(34)
lock.turnRight(36)
lock.open()