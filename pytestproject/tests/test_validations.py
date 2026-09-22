# Validate using Greater than
def test_validate_greaterthan():
    assert (10 > 5)

def test_validate_greaterthanequalto():
    assert (10 >= 10)

def test_validate_lessthan():
    assert (45 < 75)

def test_validate_lessthanequalto():
    assert (55 <= 80)

def test_validate_equalto():
    assert (65==65)

def test_validate_notequalto():
    assert (65 != 95)

def test_validate_contains():
    s1="Welcome"
    s2="Every one is Welcome to Dasara"
    assert (s1 in s2)

def test_validate_notcontains():
    s1="Program"
    s2="Every one is Welcome to Dasara"
    assert (s1 not in s2)

def test_validate_referenceofdata():
    s1="Welcome"
    s2="Welcome"
    assert (s1 is s2)

def test_validate_referenceofdatainverse():
    s1="Welcome"
    s2="Good Evening"
    assert (s1 is not s2)

def test_validate_startswithdata():
    s1="S G Software Testing Institute"
    assert (s1.startswith('S G'))

def test_validate_endswithdata():
    s1="S G Software Testing Institute"
    assert (s1.endswith('Institute'))

def test_validate_uppercase():
    s1="S G TESTING"
    assert(s1.isupper()==True)

def test_validate_lowercase():
    s1="s g testing"
    assert(s1.islower()==True)

def test_validate_stringtitle():
    s1="Python Program Code"
    assert(s1.istitle()==True)

def test_validate_list_flowers():
    flowers=["Lotus","Lilly","sunflower","Cosmos"]
    assert(len(flowers)==4)

def test_validate_tuple():
    tuple=("Apple","Mango",True,15.175,"Mango")
    assert(tuple.count("Mango")==2)

def test_validate_dictionary():
    student={
        "fname":"Santosh",
        "course":"Science and Research",
        "age":23
    }
    assert(student.get("fname")=='Santosh')