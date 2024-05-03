def permutation(n):
    arr=[0 for i in range(n)]
    j=1
    x=False
    y=False
    for i in range(n):
        
        if (i+1)%2!=0:
            arr[i]=j
            x=True
            
        else:
             arr[i]=n-j+1
             y=True
        
        if x and y:
             x=False
             y=False
             j+=1
          
        
        
    
    print(*arr)
    

if __name__ == "__main__" :
    for _ in range(int(input())) :
        permutation(int(input()))

        

