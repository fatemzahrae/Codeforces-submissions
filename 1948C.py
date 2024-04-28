def arrow_path(table, n):
    for i in range(1,n,2) :
        if (i+1 < n  and table[0][i] == table[1][i+1] == '<') or ( table[0][i] == table[1][i - 1] == '<'):
            print('NO')
            break
    else:
        print("YES")




def function() :
    for _ in range(int(input())) :
        n = int(input())
        table = [list(input().strip()) for _ in range(2)]
        arrow_path(table,n)


if __name__ == "__main__" :
    function()