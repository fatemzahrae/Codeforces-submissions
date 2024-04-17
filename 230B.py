import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def is_t_prime(num, is_prime):
    root = int(math.sqrt(num))
    if root * root == num and is_prime[root]:
        return True
    else:
        return False

def function():
    n = int(input())
    x = list(map(int, input().split()))

    is_prime = sieve(1000000)

    for num in x:
        if is_t_prime(num, is_prime):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    function()
