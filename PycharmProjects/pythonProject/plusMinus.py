def plusMinus(arr):
    positive_number = 0
    negative_number = 0
    zero_number = 0
    arr_size = len(arr)

    for number in arr:
        if number > 0:
            positive_number = positive_number + 1
        if number < 0:
            negative_number = negative_number + 1
        if number == 0:
            zero_number = zero_number + 1

    plus_minus_positive = format(positive_number / arr_size, '.6f')
    plus_minus_negative = format(negative_number / arr_size, '.6f')
    plus_minus_zero = format(zero_number / arr_size, '.6f')


    print(plus_minus_positive,plus_minus_negative,plus_minus_zero)
    return plus_minus_positive,plus_minus_negative,plus_minus_zero
if __name__ == '__main__':
    arr=( -2, -7 ,-8, -5,1)
    plusMinus(arr)