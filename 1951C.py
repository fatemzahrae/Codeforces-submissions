def min_price():
    n, m, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()

    tickets = 0
    addition = 0
    min_price = 0

    for price in a :
        tickets = min(m,k)
        min_price += tickets * (price + addition)
        addition += tickets
        k -= tickets

    print(min_price)

if __name__ == "__main__" :
    for _ in range(int(input())):
        min_price()
