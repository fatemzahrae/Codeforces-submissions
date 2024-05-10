def function(n,boys,m,girls) :
    if m >= n :
        count = 0
        while  len(boys) > 0 :
            b = boys.pop(0)
            n -= 1
            while  len(girls) > 0:
                g = girls[0]
                diff = (b-g)
                if  diff in [-1,0,1]:
                    count += 1
                    girls.pop(0)
                    break

                elif diff < -1 :
                    break
                elif diff > 1 :
                    girls.pop(0)

    else :
        count = 0
        while  len(girls) > 0 :
            g = girls.pop(0)
            m -= 1
            while  len(boys) > 0:
                b = boys[0]
                diff = (g-b)
                if  diff in [-1,0,1]:
                    count += 1
                    boys.pop(0)
                    break

                elif diff < -1 :
                    break
                elif diff > 1 :
                    boys.pop(0)
                    

    print(count)


if __name__ == "__main__" :

    n = int(input())
    boysList = sorted(list(map(int,input().split())))

    m = int(input())
    girlList = sorted(list(map(int,input().split())))

    function(n,boysList,m,girlList)