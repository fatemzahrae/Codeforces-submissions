def verify(s) :
    h = "hello"
    k = 0

    for i in range(len(s)):
        if k < len(h) :
            if s[i] == h[k]:
                k += 1
            else :
                continue

    if k == len(h):
        return "YES"
    else:
        return "NO"

def function():
    s = str(input())
    print(verify(s))

if __name__ == "__main__":
    function()
