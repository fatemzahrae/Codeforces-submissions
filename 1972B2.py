def coins_game(coins) :
    u = coins.count("U")
    if u % 2 == 0 :
        print("NO")
    else :
        print("YES")

if __name__ == "__main__" :
    for _ in range(int(input())) :
        n = int(input())
        coins = str(input())
        coins_game(coins) 
    