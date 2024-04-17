def QueueAt(t, s) :
    k = 0
    
    while k < t :
        res= ""
        change = False
        for i in range(len(s)-1):
            if not change :
                if s[i]=="B" and s[i+1]=="G" :
                    res += s[i+1] + s[i] 
                    change = True
                else:
                    res += s[i]
            else:
                change = False
        
        if len(res) != len(s) :
            res += s[-1]
        k += 1
        s=res


    return res




def function():
    x = str(input())
    L = x.split()
    s = str(input())
    print(QueueAt(int(L[1]) ,s))


if __name__ == "__main__" :
    function()


    
