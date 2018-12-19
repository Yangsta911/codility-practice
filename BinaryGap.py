def solution(N):
    binary = format(N, "b")
    print (binary)
    x = 0
    y = 0
    int_binary = int(binary)
    for value in binary:
        if value == '0':
            x +=1
        if value == '1':
            if x > y:
                y = x
            x = 0
        #print x
    print('the y is: {}'.format(y))

solution(1041)