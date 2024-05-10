def function(n, t, a):
    max_books = 0
    current_books = 0
    current_time = 0
    left = 0
    
    for right in range(n):
        current_time += a[right]
        current_books += 1
        
        while current_time > t:
            current_time -= a[left]
            current_books -= 1
            left += 1
            
        max_books = max(max_books, current_books)
        
    return max_books

if __name__ == "__main__":
    L = list(map(int, input().split()))
    a = list(map(int, input().split()))

    print(function(L[0], L[1], a))