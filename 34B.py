def sumOfMoney(a, m):
    sum = 0
    count = m
    for i in range(len(a)) :
        if count > 0 :
            if a[i] < 0 :
                sum -= a[i]
                count -= 1
        else: 
            break
    return sum
        
def function():

    x = str(input())
    n = int((x.split())[0])
    m = int((x.split())[1])
    y = str(input()).split()
    a = []
    for i in y :
        a.append(int(i))
    a = sorted(a)
    print(sumOfMoney(a,m))

if __name__ == "__main__" :
    function()







