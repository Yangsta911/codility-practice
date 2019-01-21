def solution(A, K):
    a = len (A)
    B = A
    for value in A:
        if len(A) == a:
            C = B[a-K:a-K+1]
            a -= 1
        elif  a > 0:
            B[a+K-1:a +K] = A[a-K:a-K+1]
            B[a-1:a] = [0]
            a -= 1
        if a == 0:
            B[a+K-1:a+K] = C
    print B




A = [1, 2, 3, 4, 5]
K = 2
solution(A,K)
