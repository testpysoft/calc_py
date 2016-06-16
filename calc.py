print('Please input a')
number_a = int(input())
print('Please input b')
number_b = int(input())
print('Please input operand in  (add,muliply,divide,subtract)')
oper=input()

def add():
    print(number_a+number_b)

def multy():
    print(number_a*number_b)

def divide():
    if (number_b== 0):
        print('division by zero')
        return
    print(number_a/number_b)
def multiply():
    print(number_a*number_b)
def subtract():
    print (number_a-number_b)


actions = {'add': add, 'multiply': multiply,'divide':divide,'subtract': subtract}

actions[oper]()

