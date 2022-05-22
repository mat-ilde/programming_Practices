"""
    Function to revert the orden of a list using while loop
"""

def reverseList(arr):
    size=len(arr)
    i=0
    while i!=size//2:
        swap = arr[i]
                # iterating the end to the list until the middle of the list
        arr[i] = arr[(size - 1) - i]
        arr[(size - 1) - i] = swap
        i+=1

    return arr

if __name__ == '__main__':
    arr=[ 10, 20, 30, 40 ,50,60,70,80 ]
    print(reverseList(arr))