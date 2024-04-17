my_list=list(map(int,input().split()))
b=input()
c=list(b)
for j in range(my_list[1]):
    f=0
    for i in range(my_list[0]-1):
        if f<my_list[0]-1:
            if c[f]=="B" and c[f+1]=="G" :
                x=c.pop(f)
                c.insert(f+1,x)
                f+=2
            else:
                f+=1
                continue
s=""
for j in c:
    s+=j
print(s)
            