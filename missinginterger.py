def solution(A):
    A.sort()
    intset = set()
    for item in A:
        if item > 0:
            intset.add(item)
            intsetlist = list(intset)
    if 1 in intset:
        if len(intsetlist) == 1:
            missingitem = intsetlist[0] + 1
            return missingitem
        else:
            intsetlist.sort()
            previousitem = intsetlist[0]
            for item in intsetlist[1:]:
                if item != previousitem+1:
                    missingitem = previousitem + 1
                    return missingitem
                elif previousitem == len(intsetlist) - 1:
                    missingitem = intsetlist[len(intsetlist) - 1] + 1
                    return missingitem
                else:
                    previousitem = item
    else:
        missingitem = 1
        return missingitem

A = [-1, -3]
answer = solution(A)
print answer
