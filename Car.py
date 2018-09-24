#car
#2018 09 18
#Cheung Anthony

# Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# A sample output would be like this:?

class Car:
    price=0
    tax=0
    def __init__(self,price,speed,fuel,mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
    def display_all(self):
        if self.price > 10000:
            self.tax=0.15
        else:
            self.tax=0.12
        print("Price: "+ str(self.price)+ "\nSpeed: "+ self.speed + "\nFuel: "+ str(self.fuel) + "\nMileage: "+ str(self.mileage) +"\nTax: " +str(self.tax) + "\n")
        return self
car1=Car(2000,"35mph","Full","15mpg")
car2=Car(2000,"5mph","Not Full","105mpg")
car3=Car(2000,"15mph","Kind of Full","95mpg")
car4=Car(2000,"25mph","Full","25mpg")
car5=Car(2000,"45mph","Empty","25mpg")
car6=Car(20000000,"35mph","Empty","15mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
