# GROUP 6
# Members: George Lin, Andrew Li, Xiaoti Hu, Mingda Xie
# Group Project 3 : Fair Distribution of Cookies Solution - Simulated Annealing

import random
import math


def distributeCookies(cookies, k):
    n = len(cookies)

    # initialize: random assignment of bags to children
    assignment = [random.randint(0, k - 1) for _ in range(n)]

    def calculate_unfairness(assignment):
        # calculate max cookies any child has
        child_cookies = [0] * k
        for bag_idx, child in enumerate(assignment):
            child_cookies[child] += cookies[bag_idx]
        return max(child_cookies)

    def get_neighbor(assignment):
        # generate neighbor: reassign one bag to different child
        new_assignment = assignment.copy()
        bag_to_move = random.randint(0, n - 1)
        old_child = new_assignment[bag_to_move]
        new_child = random.randint(0, k - 1)
        # avoid picking the same child
        while new_child == old_child and k > 1:
            new_child = random.randint(0, k - 1)
        new_assignment[bag_to_move] = new_child
        return new_assignment

    # SA parameters
    current = assignment
    current_unfairness = calculate_unfairness(current)
    best = current.copy()
    best_unfairness = current_unfairness

    temperature = 100.0
    cooling_rate = 0.995
    iterations = 10000

    # main optimization loop
    for i in range(iterations):
        neighbor = get_neighbor(current)
        neighbor_unfairness = calculate_unfairness(neighbor)

        delta = neighbor_unfairness - current_unfairness

        # accept or reject
        if delta < 0:  # better solution
            current = neighbor
            current_unfairness = neighbor_unfairness
            if current_unfairness < best_unfairness:
                best = neighbor.copy()
                best_unfairness = current_unfairness
        else:  # worse solution, accept with probability
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current = neighbor
                current_unfairness = neighbor_unfairness

        # cool down
        temperature *= cooling_rate

        # restart if temperature too low
        if temperature < 0.001:
            temperature = 10.0  # reheat

    return best_unfairness


if __name__ == "__main__":
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
    )  # 30
