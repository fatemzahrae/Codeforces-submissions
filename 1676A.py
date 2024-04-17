def isLucky(ticketNumber):
     if len(ticketNumber) != 6:
          return "NO"
     else:
        rightSum = int(ticketNumber[0]) +  int(ticketNumber[1]) + int(ticketNumber[2])                 
        leftSum = int(ticketNumber[3]) +  int(ticketNumber[4]) + int(ticketNumber[5])  
        if rightSum == leftSum:
             return "YES"
        else:
             return "NO"



def function():
    testNumber = int(input())
    L=[]
    for i in range(testNumber):
        ticketNumber = str(input())
        res = isLucky(ticketNumber)
        L.append(res)
    for i in range(testNumber):
         print(L[i])


if __name__ == "__main__" :
        function()