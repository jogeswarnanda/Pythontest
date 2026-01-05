def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5))


# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     print(type(kwargs))

# calculate(add=1, sub=2, mul=3, div=4)

def calculate(n, **kwargs):
    
    n += kwargs["add"]
    n *= kwargs["mul"]
    print( "result :" , n)
    
calculate(2,add=3,  mul=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Toyota", model="Corolla", color="red", seats=5)
print(my_car.make, my_car.model, my_car.color, my_car.seats)
