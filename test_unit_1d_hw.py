from unit_1d_hw import *
import random

def test_if_practice_1():
    assert if_practice_1(5) == "X is 5!", "When X is 5 must print 'X is 5!'"
    assert if_practice_1(6) == "X is 6!", "When X is 6 must print 'X is 6!'"
    assert if_practice_1(random.randint(7,100)) == "X is not 5 or 6!"
    assert if_practice_1(random.randint(-100, 3)) == "X is not 5 or 6!"

def test_if_practice_2():
    assert if_practice_2("y") == True, "Passed in y but did not return True"
    assert if_practice_2("Y") == True, "Passed in Y but did not return True"
    assert if_practice_2("N") == False, "Passed in N but did not return False"
    chars = ["abcdefghijklmnopqrstuvwxz"]
    assert if_practice_2(chars[random.randint(0, 24)]) == False, "Passed in a non y or Y value and did not return False"

def test_if_practice_3():
    assert if_practice_3(random.randint(1,9)) == False, "score was not divisible by 10 but did not return False"
    assert if_practice_3(random.randint(0, 99) * 10) == True, "score was divisible by 10 but did not return True"

def test_if_practice_4():
    assert if_practice_4(random.randint(0, 9)) == 0
    assert if_practice_4(10) == 1
    assert if_practice_4(random.randint(11, 20)) == 2

def test_for_loop_1():
    l = for_loop_1()
    value = random.randint(0, 99)
    assert l[value] == value%10 + 1
    value = random.randint(0, 99)
    assert l[value] == value%10 + 1
    value = random.randint(0, 99)
    assert l[value] == value%10 + 1

def test_for_loop_2():
    l = for_loop_2()
    value = random.randint(0, 99)
    assert l[value] == value
    value = random.randint(0, 99)
    assert l[value] == value
    value = random.randint(0, 99)
    assert l[value] == value
    value = random.randint(0, 99)
    assert l[value] == value

def test_for_loop_3():
    l = for_loop_3()
    for num in l[1::4]:
        assert num == 2, "1 must be replaced with 2, did not find a 2 where a 1 was before"

def test_while_loop_1():
    value = random.randint(0, 999) 
    new_value = while_loop_1(value)
    assert new_value < 0, "Value returned was not negative "
    assert new_value > -4, "Value exceeded the decrement value"
    new_value_1 = while_loop_1(1)
    new_value_2 = while_loop_1(6)
    assert new_value_1 == -2
    assert new_value_2 == -3


def test_while_loop_2():
    break_num = while_loop_2()
    assert break_num == 5, f"Can only break on the num 5, you broke on the num '{break_num}'"
