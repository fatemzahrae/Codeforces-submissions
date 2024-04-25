def balanceArray(n) :
    if (n/2) % 2 != 0 :
        print("NO")
    else :
        L = []
        for i in range(0,n//2):
            L.append(2*(1+i))
            
        k = 0
        for j in range(n//2,n-1) :
            L.append(2*k + 1)
            k += 1

        L.append(sum(L[ :n//2])- sum(L[n//2: ]))
        print("YES")
        print(" ".join(map(str, L)))

def function() :
    for _ in range(int(input())):
        n = int(input())
        balanceArray(n)
    
if __name__ == "__main__" :
    function()