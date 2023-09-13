class Env:
    def __init__(self, n) -> None:
        """ Create Env nxn matrix with  0 as clean and 1 as dirt """
        self.n = n
        self.Agent_x = 0
        self.Agent_y = 0
        self.env = [[randint(0, 1) for a in range(n)] for _ in range(n)]
        # self.env = [[0 for a in range(n)] for _ in range(n)]

    def display(self) -> None:
        for a in range(self.n):
            for b in range(self.n):
                print(self.env[a][b], end=" ")
            print()

    def index(self, x, y):
        return (self.env[x][y])

    def AgentlocChange(self, x, y):
        if (x < self.n and y < self.n):
            self.env[self.Agent_x][self.Agent_y] = 0
            self.env[x][y] = 'A'
            self.Agent_x, self.Agent_y = x, y

    def dirtPresent(self) -> bool:
        sm = 0
        for a in self.env:
            for b in a:
                if type(b) == int:
                    sm += b
        return sm != 0

    def isAvailable(self, x, y) -> bool:
        if x < self.n and y < self.n:
            return True
        else:
            return False

    def AgentPostion(self):
        return (self.Agent_x, self.Agent_y)

    def isDirt(self, x, y):
        if self.env[x][y] == 1:
            return True
        return False


class Agent:
    def __init__(self, env: Env) -> None:
        self.env = env
        self.x = 0  # agent location
        self.y = 0
        self.n = self.env.n
        self.percept_Sequenc = []
        self.env.AgentlocChange(self.x, self.y)
        self.env.display()

    def left(self):
        if (self.env.isAvailable(self.x-1, self.y)):
            self.x -= 1
            self.env.AgentlocChange(self.x, self.y)

    def right(self):
        if (self.env.isAvailable(self.x+1, self.y)):
            self.x += 1
            self.env.AgentlocChange(self.x, self.y)

    def up(self):
        if (self.env.isAvailable(self.x, self.y-1)):
            self.y -= 1
            self.env.AgentlocChange(self.x, self.y)

    def down(self):
        if (self.env.isAvailable(self.x, self.y+1)):
            self.y += 1
            self.env.AgentlocChange(self.x, self.y)

    def clean(self):
        while self.env.dirtPresent() != 0:
            x, y = self.env.AgentPostion()
            print("-----------------------------------------------------")
            self.env.display()
            print("-----------------------------------------------------")
            # checking in right
            if (self.env.isAvailable(x+1, y) and self.env.isDirt(x+1, y)):
                self.right()
                continue
            # checking in left
            if (self.env.isAvailable(x-1, y) and self.env.isDirt(x-1, y)):
                self.left()
                continue
            # checking in up
            if (self.env.isAvailable(x, y-1) and self.env.isDirt(x, y-1)):
                self.up()
                continue
            # checking in down
            if (self.env.isAvailable(x, y+1) and self.env.isDirt(x, y+1)):
                self.down()
                continue
            self.env.AgentlocChange(x+randint(0, 1), y+randint(0, 1))

        self.env.display()


En = Env(6)
Agnt = Agent(En)
# print(En.dirtPresent())
Agnt.clean()
