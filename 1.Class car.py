class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_description(self):
     return ( f' {self.make} {self.model} {self.year}')
        
    def read_odometer(self):
        print (self.odometer_reading)
        
    def update_odometer(self,new_reading):
        if new_reading > self.odometer_reading :
            self.odometer_reading = new_reading
            return self.odometer_reading
        else:
            print('This not rithg')
    def incremant_odometer(self,incremant_reading):
        self.odometer_reading += incremant_reading
        return self.odometer_reading

s= car ('BMV','IMP4',2024)
print(s.get_description())
s.read_odometer()
s.update_odometer(30)
s.read_odometer ()
s.incremant_odometer(70)
s.read_odometer()
                
            
        
        
