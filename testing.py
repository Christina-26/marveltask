"""testing functions"""

def add(number_a, number_b):
    """
    This function adds 2 numbers
    """
    return number_a  + number_b 
def test_add():
    """testing add function"""
    print(add(2,3)==5)
    print(add(0, 42) == 42)
    print(add(-1, 1) ==0 )
test_add()