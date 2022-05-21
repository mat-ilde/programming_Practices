"""
Input = Array of integers that represent the height of apartments. Left most apartment is in index 0
& the array lists the apartments from left to right. After the rightmost apartment, we hit the ocean.
Apartments are of the same width and in a straight line from left to right towards the ocean.
Output = Take in the Array and return the indexes of the apartments that have ocean view
You can paste this into CoderPad to illustrate:
// Ocean View
//Input: [4, 3, 2, 3, 1]
//Output: [0, 3, 4]
//
//   _
// 4 |  |  _         _
// 3 |  |  |  |  _   |  |
// 2 |  |  |  |  |  |  |  |  _
// 1 |  |  |  |  |  |  |  |  |  |
//                               ~~~ Ocean
//   b0,    b1,   b2,   b3,   b4
"""
#return how many apartments with ocean view there is in the building
def oceanView(apartments):
    apartments_with_views = []
    for apartment_id, apartment_height in enumerate(apartments):
        taller = False
        for right_apartment_height in apartments[apartment_id+1:]:
            if(right_apartment_height>=apartment_height):
                taller = True
        if not taller:
            apartments_with_views.append(apartment_id)
    print(apartments_with_views)
    return apartments_with_views
if __name__ == '__main__':
    ar=[40, 60, 20, 30, 10,10]
    oceanView(ar)