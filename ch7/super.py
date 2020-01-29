class father:
    def __init__(self,x=5):
        self.x = x

class child(father):
    # def __init__(self, x, a):
    #     self.x = x
    #     self.a = a
    def __init__(self, x, a):
        super().__init__(x)
        self.a = a
 
    def test(self):
        print(self.x * self.a)
 
c = child(8, 9)
c.test()