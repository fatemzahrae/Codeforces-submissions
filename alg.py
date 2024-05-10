def function(n, k):
    count = 0
    for i in range(1, 10**9 + 1):
        if i % n != 0:
            count += 1
            if count == k:
                return i

if __name__ == "__main__":
    for t in range(int(input())):
        l = list(map(int, input().split()))
        print(function(l[0], l[1]))
