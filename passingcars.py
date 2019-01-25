def solution (A):
    zeros = 0
    pairs = 0
    for item in A:
        if item == 0:
            zeros = zeros +1
        else:
            pairs = pairs + zeros
    if pairs > 1000000000:
        pairs = -1
    return pairs



A = [0,1,0,1,1]
answer = solution(A)
print answer