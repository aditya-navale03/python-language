class Country:
    def __init__(self,nationality):
        self.nationality = nationality
        
    def print_n(self):
        print("Natinality:-",self.nationality)
        
        
class state(Country):
    def __init__(self,nationality,country,state):
        super().__init__(nationality)
        self.country = country
        self.state = state
        
    def print_s(self):
        print("state:-",self.state)
        
        
    def detail_prit(self):
        print("stste:_",self.state)
        self.print_n()
        self.print_s()        
        
s = Country('indain')
s.print_n()
b = state('s','d','rf')
b.print_n()
b.print_s()
b.detail_prit()