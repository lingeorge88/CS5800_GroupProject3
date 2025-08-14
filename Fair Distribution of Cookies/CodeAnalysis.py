# GROUP 6
# Members: George Lin, Andrew Li, Xiaoti Hu, Mingda Xie
# Group Project 3 : Fair Distribution of Cookies Analysis

# import libraries and modules
import random
import time
import matplotlib.pyplot as plt
from LC2305_impl_SA import distributeCookies as distributeCookiesSA
from LC2305_impl_bruteforce import distributeCookies as distributeCookiesBF


def run_timing_analysis():
    # Test problem sizes from 2 to 14 cookie bags
    sizes = list(range(2, 15))
    # Number of children to distribute cookies to
    k = 3
    # Lists to store execution times for each algorithm
    sa_times = []
    bf_times = []

    # Test each problem size
    for n in sizes:
        # Generate random cookie bag sizes (1-20 cookies per bag)
        cookies = [random.randint(1, 20) for _ in range(n)]

        # Time the Simulated Annealing algorithm
        start = time.time()
        distributeCookiesSA(cookies, k)
        sa_times.append(time.time() - start)

        # Time the Brute Force algorithm
        start = time.time()
        distributeCookiesBF(cookies, k)
        bf_times.append(time.time() - start)

    # Create performance comparison plot
    plt.figure(figsize=(8, 6))
    # Plot SA and brute force execution times
    plt.plot(sizes, sa_times, marker="o", label="Simulated Annealing (Heuristic)")
    plt.plot(sizes, bf_times, marker="s", label="Brute Force DFS")

    # chart and axis label
    plt.xlabel("Number of Cookie Bags (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison: SA vs Brute Force")
    plt.legend()
    plt.grid(True)
    plt.show()


run_timing_analysis()
