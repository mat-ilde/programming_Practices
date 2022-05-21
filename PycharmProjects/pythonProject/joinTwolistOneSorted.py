def joinTwolistOneSorted(arr,arr2):
    new_sorted_list=list()
    for i, element_in_first_list in enumerate(arr):
        for j,element_in_second_list in enumerate(arr2):
            if element_in_second_list<element_in_first_list:
                swap=arr[i]
                arr[i]=arr2[j]
                arr2[j]=swap
            new_sorted_list.append(arr[i])

    print(new_sorted_list)

    return new_sorted_list

if __name__ == '__main__':
    arr=[ 10, 20, 30, 40 ,50 ]
    arr3 = [10, 20, 30, 40, 50,70, 80, 90, 100]
    arr2 = [70, 60, 50, 40]
    joinTwolistOneSorted(arr,arr2)