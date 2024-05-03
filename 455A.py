def score_calcul(array,n) :

    count = [0]*(10**5+1)
    l = [0]*(10**5+1)

    for i in array :
        count[i] += 1

    l[1] = count[1]
    for i in range(2,(10**5+1)):
        l[i] = max(l[i-1], l[i-2]+i*count[i])

    print(max(l))



if __name__ == "__main__" :
    n = int(input())
    array = list(map(int, input().split()))
    score_calcul(array,n)