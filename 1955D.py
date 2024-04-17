def list_to_dict(lst):
    result_dict = {}
    for element in lst:
        result_dict[element] = result_dict.get(element, 0) + 1
    return result_dict


def isGood(N,M,k):
    n, m = len(N), len(M)
    count_list = 0
    dic = {}
    dic_ref = list_to_dict(M)
    
    for i in range(n-m+1):

        dic = list_to_dict( N[i:i+m] )
        count_k = 0

        for j in dic :
            if j in dic_ref :
                count_k += min(dic[j],dic_ref[j])
    
        if count_k >= k :
            count_list += 1

    return count_list

def function() :
    for t in range(int(input())):
        a = list(map(int, input().split()))
        N = list(map(int, input().split()))
        M = list(map(int, input().split()))
        print(isGood(N,M,a[2]))
    
if __name__ == "__main__":
    function()


