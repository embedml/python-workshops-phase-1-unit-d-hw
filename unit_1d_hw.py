'''
Welcome to the control flow homework! This homework will take
the concepts you learned from the previous homework and use them 
in new ways with control flow. 

There will also be small formatting/return statements to ensure that
the question was answered correctly. 
'''
import random


######## if, elif, else ########

def if_practice_1(num):
    '''
    num is going to be a random number, use if, elif and else to return a value to the tester. 
    
    If, num is 5, it should return a string "num is 5!"
    Else if num is 6, it should return a string "num is 6!"
    Else if num is not 6 or 5, it should return the string "num is not 5 or 6!"
    '''
    # Note: You will have to indent the return statements onces you create your if, elif and else statements

    # Put/alter your code below#
    
    return "num is 5!"
    
    return "num is 6!"
    
    return "num is not 5 or 6!"
    ######################

def if_practice_2(user_input):
    '''
    Some user has typed in a string value and it is being passed in as the variable
    `user_input`. 

    Check to see if the value is a "y" or a "Y" if it is return True
    otherwise return the value False
    '''
    #user_input
    return True

    return False

def if_practice_3(score):
    '''
    You have a score board that can only take in values that are divisible by ten. 
    
    The value will be passed in as the variable `score`. If the score is not divisible by 10
    then return False, otherwise return True

    Hint: Use modulo to determine if the score is divisible by 10
    '''
    #score
    return True
    return False

def if_practice_4(item_price):
    '''
    Python lets you automate decisions. In this exercise a value will be given a price
    stored in the `item_price` variable. If the item is more than the fair price 
    given, then return 2, if the item_price is the same as the fair_price then 
    return 1, if it it less then the fair price then return 0
    
    '''
    fair_price = 10 # Use this varible but do not alter 10



########## for loops ###########

def for_loop_1():
    '''
    Given a list called `nums` add 1 to each item in the list

    Hint: Use a variable to increment the index
    Hint: or use `enumerate` to get the current index and value     ` 
    '''
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 100 # List with pattern [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3  ...]
    return nums

def for_loop_2():
    '''
    Use a for loop to create a list that has the values [0, 1, 2, 3, 4, 5, ... 99] the numbers (0 - 99)
    Assign the list to the variable sequence 
    '''
    sequence = [] # Hint: Look up the append feature of a list!
    return sequence


def for_loop_3():
    '''
    A list with 400 elements will be given.
    For each entry with a value of 1, replace it with a value of 2

    Hint: Iterate through all elements in the list, then check if the value is a 1, if it is a one use that index of the list
    to write the value as a 2. 

    Hint Hint: Use the variable index to keep track of the index you are on  

    BONUS POINTS (Optional): Use the enumerate function on the list to get index and value https://realpython.com/python-enumerate/

    '''
    x = [0, 1, 0, 3] * 400 # List with pattern [0, 1, 0, 3, 0, 1, 0, 3, ...  3]
    index = 0 # Depending on your implementation you may not need index
    # Put/alter your code below#
    
    ######################
    return x


########## while loops #########

def while_loop_1(num):
    '''
    Create while loop that subtracts the passed in variable `num` by 5 and reassigns `num` that new value. 
    Once the value becomes negative the while loop should end. 

    Ex: If num is 3, subtract by 5, now num is -2 and should break out of the loop

    # Hint: Use the condition of the while loop to stop the while loop!
    '''
    # Add your code below! #

    return num



def while_loop_2():
    '''Create a while loop that will only break if the expression for the while loop evaluates to the number 5'''
    x = None
    '''
    The loop's condition should have the loop stop when the value of `x` is equal to 5.
    Then, inside the while loop use the code below to generate a new number for `x` on every single iteration of the loop
        x = random.randint(0, 10) # This should live in the while loop, so you may need to indent it once you have the while loop implemented
    (Note on random.randint(). This will generate an integer between the two values passed in each time it is run, this case a random number between
    0 and 10)
    '''
    # Put/alter your code below#
    
    x = random.randint(0, 10) # This should live in the while loop, so you may need to indent it once you have the while loop implemented
    ######################
    return x
