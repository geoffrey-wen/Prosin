class Material:
    def __init__(self, id, location, type):
        self.id = id
        self.location = location
        self.history = []
        self.type = type
        #tambahin attrib kapan material masuk

    def process(self, i, formula):
        if len(self.location.next_workstation.products[0].component[i]) < formula:
            self.location.products.remove(self)
            self.location.next_workstation.products[0].component[i].append(self)
            self.location = self.location.next_workstation.products[0]
        self.history.append(self.location.id)
        return self.location