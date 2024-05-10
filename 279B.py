def function(n,t,a) :
    m = 0

    for i in range(n) :
        counterReadBook = 0
        newArray = a[i:] 
        time = t
        for j in range(len(newArray)) :

            if newArray[j] <= time and counterReadBook < n :
                time -= newArray[j]
                counterReadBook += 1
                
            else :
                break 

        if counterReadBook == n :
            return (counterReadBook)
            
        else:
            m = max(m,counterReadBook)
            

    return (m)





if __name__ == "__main__" :
    L = list(map(int,input().split()))
    a = list(map(int,input().split()))

    print(function(L[0],L[1],a))