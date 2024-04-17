def splitElement(a, index):
    element = str(a[index])
    element1 = element[0]
    element2 = element[1]
    a.pop(index)
    a.insert(index,int(element1))
    a.insert(index+1, int(element2))


def convertToArray(list):
    L_str = list.split()
    L_int = []
    for i in L_str:
        L_int.append(int(i))
    return L_int

def function():
    t = int(input())
    res = []
    for i in range(t):
        n = int(input())
        list = str(input())
        a = convertToArray(list)
    

        if a == sorted(a):
            res.append("yes")
        else:
            for i in range(len(a)):
                if a[i]>=10:
                    splitElement(a, i)
                    if a == sorted(a):
                        res.append("yes")
                        break
            if a != sorted(a):
                res.append("no")
    for i in res:
        print(i)
   
    



if __name__ == "__main__":
    function()





