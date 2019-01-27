def solution (S, P, Q):
    answer = []
    listS = list(S)
    for item1, item2 in zip(P, Q):
        value = 5
        for item in listS[item1 : item2+1]:
            if item == 'A':
                item = 1
            elif item == 'C':
                item = 2
            elif item == 'G':
                item = 3
            elif item == 'T':
                item = 4
            if item < value:
                value = item
        answer.append(value)
    return answer


S = 'TC'
P = [0, 0, 1]
Q = [0, 1, 1]
answer = solution(S,P,Q)
print answer