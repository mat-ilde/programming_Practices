
def reverseList(arr):

    size=len(arr)
    for i, element in enumerate(arr):
        if i==(size//2):
           break
        swap=arr[i]
        arr[i]= arr[(size - 1) - i]
        arr[(size - 1) - i]=swap

    #print(arr)
    return arr

def reverseList_2(arr):
    size=len(arr)
    #ve desde 0 a la mitad del array
    for i in range(len(arr)//2):
        swap=arr[i]
        arr[i]= arr[(size - 1) - i]
        arr[(size - 1) - i]=swap
    print(arr)
    return arr

if __name__ == '__main__':
    arr=[ 10, 20, 30, 40 ,50 ]
    reverseList_2(arr)