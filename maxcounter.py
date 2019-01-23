def solution (N,A):
    maxcounter =  [0] * N
    for item in A:
        if item <= N:
            maxcounter[item-1] = maxcounter[item-1] + 1
        if item == N+1:
            maxcounter.sort()
            maxcounter = [maxcounter[len(maxcounter)-1]] * N
    return maxcounter

N = 1
A = [1]
answer = solution(N,A)
print answer
