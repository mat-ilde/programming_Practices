"""
    Function with a list as input search for the value which is just one time and return it if not return 0
"""

def lonelyinteger(arr):
    lonely = 0
    my_dict = dict()
    for number in arr:
        if number not in my_dict:
            my_dict[number] = 0
        my_dict[number] = my_dict[number] + 1
    for j,k in my_dict.items():
        if k==1:
            lonely=j
    print(lonely)

    return lonely

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 5, 20, 30, 40]
    lonelyinteger(arr)
