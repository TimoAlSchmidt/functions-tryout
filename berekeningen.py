import random

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2
    
def multiplication(number1, number2):
    return number1 * number2
    
def division(number1, number2): 
    return number1 / number2
    
def increment(number):
    return number + 1
    
def decrement(number):
    return number - 1
    
random.seed()

for i in range(3):
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    print(number1,"+",number2,"=",addition(number1,number2))
    
for i in range(3):
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    print(number1,"-",number2,"=",subtraction(number1,number2))
    
for i in range(3):
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    print(number1,"*",number2,"=",multiplication(number1,number2))
    
for i in range(3):
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    print(number1,"/",number2,"=",division(number1,number2))
    
for i in range(3):
    number1 = random.randint(0,100)
    print(number1,"+ 1 =",increment(number1))
    
for i in range(3):
    number1 = random.randint(0,100)
    print(number1,"- 1 =",decrement(number1))