import bisect

def countShops(a, money) :
    return bisect.bisect_right(a,money)

def function():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    for i in range(q) :
        money = int(input())
        print(countShops(a, money))

if __name__ == "__main__":
    function()

