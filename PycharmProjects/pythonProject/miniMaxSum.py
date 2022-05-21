def miniMaxSum(arr):
    maximum=0
    minimum=arr[0]
    minimum_sum=0
    maximum_sum=0

    for element in arr:
        if element<minimum:
            minimum=element
        if element>maximum:
            maximum=element
        minimum_sum = minimum_sum + element
        maximum_sum = maximum_sum +element
    maximum_sum=maximum_sum-maximum
    minimum_sum=minimum_sum-minimum
    print(maximum_sum,minimum_sum)

    return minimum_sum,maximum_sum
if __name__ == '__main__':
    arr=[ 1, 2, 3, 4, 5,]
    miniMaxSum(arr)