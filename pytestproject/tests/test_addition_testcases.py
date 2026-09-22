from sourcecode.mathsbasics import addition

# Add Two Positive Numbers
def test_add_two_positive_numbers():
    num1=12
    num2=10
    expected=22
    actual=addition(num1,num2)
    assert (actual==expected)

# Add Two Negative Numbers
def test_add_two_negative_numbers():
    num1=-45
    num2=-15
    expected=-60
    actual=addition(num1,num2)
    assert (actual==expected)

# Add one positive and one negative numbers
def test_add_positive_negative_numbers():
    num1=65
    num2=-30
    expected=35
    actual=addition(num1,num2)
    assert(actual==expected)

# Add positive numebr with zero
def test_add_positive_with_zero():
    num1=77
    num2=0
    expected=77
    actual=addition(num1,num2)
    assert(actual== expected)

# Add negative numebr with zero
def test_add_negative_with_zero():
    num1=-70
    num2=0
    expected=-70
    actual=addition(num1,num2)
    assert(actual== expected)

# Add Multiple positive numbers
def test_add_multiple_numbers():
    list=[10,20,30,40]
    expected=100
    actual=0
    for element in list:
        actual=actual+element
    assert(actual==expected)
    