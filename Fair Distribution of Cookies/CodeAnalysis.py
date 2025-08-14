import random
import time
import matplotlib.pyplot as plt

# Import functions without triggering their __main__ blocks
from LC2305_impl_SA import distributeCookies as distributeCookiesSA
from LC2305_impl_bruteforce import distributeCookies as distributeCookiesBF

def run_timing_analysis():
    # small sizes for brute force (DFS)
    small_sizes = list(range(2, 12))
    # larger sizes for SA
    large_sizes = list(range(12, 21))
    k = 3

    bf_times = []
    sa_times_small = []
    sa_times_large = []

    # Timing Brute Force (DFS)
    for n in small_sizes:
        cookies = [random.randint(1, 20) for _ in range(n)]
        start = time.time()
        distributeCookiesBF(cookies, k)
        bf_times.append(time.time() - start)

        start = time.time()
        distributeCookiesSA(cookies, k)
        sa_times_small.append(time.time() - start)

    # Timing SA on larger sizes
    for n in large_sizes:
        cookies = [random.randint(1, 20) for _ in range(n)]
        start = time.time()
        distributeCookiesSA(cookies, k)
        sa_times_large.append(time.time() - start)

    # Plot results
    plt.figure(figsize=(10,6))
    plt.plot(small_sizes, bf_times, marker='s', label='Brute Force DFS (small n)')
    plt.plot(small_sizes, sa_times_small, marker='o', label='SA (small n)')
    plt.plot(large_sizes, sa_times_large, marker='o', linestyle='--', label='SA (large n)')
    
    plt.xlabel("Number of Cookie Bags (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison: SA vs Brute Force DFS")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_timing_analysis()
