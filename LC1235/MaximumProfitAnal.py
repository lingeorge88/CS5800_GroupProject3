# GROUP 6
# Members: George Lin, Andrew Li, Xiaoti Hu, Mingda Xie
# Group Project 3 : Maximum Profit in Job Scheduling Analysis

# import necessary libraries
import sys
import random
import time
import statistics as stats
from typing import List
import matplotlib.pyplot as plt
import tracemalloc

# Import the Solution class from a separate file named MaximumProfitSol.py
from MaximumProfitSol import Solution

# The DP solution uses recursion. For large inputs, we need to increase the recursion limit.
sys.setrecursionlimit(12000)


def run_analysis(sizes, num_trials, density_multiplier, scenario_name):
    """
    Runs a comparative analysis for a specific job density scenario.
    """
    solver = Solution()
    results = []

    # print function for memory results ***
    print(f"\n--- Running Analysis for: {scenario_name} ---")
    print(
        f"{'Size':>10s} | {'DP Time (s)':>15s} | {'Heur Time (s)':>15s} | {'Accuracy (%)':>15s} | {'DP Mem (KiB)':>15s} | {'Heur Mem (KiB)':>15s}"
    )
    print("-" * 105)

    for size in sizes:
        # initialize lists to store runtime and memory usage results
        dp_times, heuristic_times, accuracies = [], [], []
        dp_memory_peaks, heuristic_memory_peaks = [], []

        time_range = size * density_multiplier

        for trial in range(num_trials):
            start_times, end_times, profits = [], [], []
            for _ in range(size):
                duration = random.randint(1, max(10, time_range // 20))
                s = random.randint(1, time_range - duration)
                e = s + duration
                p = random.randint(1, 100)
                start_times.append(s)
                end_times.append(e)
                profits.append(p)

            # --- Profile DP Solution ---
            tracemalloc.start()
            start_t = time.perf_counter()
            profit_dp = solver.jobSchedulingDP(start_times[:], end_times[:], profits[:])
            dp_times.append(time.perf_counter() - start_t)
            current, peak = tracemalloc.get_traced_memory()
            #  Appending memory data to its list
            dp_memory_peaks.append(peak / 1024)
            tracemalloc.stop()

            # --- Profile Heuristic Solution ---
            tracemalloc.start()
            start_t = time.perf_counter()
            profit_heuristic = solver.jobSchedulingHeuristic(
                start_times[:], end_times[:], profits[:]
            )
            heuristic_times.append(time.perf_counter() - start_t)
            current, peak = tracemalloc.get_traced_memory()
            #  Corrected variable name and appended memory data
            heuristic_memory_peaks.append(peak / 1024)
            tracemalloc.stop()

            # Calculate accuracy
            if profit_dp > 0:
                accuracies.append((profit_heuristic / profit_dp) * 100)
            elif profit_heuristic == 0:
                accuracies.append(100.0)

        # --- Average the results from all trials ---
        avg_dp_time = stats.mean(dp_times)
        avg_heuristic_time = stats.mean(heuristic_times)
        avg_accuracy = stats.mean(accuracies) if accuracies else 100.0
        # Calculate average memory usage
        avg_dp_mem = stats.mean(dp_memory_peaks)
        avg_heuristic_mem = stats.mean(heuristic_memory_peaks)

        #  Add memory results to the dictionary
        results.append(
            {
                "size": size,
                "avg_dp_time": avg_dp_time,
                "avg_heuristic_time": avg_heuristic_time,
                "avg_accuracy": avg_accuracy,
                "avg_dp_mem": avg_dp_mem,
                "avg_heuristic_mem": avg_heuristic_mem,
            }
        )

        # print statement to show memory results
        print(
            f"{size:>10d} | {avg_dp_time:>15.6f} | {avg_heuristic_time:>15.6f} | {avg_accuracy:>14.2f}% | {avg_dp_mem:>15.2f} | {avg_heuristic_mem:>15.2f}"
        )

    return results


def save_and_plot_results(all_results, sizes):
    """Saves results to a CSV file and generates four insightful plots."""
    if not all_results:
        print("No data to save or plot.")
        return

    # Use results from 'Normal Density' for time and memory plots
    normal_results = all_results.get("Normal Density", [])

    # --- Plot 1: Runtime Comparison (for Normal Density) ---
    plt.figure(figsize=(8, 6))
    if normal_results:
        sizes_plot = [r["size"] for r in normal_results]
        dp_times = [r["avg_dp_time"] for r in normal_results]
        heuristic_times = [r["avg_heuristic_time"] for r in normal_results]

        plt.plot(sizes_plot, dp_times, "o-", label="DP (Optimal)")
        plt.plot(sizes_plot, heuristic_times, "s-", label="Heuristic (Greedy)")
        plt.xlabel("Problem Size (Number of Jobs)")
        plt.ylabel("Average Execution Time (s)")
        plt.title("Runtime Comparison (Normal Job Density)")
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.yscale("log")
        plt.savefig("plot1_runtime_comparison.png")
        plt.show()

    # --- Plot 2: Accuracy Comparison Across Densities ---
    plt.figure(figsize=(8, 6))
    for scenario_name, results_data in all_results.items():
        if results_data:
            sizes_plot = [r["size"] for r in results_data]
            accuracies = [r["avg_accuracy"] for r in results_data]
            plt.plot(sizes_plot, accuracies, "o-", label=scenario_name)

    plt.xlabel("Problem Size (Number of Jobs)")
    plt.ylabel("Heuristic Accuracy (%)")
    plt.title("Heuristic Accuracy vs. Problem Size by Job Density")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.ylim(bottom=70, top=101)
    plt.savefig("plot2_accuracy_by_density.png")
    plt.show()

    # --- Plot 3: Summary of Accuracy at Largest Problem Size ---
    plt.figure(figsize=(8, 6))
    final_accuracies = []
    scenario_names = list(all_results.keys())

    for name in scenario_names:
        results = all_results.get(name)
        if results:
            final_accuracies.append(results[-1]["avg_accuracy"])

    if final_accuracies:
        bars = plt.bar(
            scenario_names, final_accuracies, color=["green", "orange", "red"]
        )
        plt.xlabel("Job Density Scenario")
        plt.ylabel("Average Heuristic Accuracy (%)")
        plt.title(f"Heuristic Accuracy for Largest Problem Size (N={sizes[-1]})")
        plt.ylim(bottom=min(final_accuracies) - 10, top=101)
        for bar in bars:
            yval = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                yval + 0.5,
                f"{yval:.2f}%",
                ha="center",
                va="bottom",
            )
        plt.savefig("plot3_accuracy_summary.png")
        plt.show()

    # --- Plot 4: Memory Usage Comparison ---
    plt.figure(figsize=(8, 6))
    if normal_results:
        sizes_plot = [r["size"] for r in normal_results]
        dp_mem = [r["avg_dp_mem"] for r in normal_results]
        heuristic_mem = [r["avg_heuristic_mem"] for r in normal_results]

        plt.plot(sizes_plot, dp_mem, "o-", label="DP (Optimal)")
        plt.plot(sizes_plot, heuristic_mem, "s-", label="Heuristic (Greedy)")
        plt.xlabel("Problem Size (Number of Jobs)")
        plt.ylabel("Peak Memory Usage (KiB)")
        plt.title("Memory Usage Comparison (Normal Job Density)")
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.savefig("plot4_memory_comparison.png")
        plt.show()

    print("\nSuccessfully generated 4 plots.")


if __name__ == "__main__":
    # Define problem sizes for the analysis
    SIZES = [50, 100, 200, 500, 800, 1000, 2000, 3000, 4000, 5000]

    # Number of trials for each size
    NUM_TRIALS = 5

    # Define density scenarios: multiplier for time_range = size * multiplier
    SCENARIOS = {
        "Low Density": 15,
        "Normal Density": 5,
        "High Density (High Overlap)": 1,
    }

    all_analysis_results = {}
    for name, multiplier in SCENARIOS.items():
        all_analysis_results[name] = run_analysis(SIZES, NUM_TRIALS, multiplier, name)

    save_and_plot_results(all_analysis_results, SIZES)
