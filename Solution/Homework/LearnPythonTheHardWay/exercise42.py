## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is_a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pets = list()
    def add_pet(self,pet):
		self.pets.append(pet)

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a Person and the initializer of Person needs a name 
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
	
## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet 
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has_a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()