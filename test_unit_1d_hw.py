
import random
from unit_1d_hw import *

def test_car_class():
    mpg = random.randrange(-999,999)
    car_class = Car(miles_per_gallon=mpg)
    assert car_class.mpg == mpg, f"Expected car_class's mpg field to be {mpg} but your class's mpg field contained {car_class.mpg}"

def test_dog_class():
    possible_dog_breeds = {"American Foxhound":66.87, "Australian Shepherd":37, "Beagle":20.3, "Chihuahua":4.53, "Great Dane":144.2, "Greyhound":70.96, "Mastiff":220.3, "Newfoundland":135.2, "Papillon":9.2, "Poodle":5.55, "Pug":16.01, "Rottweiler":122.3, "Shih Tzu":12.2, "Yorkshire Terrier":6.46}
    key = random.choice(list(possible_dog_breeds.keys()))     
    dog_class = Dog(breed=key, weight=possible_dog_breeds[key])
    assert dog_class.breed == key, f"Expecting breed field to be {key} but your class's field contianed {dog_class.breed}"
    assert dog_class.weight == possible_dog_breeds[key], f"Expected weight field to be {possible_dog_breeds[key]} but your class's field contained {dog_class.weight}."
    assert dog_class.get_breed() == key, f"Expecting get_breed() function to return {key} but your function returned {dog_class.get_breed()}"
    assert dog_class.get_weight() == possible_dog_breeds[key], f"Expected get_weight() function to return {possible_dog_breeds[key]} but your function returned {dog_class.get_weight()}."
    
def test_math_operations_class():
    math_operations = Math_Operations()
    a = random.randrange(-999,999)
    b = random.randrange(-999,999)
    m = random.randrange(-999,999)
    assert math_operations.add(a=a, b=b) == (a+b), f"Math_Operations: expected your add function to return {(a+b)} but it returned {math_operations.add(a=a, b=b)}"
    assert math_operations.sub(a=a, b=b) == (a-b), f"Math_Operations: expected your sub function to return {(a-b)} but it returned {math_operations.sub(a=a, b=b)}"
    assert math_operations.slope_intercept(m=m, x=a, b=b) == m*a+b, f"Math_Operations: expected your slope_intercept function to return {m*a+b} but it returned {math_operations.slope_intercept(m=m, x=a, b=b)}"
    assert math_operations.pythagorean(a=a, b=b) == (a**2+b**2)**0.5, f"Math_Operations: expected your pythagorean function to return {(a**2+b**2)**0.5} but it returned {math_operations.pythagorean(a=a, b=b)}"
    