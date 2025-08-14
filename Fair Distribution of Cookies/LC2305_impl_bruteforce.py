# GROUP 6
# Members: George Lin, Andrew Li, Xiaoti Hu, Mingda Xie
# Group Project 3 : Fair Distribution of Cookies Solution - Brute force


def distributeCookies(cookies, k):
    # Track current cookie count for each child
    cur = [0] * k

    def dfs(i):
        # Base case: all cookies have been distributed
        if i == len(cookies):
            return max(cur)

        # Try giving the current cookie bag to each child
        answer = float("inf")
        for j in range(k):
            # Give cookie bag i to child j
            cur[j] += cookies[i]
            # Recursively distribute remaining cookies
            answer = min(answer, dfs(i + 1))
            # Backtrack: take cookie bag i back from child j
            cur[j] -= cookies[i]

        return answer

    # Start DFS from the first cookie bag
    return dfs(0)


if __name__ == "__main__":
    # sample test cases :

    print(distributeCookies([8, 15, 10, 20, 8], 2))  # 31
    print(distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))  # 7

    print(distributeCookies([1, 2, 3, 4, 5], 1))  # 15
    print(distributeCookies([10, 20, 30, 40], 4))  # 40
    print(distributeCookies([1, 1, 1, 1, 100], 2))  # 100
    print(distributeCookies([5, 5, 5, 5, 5, 5], 3))  # 10
    print(distributeCookies([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5))  # 2
    print(distributeCookies([1000, 2000, 3000, 4000, 5000], 2))  # 8000
    print(distributeCookies([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # 19
    print(
        distributeCookies([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4)
    )  # 30 will take long time
