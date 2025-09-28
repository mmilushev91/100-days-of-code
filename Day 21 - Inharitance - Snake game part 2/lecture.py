class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    
    def __init__(self):
        super().__init__()
    
    def breath(self):
        super().breath()
        print("Doing it underwater")
    
    def swim(self):
        print("Moving in the water")
    
nemo = Fish()

print(nemo.num_eyes) # 2
nemo.breath() # Inhale, Exhale.
nemo.swim() # Moving In the water
