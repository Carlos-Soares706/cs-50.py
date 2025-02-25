from numb3rs import validate

def main():
    test_structure()
    test_numbers()

def test_structure():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False

def test_numbers():
    assert validate('1.1.1.1') == True
    assert validate('255.255.255.255') == True
    assert validate('500.255.255.255') == False
    assert validate('255.500.255.255') == False
    assert validate('255.255.500.255') == False
    assert validate('255.255.255.500') == False

if __name__ == "__main__":
    main()
