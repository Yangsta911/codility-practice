def Permcheck(A):
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

def solution (X,A):
    timepassed = -1
    nosolution = -1
    leavesfallen = set()
    for item in A:
        leavesfallen.add(item)
        listleavesfallen = list(leavesfallen)
        listleavesfallen.sort()
        timepassed = timepassed + 1
        if X in listleavesfallen:
            if Permcheck(listleavesfallen) == 1:
                return timepassed
            elif timepassed == len(A) - 1:
                return nosolution
        elif timepassed == len(A) - 1:
            return nosolution


X = 3
A = [1, 3, 1, 3, 2, 1, 3]
answer = solution(X,A)
print answer


