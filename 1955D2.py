def isGood(N, M, k):
    n, m = len(N), len(M)
    count_list = 0
    dic_ref = {}
    
    for element in M:
        dic_ref[element] = dic_ref.get(element, 0) + 1

    dic = {}
    for element in N[:m]:
        dic[element] = dic.get(element, 0) + 1

    count_k = 0
    for j in dic:
        if j in dic_ref:
            count_k += min(dic[j], dic_ref[j])
    
    if count_k >= k:
        count_list += 1

    for i in range(1, n - m + 1):
        dic[N[i - 1]] -= 1
        if dic[N[i - 1]] == 0:
            del dic[N[i - 1]]

        if i + m - 1 < n:
            dic[N[i + m - 1]] = dic.get(N[i + m - 1], 0) + 1

        count_k = 0
        for j in dic:
            if j in dic_ref:
                count_k += min(dic[j], dic_ref[j])
        
        if count_k >= k:
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
