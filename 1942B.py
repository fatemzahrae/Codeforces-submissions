# my attempt >> not correct
def MEX(P):
    for i in range(max(P)+1):
        if i not in P :
            return i
    return max(P)+1


def CONSTRUCT_P(a):
    P = []
    n = len(a)
    for i in range(n) :
        j=-n
        while len(P) < n :
            if j not in P :
                if ( MEX( P + [j] ) - j ) == a[i] :
                    P.append(j)
                else :
                    j+=1
            else:
                j += 1


    return P

def function():
    testNumber = int(input())
    for t in range(testNumber) :
        n = int(input())
        a = list(map(int,input().split()))
        P = CONSTRUCT_P(a)
        print(P)
        
if __name__ == "__main__" :
    function()