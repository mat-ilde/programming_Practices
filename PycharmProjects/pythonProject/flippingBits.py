import re
def swaping0and1(binary_list):
    n_list=list()
    for zeros_and_ones in binary_list:
        zeros_and_ones = int(zeros_and_ones) - 1
        if zeros_and_ones==-1:
            zeros_and_ones=1
        else:
            zeros_and_ones = 0
        n_list.append(zeros_and_ones)
        not_assigned=zeros_and_ones+2 ** 32
    for n in n_list:
        print(n+2 ** 32)
    return not_assigned

def flippingBits(n):
    binary_list = list()
    for long_number in n:
        binary = '{:032b}'.format(long_number)
        binary_list.append(binary)
    print( '{:032b}'.format(2147483647))


    return swaping0and1(binary_list[0]), swaping0and1(binary_list[1]), swaping0and1(binary_list[2]), swaping0and1(binary_list[3])


if __name__ == '__main__':
    n = [3, 2147483647, 1, 0]
    print(flippingBits(n))


    #flippingBits(n)
