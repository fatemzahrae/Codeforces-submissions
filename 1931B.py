

def makeEqual(a, n):
    count1 = 0
    number = sum(a) // n
    for i in a :
        if i > number :
            count1 += i - number
        else :
            if (i + count1) < number :
                return ("NO")
            else :
                count1 -= number - i

    if count1 == 0 :
        return ("YES")
    else :
        return ("NO")


def function() :
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(makeEqual(a,n))

            

if __name__ == "__main__" :
    function()