def lonelyinteger(a):
    lonely = 0
    my_dict = dict()
    for number in a:
        if number not in my_dict:
            my_dict[number] = 0
        my_dict[number] = my_dict[number] + 1
    for j,k in my_dict.items():
        if k==1:
            lonely=j
    print(lonely)




    return lonely

if __name__ == '__main__':
    a = [10, 20, 30, 40, 10, 20, 30, 40]
    lonelyinteger(a)
