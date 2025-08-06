def distributeCookies(cookies, k):
    n = len(cookies)
    children = [0] * k
    min_unfairness = float('inf')
    
    def backtrack(i):
        nonlocal min_unfairness
        
        if max(children) >= min_unfairness:
            return
        
        if i == n:
            min_unfairness = max(children)
            return
        
        for j in range(k):
            children[j] += cookies[i]
            backtrack(i + 1)
            children[j] -= cookies[i]
    
    backtrack(0)
    return min_unfairness

print(distributeCookies([8,15,10,20,8], 2)) # 31
print(distributeCookies([6,1,3,2,2,4,1,2], 3)) # 7
print(distributeCookies([1,2,3,4,5,6,7,8,9,10], 5)) # 11

