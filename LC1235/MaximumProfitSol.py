# GROUP 6
# Members: George Lin, Andrew Li, Xiaoti Hu, Mingda Xie
# Group Project 3 : Maximum Profit in Job Scheduling Solutions

# import libraries
from typing import List
import random
import time


class Solution:
    def jobSchedulingDP(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """
        Dynamic Programming solution for the job scheduling problem.

        Problem: Given n jobs with start times, end times, and profits,
        find the maximum profit by scheduling non-overlapping jobs.
        """
        n = len(startTime)
        # Create index array to maintain original job order while sorting
        index = list(range(n))
        # Sort indices by start time to process jobs in chronological order
        index.sort(key=lambda i: startTime[i])

        # Memoization cache to store computed results
        cache = [-1] * n

        def dfs(i):
            """
            Recursive function with memoization to find maximum profit.

            Args:
                i: Current job index in the sorted order

            Returns:
                Maximum profit achievable starting from job i
            """
            # Base case: no more jobs to consider
            if i == n:
                return 0
            # Return cached result if already computed
            if cache[i] != -1:
                return cache[i]

            # Choice 1: Skip current job, take profit from remaining jobs
            res = dfs(i + 1)

            # Choice 2: Take current job and find next compatible job
            # Use binary search to find the first job that starts after current job ends
            left, right, j = i + 1, n, n
            while left < right:
                mid = (left + right) // 2
                if startTime[index[mid]] >= endTime[index[i]]:
                    # Found a compatible job, but keep searching for the first one
                    j = mid
                    right = mid
                else:
                    # Current mid job overlaps, search in right half
                    left = mid + 1

            # Take maximum of skipping vs taking current job
            cache[i] = res = max(res, profit[index[i]] + dfs(j))
            return res

        return dfs(0)

    def jobSchedulingHeuristic(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """
        Greedy heuristic solution for the job scheduling problem.
        1. Sorts jobs by end time (earliest finish first)
        2. Takes jobs greedily if they don't overlap with previously selected jobs
        """
        # Combine job data into tuples for easier processing
        jobs = list(zip(startTime, endTime, profit))
        # Sort by end time (earliest finish first) - greedy choice
        jobs.sort(key=lambda x: x[1])

        total_profit = 0
        last_end = 0  # Track the end time of the last selected job

        # Iterate through jobs in order of increasing end time
        for s, e, p in jobs:
            # If current job starts after the last selected job ends, we can take it
            if s >= last_end:
                total_profit += p
                last_end = e

        return total_profit


def test_random_cases(num_cases=10, num_jobs=30, time_range=50):
    """
    Test function to compare the optimal DP solution with the greedy heuristic.

    Generates random test cases and compares the results of both algorithms
    to see how often the greedy heuristic produces optimal results.

    Args:
        num_cases: Number of test cases to generate
        num_jobs: Number of jobs per test case
        time_range: Maximum time value for start/end times
    """
    # initialize solution class
    solver = Solution()

    for case in range(num_cases):
        # Initialize arrays for this test case
        start = []
        end = []
        profit = []

        # Generate random job data
        for _ in range(num_jobs):
            # Random start time (1 to time_range-1)
            s = random.randint(1, time_range - 1)
            # Random end time (after start time, up to time_range)
            e = random.randint(s + 1, time_range)
            # Random profit (1 to 100)
            p = random.randint(1, 100)
            start.append(s)
            end.append(e)
            profit.append(p)

        # Time DP
        start_time = time.perf_counter()
        res_opt = solver.jobSchedulingDP(start, end, profit)
        dp_time = time.perf_counter() - start_time

        # Time Heuristic
        start_time = time.perf_counter()
        res_heur = solver.jobSchedulingHeuristic(start, end, profit)
        heur_time = time.perf_counter() - start_time

        match = res_opt == res_heur

        # print for quick visualization of results
        print(
            f"Case {case+1}: Match={match}, Optimal={res_opt}, Heuristic={res_heur}, "
            f"Difference={res_opt - res_heur}, DP time={dp_time:.6f}s, Heur time={heur_time:.6f}s"
        )


def main():
    test_random_cases(num_cases=10, num_jobs=10, time_range=10)


if __name__ == "__main__":
    main()
