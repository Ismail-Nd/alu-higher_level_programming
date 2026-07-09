class Mother:
    def __init__(self, eye, infection):
        self.eye = eye
        self.infection = infection

    

class Father:
    def __init__(self):
        self.height = "tall"

class ismail(Mother, Father):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)

me = ismail()
print(me.eye, me.height)
