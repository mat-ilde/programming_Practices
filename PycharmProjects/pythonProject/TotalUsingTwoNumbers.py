"""
    Function with a target and a list return true or false if the sum of 2 numbers in the list is equal to target
"""
def TotalUsingTwoNumbers(target, numbers):
    encontrado = False
    my_set=set()
    for number in numbers:
        y = target - number
        if y in my_set:
            encontrado = True
        my_set.add(number)

    return encontrado

if __name__ == '__main__':
    target= 10
    numbers=[3,2,1,5]
    print(TotalUsingTwoNumbers(target,numbers))