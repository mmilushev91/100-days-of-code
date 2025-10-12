#unlimitted positional arguments

def add(*args):
    #args eguals to tuple
    return sum(args)
    
print(add(1, 2, 3 ,4 ,5))

#unlimitted keyword arguments
def calculator(num, **kwargs):
    #kwargs == dictionary
    result = num
    
    result += kwargs["add"]
    result *= kwargs["multiply"]
    
    return result 

print(calculator(num=3, add=3, multiply=3))

class Car:
    
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        
car = Car(model="nissan")
print(car.model)
print(car.color)
