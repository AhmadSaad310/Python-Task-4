class  Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print (f'{self.name} {self.age}')
    def sitt(self):
        print ('The dog is sitting')
    def roll_over(self):
        print('The dog is rolling over')
n=Dog('Max',3)
n.sitt()
n.roll_over()
