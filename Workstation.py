class Workstation:
    def __init__(self, id, next_workstation):
        self.id = id
        self.products = []
        self.next_workstation = next_workstation
        self.history = []

    def writeworkstationhistory(self):
        temp = []
        for i in range(len(self.products)):
            temp.append(self.products[i].id)
        self.history.append(temp)

    def fromworkstationtoproduct(self, productlist, stat):
        for i in range(len(productlist)):
            if self.products[0].id == productlist[i].id:
                index = i
        productlist[index].empty = stat