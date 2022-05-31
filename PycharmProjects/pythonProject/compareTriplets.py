"""
The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.
Given a and b, determine their respective comparison points.
"""

def compareTriplets(alice_challenge, bob_challenge):
    alice_count = 0
    bob_count = 0
                #using python function zip to compare 2 strings at the same time
    zip_object = zip(alice_challenge, bob_challenge)
    for alice, bob in zip_object:
        if alice>bob:
            alice_count=alice_count+1
        if bob>alice:
            bob_count=bob_count+1
    print(alice_count,bob_count)

    return alice_count, bob_count

if __name__ == '__main__':
    alice = [17, 28, 30]
    bob = [99, 16, 8]
    print(compareTriplets(alice,bob))