def function():
    for t in range(int(input())) :
        n = int(input())
        a = list(map(int, input().split()))
        s = set(a)
        print(n-len(s))
    
if __name__ == "__main__" :
    function()

