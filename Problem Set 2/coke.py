#moedas aceitas 50, 25, 10, 5.

#valor da coke: 50

total = 50

while total > 0:
    # Print the mount due
    print("Amount Due:", total)

    # Ask the user the value
    value = int(input("Insert Coin: "))

    if value in [25, 10, 5]:
        total -= value

change_owed = abs(total)

print("Change Owed:", change_owed)
