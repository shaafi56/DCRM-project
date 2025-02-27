# define the class named Cars
class cars:
    #inside the class we created two functions
    def __init__(self, brand , model, year):
        self.brand = brand 
        self.model = model
        self.year = year
    

car1 = cars("BMW", "4a", 2019)
print(f"model: {car1.model} \nbrand: {car1.brand} \nyear: {car1.year}")
    


