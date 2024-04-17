def Palindrome(pal):
    return pal == pal[::-1]
    

def calcul_f(t):
    sum_of_lengths = 0
    lengths = set()
    for i in range(len(t)-1):
        for j in range(i+2, len(t)+1):
            substring = t[i:j]
            if not Palindrome(substring) :
                if len(substring) not in lengths:
                    sum_of_lengths += len(substring)
                    lengths.add(len(substring))
    return sum_of_lengths

          
def function():
    for i in range(int(input())):
        array = list(map(int, input().split()))
        s = str(input())
        res = 0
        for j in range(array[1]):
            limits = list(map(int, input().split()))
            subString = s[limits[0]-1:limits[1]]
            res = calcul_f(subString)
            print(res)


if __name__ == "__main__" :
    function()

