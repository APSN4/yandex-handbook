data = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

def maxPairwiseProduct(A):
    global count
    m1 = A[0]
    m2 = A[1]
    count += 1
    if m2 > m1:
        m1, m2 = m2, m1

    for i in range(2, len(A)):
        count += 1
        if A[i] > m1:
            m2 = m1
            m1 = A[i]
        else:
            count += 1
            if A[i] > m2:
                m2 = A[i]
    print(count)
    return m1 * m2

print(maxPairwiseProduct(data))