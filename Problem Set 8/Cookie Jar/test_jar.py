from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(50)
    assert jar2.capacity == 50
    jar3 = Jar()
    assert jar3.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(20)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(12)
    assert jar.size == 15

def test_withdraw():
    jar = Jar(100)
    jar.deposit(50)
    jar.withdraw(25)
    assert jar.size == 25
    jar.withdraw(15)
    assert jar.size == 10