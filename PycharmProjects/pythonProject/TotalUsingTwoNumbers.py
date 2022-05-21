
def TotalUsingTwoNumbers(target, numbers):
    encontrado = False
    my_set=set()
    for number in numbers:
        y = target - number
        if y in my_set :#and number+y == target:
            encontrado = True
        my_set.add(number)

    return encontrado

if __name__ == '__main__':
    target= 10
    numbers=[3,2,1,5]
    print(TotalUsingTwoNumbers(target,numbers))