class Product:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.history = [[], [], []]
        self.component = []
        self.empty = 0

    def moving(self):
        self.location.products.remove(self)
        self.location.next_workstation.products.append(self)
        self.location = self.location.next_workstation

    def move(self, i ,formula):
        if len(self.component[i]) < formula:
            self.history[2].append("Lack of component")
        elif self.location.next_workstation.next_workstation is None:
            self.moving()
            self.history[2].append("Success")
        elif len(self.location.next_workstation.products) >= 1:
            self.history[2].append("Waiting")
        else:
            self.moving()
            self.history[2].append("Success")

    def writeproducthistory(self):
        self.history[0].append(self.location.id)
        temp = []
        for i in range(len(self.component)):
            for j in range(len(self.component[i])):
                temp.append(self.component[i][j].id)
        self.history[1].append(temp)

