#C
#n桁
n = int(input())
s = [list(input()) for i in range(5)]
for i in range(n):
    s1 = s[0][i*4+1:(i+1)*4]
    s2 = s[1][i*4+1:(i+1)*4]
    s3 = s[2][i*4+1:(i+1)*4]
    s4 = s[3][i*4+1:(i+1)*4]
    s5 = s[4][i*4+1:(i+1)*4]
    # print(i*n, (i+1)*4-1, s1, s2, s3, s4, s5, sep='\n')
    if s1 == ['#', '#', '#'] and\
        s2 == ['#', '.', '#'] and\
        s3 == ['#', '.', '#'] and\
        s4 == ['#', '.', '#'] and\
        s5 == ['#', '#', '#']:
        print("0", end='')
    elif s1 ==['.', '#', '.']and\
        s2 ==['#', '#', '.']and\
        s3 ==['.', '#', '.']and\
        s4 ==['.', '#', '.']and\
        s5 == ['#', '#', '#']:
        print("1",end="")
    elif s1 ==['#', '#', '#']and\
        s2 ==['.', '.', '#']and\
        s3 ==['#', '#', '#']and\
        s4 ==['#', '.', '.']and\
        s5 == ['#', '#', '#']:
        print("2", end="")
    elif s1 ==['#', '#', '#']and\
        s2 ==['.', '.', '#']and\
        s3 ==['#', '#', '#']and\
        s4 ==['.', '.', '#']and\
        s5 == ['#', '#', '#']:
        print(3, end="")
    elif s1==['#', '.', '#']and\
        s2 ==['#', '.', '#']and\
        s3 ==['#', '#', '#']and\
        s4 ==['.', '.', '#']and\
        s5 == ['.', '.', '#']:
        print("4", end="")
    elif s1==['#', '#', '#']and\
        s2 ==['#', '.', '.']and\
        s3 ==['#', '#', '#']and\
        s4 ==['.', '.', '#']and\
        s5 == ['#', '#', '#']:
        print("5",end="")
    elif s1==['#', '#', '#']and\
        s2 ==['#', '.', '.']and\
        s3 ==['#', '#', '#']and\
        s4 ==['#', '.', '#']and\
        s5 ==['#', '#', '#']:
        print("6", end="")
    elif s1==['#', '#', '#']and\
        s2 ==['.', '.', '#']and\
        s3 ==['.', '.', '#']and\
        s4 ==['.', '.', '#']and\
        s5 == [ '.', '.', '#']:
        print("7",end="")
    elif s1==['#', '#', '#']and\
        s2 ==['#', '.', '#']and\
        s3 ==['#', '#', '#']and\
        s4 ==['#', '.', '#']and\
        s5 == ['#', '#', '#']:
        print("8",end='')
    elif s1==['#', '#', '#']and\
        s2 ==[ '#', '.', '#']and\
        s3 ==[ '#', '#', '#']and\
        s4 ==[ '.', '.', '#']and\
        s5 == ['#', '#', '#']:
        print("9", end="")

