def maxPairwiseProduct(A):
    m1 = A[0]
    m2 = A[1]
    if m2 > m1:
        m1, m2 = m2, m1

    for i in range(2, len(A)):
        if A[i] > m1:
            m2 = m1
            m1 = A[i]
        else:
            if A[i] > m2:
                m2 = A[i]
    return m1 * m2