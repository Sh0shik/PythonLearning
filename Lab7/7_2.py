import abc

class CargoContainer(abc.ABC):

    def __init__(self, max_weight, current_weight):
        self.max_weight = max_weight
        self.current_weight = current_weight

    @abc.abstractmethod 
    def get_free_space(self):
        pass
    
    @abc.abstractmethod 
    def is_overloaded(self):
        pass

    def info(self):
        return f"{self.__class__.__name__} - Free Space: {self.get_free_space()}, Overloaded: {self.is_overloaded()}"

class StandardContainer(CargoContainer):

    def get_free_space(self):
        return self.max_weight - (self.current_weight + self.current_weight * 0.1)  # 10% of current weight is considered as occupied space

    def is_overloaded(self):
        return (self.current_weight * 1.1) > self.max_weight

class  RefrigeratedContainer(CargoContainer):

    def get_free_space(self):
        return self.max_weight - (self.current_weight + self.current_weight * 0.3)  # 30% of current weight is considered as occupied space

    def is_overloaded(self):
        return (self.current_weight * 1.3) > self.max_weight

standard = StandardContainer(100, 80)
refrigerated = RefrigeratedContainer(100, 80)

print(standard.info())
print(refrigerated.info())