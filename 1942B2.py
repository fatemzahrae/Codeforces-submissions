#correct answer 

for i in range(int(input())):
  n,A=int(input()),list(map(int,input().split()))[::-1]
  for j in range(n):A[j],n=n-A[j],min(n,n-A[j])
  print(*A[::-1])