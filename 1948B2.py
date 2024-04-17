for _ in range(int(input())):
    
    n=int(input())
    my_map = map(int,input().split())
    my_list=list(my_map)
    print(my_list)

    res='NO'
    if(my_list==sorted(my_list)):
        res='YES'
    i=0
    while i<len(my_list):
        if(my_list[i]<10):i+=1;continue
        my_list=my_list[:i]+[my_list[i]//10,my_list[i]%10]+my_list[i+1:]
        i+=1
        if(my_list==sorted(my_list)):
            res='YES';break
    print(res)


