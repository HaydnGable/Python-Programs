#Haydn Gable, Python M03 Case Study
"""
This app prompts the user the enter a vehicle's type and data, then
prints the output data. 
"""

#Parent Vehicle class with vehicle type attribute
class Vehicle:
    def __init__(self, vtype):
        self.vtype = vtype
        
#Child Automobile class with other attributes and inherited type attribute        
class Automobile(Vehicle):
    def __init__(self, vtype, year, make, model, doors, roof):
        super().__init__(vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#Print method to neatly print all vehicle data
    def print(self):
        print(f"Vehicle type: {self.vtype}, Year: {self.year}, Make: {self.make}, Model: {self.model}, Number of doors: {self.doors}, Type of roof: {self.roof}.")

#Automobile class object that the user inputs the car data into
vehicle = Automobile(
input("Enter the type of the vehicle: "),
input("Enter the year of the vehicle: "),
input("Enter the make of the vehicle: "),
input("Enter the model of the vehicle: "),
input("Enter the number of doors of the vehicle: "),
input("Enter the roof type of the vehicle: ")
)

#Call the print method of the Automobile class with the vehicle object
vehicle.print()
