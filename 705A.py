def hulk(n):
    count = 2
    x = " I hate that"
    y = " I love that"

    res = x[1: ]
    
    while count <= n :
        if count % 2 == 0 :
            res += y 
            
        else :
            res += x 
        count+=1

    return res[ :-4]+ "it"

if __name__ == "__main__" :
    n = int(input())
    print(hulk(n))