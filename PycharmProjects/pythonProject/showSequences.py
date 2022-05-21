def count(array,num):
    #returns how many times sequence is in array
    count=0
    for element in array:
        if element== num:
            count=count+1
    return count

#return list with element anh how many time is in the list
def showSequences(array):
    num_count = dict()
    for num in array:
        #la primera aparición del elemento en array, solo entra la primera vez que lo ve
        if num not in num_count:
            num_count[num]=0
        num_count[num]=num_count[num]+1
    new_list = list(num_count.items())
    new_list.sort()
    print(new_list)

    return new_list
if __name__ == '__main__':
    array=[20,15,20,10,15,25,10]
    showSequences(array)


