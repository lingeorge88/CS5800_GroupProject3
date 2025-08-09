import random
import time
import matplotlib.pyplot as plt
from LC2305_impl_SA import distributeCookies as distributeCookiesSA
from LC2305_impl_bruteforce import distributeCookies as distributeCookiesBF

def run_timing_analysis():
    sizes = list(range(2, 15))
    k = 3
    sa_times = []
    bf_times = []
    
    for n in sizes:
        cookies = [random.randint(1, 20) for _ in range(n)]
        
        start = time.time()
        distributeCookiesSA(cookies, k)
        sa_times.append(time.time() - start)
        
        start = time.time()
        distributeCookiesBF(cookies, k)
        bf_times.append(time.time() - start)
    
    plt.figure(figsize=(8,6))
    plt.plot(sizes, sa_times, marker='o', label="Simulated Annealing (Heuristic)")
    plt.plot(sizes, bf_times, marker='s', label="Brute Force DFS")
    plt.xlabel("Number of Cookie Bags (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison: SA vs Brute Force")
    plt.legend()
    plt.grid(True)
    plt.show()

run_timing_analysis()
