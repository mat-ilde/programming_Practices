"""
    Function with list as input and return the sum of the elements substracting the maximum element and the sum of the element
    substracting the minimum element
"""
def miniMaxSum(arr):
    maximum=0
    minimum=arr[0]
    minimum_sum=0
    maximum_sum=0

    for element in arr:
        #searching the minimum
        if element<minimum:
            minimum=element
            #searching the maximum
        if element>maximum:
            maximum=element
        #maximum and minimum sum
        minimum_sum = minimum_sum + element
        maximum_sum = maximum_sum +element
    #maximum sum substracting the maximum element
    maximum_sum=maximum_sum-maximum
    #mimimum sum substracting the minimum element
    minimum_sum=minimum_sum-minimum
    print(maximum_sum,minimum_sum)

    return minimum_sum,maximum_sum
if __name__ == '__main__':
    arr=[ 1, 2, 3, 4, 5,]
    miniMaxSum(arr)