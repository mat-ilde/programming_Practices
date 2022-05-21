import sys

new_list = list()
my_dict = dict()

def deltaCompression(arr):
    for i, first_sequence in enumerate(arr[1:]):
        swap = arr[i]
        arr[i] = swap
        for j, second_sequence in enumerate(arr[1:]):
            if first_sequence not in my_dict:
                my_dict[first_sequence] = first_sequence
        num = first_sequence - arr[i]
        new_list.append(num)

    new_list.insert(0,arr[0])
    print(new_list)
    return new_list


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9 ,9 ,9 ,9, 8, 7, 6, 5]
    "5 1 1 1 1 0 0 0 -1 -1 -1 -1"
    deltaCompression(arr)
