
def minDep(x,y):
    if x==y==0 :
        return 0
    elif ((x**2 + y**2)**0.5) == int((x**2 + y**2)**0.5) :
        return 1
    else: return 2



def prog():
    t=int(input())
    L=[]
    for i in range(t):
        exp = input()
        x_str, y_str = exp.split()
        x=int(x_str)
        y=int(y_str)
        L.append(minDep(x,y))
    for i in range(t):
        print(L[i])


if __name__ == "__main__" :
        prog()