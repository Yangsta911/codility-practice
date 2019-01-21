def solution(A):
    perm = 1
    notperm = 0
    loopcount = 0
    A.sort()
    previousitem = 0
    if A[0] != 1:
        return notperm
    else:
        for item in A:
            if item == previousitem+1:
                previousitem = item
                loopcount = loopcount + 1
                if loopcount == len(A):
                    return  perm
            else:
                return notperm



A = [1]
answer = solution(A)
print answer