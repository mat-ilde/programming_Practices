

"""
    This problem received a list I need to substract the next value to the before value and return a list with all substract values
"""

import sys

new_list = list()
my_dict = dict()

def deltaCompression(arr):
    #iterating towards the list starting in the position 1
    for i, first_sequence in enumerate(arr[1:]):
        #saving the value to avoid being change during the iteration
        swap = arr[i]
        arr[i] = swap
        # iterating towards the value that will being changing
        for j, second_sequence in enumerate(arr[1:]):
            #checking if is not in the dictionary if not add the value to the key
            if first_sequence not in my_dict:
                my_dict[first_sequence] = first_sequence
         # if is my dictionary do the substraction
        num = first_sequence - arr[i]
        #adding the substraction to my empty list
        new_list.append(num)
    #the first postion to my new list is for the first element in my original list.
    new_list.insert(0,arr[0])
    print(new_list)
    return new_list


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9 ,9 ,9 ,9, 8, 7, 6, 5]
    deltaCompression(arr)
