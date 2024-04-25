def changeFormat(time) :
    x = int(time[0])
    if x == 0 :
        res = "12:"+ time[1]+" AM"
        print( res)
    elif x >= 1 and x <= 11 :
        res = time[0] + ":"+ time[1]+ " AM"
        print(res)
    elif x == 12 :
        res = time[0]+  ":"+  time[1]+ " PM"
        print(res)
    elif x >= 13 and x <= 21 :
        y = int(time[0]) - 12 
        res = "0"+ str(y)+ ":"+ time[1]+ " PM"
        print(res)
    else :
        y = int(time[0]) - 12 
        res = str(y)+ ":"+ time[1]+ " PM"
        print(res)









def function() :
    for _ in range(int(input())):
        time = list(map(str, input().split(":")))
        changeFormat(time)

if __name__ == "__main__" :
    function()
