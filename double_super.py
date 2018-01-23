class Base:
    def __init__(self):
        print("in Base init")

class Sup1(Base):
    def __init__(self):
        print("in Sup1 init")
        super().__init__()

class Sup2(Sup1):
    def __init__(self):
        print("in Sup2 init")
        Sup1.__init__(self)

s2 = Sup2()
