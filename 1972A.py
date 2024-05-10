def function(n,a,b):
    count = 0

    for i in range(n):

        while a[i]>b[i]:

            w = b[count]
            count += 1
            a.append(w)
            a = sorted(a)
            a.pop(-1)
    
    print(count)

if __name__ == "__main__" :
    for _ in range(int(input())) :
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        function(n,a,b)

