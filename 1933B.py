def minNumber(a):
    s = sum(a)
    if s % 3 == 0 :
        return 0
    elif s % 3 == 2 :
        return 1
    else :
        for i in a :
            if (s - i) % 3 == 0 :
                return 1
        return 2

def function() :
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(minNumber(a))


if __name__ == '__main__' :
    function()