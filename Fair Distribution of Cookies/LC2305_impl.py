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

print(distributeCookies([1,2,3,4,5], 1)) # 15
print(distributeCookies([10,20,30,40], 4)) # 40
print(distributeCookies([1,1,1,1,100], 2)) # 100
print(distributeCookies([5,5,5,5,5,5], 3)) # 10
print(distributeCookies([1,1,1,1,1,1,1,1,1,1], 5)) # 2
print(distributeCookies([1000,2000,3000,4000,5000], 2)) # 8000
print(distributeCookies([1,2,3,4,5,6,7,8,9,10], 3)) # 19
print(distributeCookies([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 4)) # 30 very slow
