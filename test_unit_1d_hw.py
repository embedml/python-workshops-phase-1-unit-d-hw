
import random
from unit_1d_hw import *

def test_car_class():
    car_class = Car(miles_per_gallon=28.5)
    assert car_class.mpg == 28.5, "You must create a class called Car with an initialization function that sets the parameter 'mpg'."

    car_class = Car(miles_per_gallon=16.932)
    assert car_class.mpg == 16.932, "You must create a class called Car with an initialization function that sets the parameter 'mpg'."

def test_dog_class():
    dog_class = Dog(breed="Dobermann", weight=92.5)
    assert dog_class.breed == "Dobermann", "Make sure that your initialization function for the class Dog is correclty setting the breed field."
    assert dog_class.weight == 92.5, "Make sure that your initialization function for the class Dog is correclty setting the weight field."
    assert dog_class.get_breed() == "Dobermann", "Make sure that your 'get_breed' function is correctly returning the breed value."
    assert dog_class.get_weight() == 92.5, "Make sure that your 'get_weight' function is correctly returning the weight value."
    
    dog_class = Dog(breed="Chihuahua", weight=5.234)
    assert dog_class.breed == "Chihuahua", "Make sure that your initialization function for the class Dog is correclty setting the breed field."
    assert dog_class.weight == 5.234, "Make sure that your initialization function for the class Dog is correclty setting the weight field."
    assert dog_class.get_breed() == "Chihuahua", "Make sure that your 'get_breed' function is correctly returning the breed value."
    assert dog_class.get_weight() == 5.234, "Make sure that your 'get_weight' function is correctly returning the weight value."
    
def test_math_operations_class():
    math_operations = Math_Operations()
    assert math_operations.add(a=4, b=5) == 9, "Make sure that your 'add' member function takes in a and b and returns the result of adding them together"
    assert math_operations.sub(a=4, b=5) == -1, "Make sure that your 'sub' member function takes in a and b and returns the result of (a-b)"
    assert math_operations.slope_intercept(m=10, x=4, b=5) == 45, "Make sure that your 'slope_intercept' member function takes in m, x, and b and returns the result of (m * x + b)"
    assert math_operations.pythagorean(a=3, b=4) == 5, "Make sure that your 'pythagorean' member function takes in a and b and returns the value of the hypotenuse of a right triangle with those two side lengths"
    
    assert math_operations.add(a=26.3, b=-16.2) == (26.3-16.2), "Make sure that your 'add' member function takes in a and b and returns the result of adding them together"
    assert math_operations.sub(a=17.23, b=28.3) == (17.23-28.3), "Make sure that your 'sub' member function takes in a and b and returns the result of (a-b)"
    assert math_operations.slope_intercept(m=2.43, x=10, b=-23) == (2.43*10-23), "Make sure that your 'slope_intercept' member function takes in m, x, and b and returns the result of (m * x + b)"
    assert math_operations.pythagorean(a=6, b=8) == 10, "Make sure that your 'pythagorean' member function takes in a and b and returns the value of the hypotenuse of a right triangle with those two side lengths"
    