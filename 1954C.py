def max_prod(x,y):
    X = []
    Y = []

    stat = True
    for i in range(len(x)) :
        if stat :
            if x[i] == y[i] :
                X.append(str((int(x[i]),int(y[i]))))
                Y.append(str((int(x[i]),int(y[i]))))
            else :
                X.append(str(max(int(x[i]),int(y[i]))))
                Y.append(str(min(int(x[i]),int(y[i]))))
                stat = False
        else :
            Y.append(str(max(int(x[i]),int(y[i]))))
            X.append(str(min(int(x[i]),int(y[i]))))

    print("".join(X))
    print("".join(Y))

if __name__ == "__main__":
    for _ in range(int(input())) :
        x = str(input())
        y = str(input())
        max_prod(x,y)
