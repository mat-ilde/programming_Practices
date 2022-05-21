"""
   /**
 * Consider haystack to be sorted in ascending order.
 * e.g. [-7, -2, 1, 1, 5, 12, 12, 12, 26, 27, 29]
 */
public int find(int[] haystack, int needle) {
  // TODO Implement me!
  return 0;
}
   26  [-7, -2, 1, 1, 5, 12, 12, 12, 26, 27, 29]
   8
   26  [ 26]
   0
   26  [-7, -2, 1, 1, 5, 12, 12, 12, 25, 27, 29]
   -1

"""
from datetime import datetime

# slowly method
def find_slow(target,arr):
    for i,num in enumerate(arr):
        if num==target:
            return i

#binary search quicker method
def find(target, arr):
    i = 0
    j = len(arr)-1
    #le digo que itere siempre
    while True:
        #guardo la posición del centro del array
        mid = (i+j)//2
        #si el número en esa posición es igual al target
        if arr[mid]==target:
            return mid
        # si el número es menor que el target el inicio del array será el medio del array, cambio de posición i
        if arr[mid]<target:
            i = mid
        #si el número es mayor que el target el final del array será el medio del array, cambio de possición j
        if arr[mid]>target:
            j = mid
    return mid
if __name__ == '__main__':
    target = 26
    arr =  [-7, -2, 1, 1, 5, 12, 12, 12, 26, 27, 29]
    #using time to compare the time is spent to return the value.
    tic = datetime.now()
    print(find(target, arr))
    toc = datetime.now()
    #print the time spent
    #print(toc - tic)
