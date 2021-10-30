#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

def getNumApple():
    print('Apple is 20 pesos')
    apple = int(input('How many apple do you want to buy? '))
    return apple

def getNumOrange():
    print('Orange is 25 pesos')
    orange = int(input('How many oranges do you want to buy? '))
    return orange

def getTotal(appleF, orangeF):
    totalApple = appleF * 20
    totalOrange = orangeF * 25
    total = totalApple + totalOrange
    return total

def display(totalF):
    print(f'The total amount is {totalF}')

numApple = getNumApple()
numOrange = getNumOrange()
total = getTotal(appleF=numApple, orangeF=numOrange)
display(total)

