def listSort(arr):
    for i, element_position in enumerate(arr):
        for j, element in enumerate(arr):
            if element<element_position:
                swap= arr[i]
                arr[i]=arr[j]
                arr[j]=swap
    print(arr)
    return arr
if __name__ == '__main__':
    arr=[ 9,5,7,3,4,3,1]
    listSort(arr)