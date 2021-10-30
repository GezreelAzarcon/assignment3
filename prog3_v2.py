#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.
def entMoney():
    _money = int(input('How much money do you have? '))
    return _money
def entPrice():
    _price = int(input('How much is the apple? '))
    return _price
def maxNumF(moneyF, priceF):
    _maxNum = moneyF // priceF
    return _maxNum
def changeF(moneyF, priceF):
    _change = moneyF % priceF
    return _change
def display(maxNumF, changeF):
    print(f'You can buy {maxNumF} apples and your change is {changeF} pesos.')

money = entMoney()
price = entPrice()
maxNum = maxNumF(money, price)
change = changeF(money, price)
display(maxNum, change)