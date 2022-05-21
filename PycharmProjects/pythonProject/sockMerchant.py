
# return how many pair of socks the same color there is in the array
def sockMerchant(n, ar):
    count = 0
    my_dict = dict()
    for sock in ar:
        if sock in my_dict:
            print("dentro:",sock)
            my_dict[sock] = my_dict[sock] + 1
            if my_dict[sock]%2==0:
                count=count+1
        else:
            my_dict[sock] = 1
            print("fuera:", sock)
    print(count)
    return count

if __name__ == '__main__':
    sockMerchant(10,(10,20,10,20,20,20,30,30))
