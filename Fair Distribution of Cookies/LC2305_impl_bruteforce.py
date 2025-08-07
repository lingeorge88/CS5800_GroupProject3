def distributeCookies(cookies, k):
    cur = [0] * k
    
    def dfs(i):
        if i == len(cookies):
            return max(cur)
        
        answer = float('inf')
        for j in range(k):
            cur[j] += cookies[i]
            answer = min(answer, dfs(i + 1))
            cur[j] -= cookies[i]
        
        return answer
    
    return dfs(0)

print(distributeCookies([8,15,10,20,8], 2)) # 31
print(distributeCookies([6,1,3,2,2,4,1,2], 3)) # 7

print(distributeCookies([1,2,3,4,5], 1)) # 15
print(distributeCookies([10,20,30,40], 4)) # 40
print(distributeCookies([1,1,1,1,100], 2)) # 100
print(distributeCookies([5,5,5,5,5,5], 3)) # 10
print(distributeCookies([1,1,1,1,1,1,1,1,1,1], 5)) # 2
print(distributeCookies([1000,2000,3000,4000,5000], 2)) # 8000
print(distributeCookies([1,2,3,4,5,6,7,8,9,10], 3)) # 19
print(distributeCookies([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 4)) # 30 will take long time