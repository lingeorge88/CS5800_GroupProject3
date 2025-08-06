import random
import math

def distributeCookies(cookies, k):
    n = len(cookies)
    
    # Initialize: random assignment of bags to children
    assignment = [random.randint(0, k-1) for _ in range(n)]
    
    def calculate_unfairness(assignment):
        # Calculate max cookies any child has
        child_cookies = [0] * k
        for bag_idx, child in enumerate(assignment):
            child_cookies[child] += cookies[bag_idx]
        return max(child_cookies)
    
    def get_neighbor(assignment):
        # Generate neighbor: reassign one bag to different child
        new_assignment = assignment.copy()
        bag_to_move = random.randint(0, n-1)
        old_child = new_assignment[bag_to_move]
        new_child = random.randint(0, k-1)
        while new_child == old_child and k > 1:
            new_child = random.randint(0, k-1)
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
    
    for i in range(iterations):
        # Get neighbor solution
        neighbor = get_neighbor(current)
        neighbor_unfairness = calculate_unfairness(neighbor)
        
        # Calculate change in unfairness
        delta = neighbor_unfairness - current_unfairness
        
        # Accept or reject
        if delta < 0:  # Better solution
            current = neighbor
            current_unfairness = neighbor_unfairness
            if current_unfairness < best_unfairness:
                best = neighbor.copy()
                best_unfairness = current_unfairness
        else:  # Worse solution - accept with probability
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current = neighbor
                current_unfairness = neighbor_unfairness
        
        # Cool down
        temperature *= cooling_rate
        
        # Optional: restart if temperature too low
        if temperature < 0.001:
            temperature = 10.0  # Reheat
    
    return best_unfairness

print(distributeCookies([8,15,10,20,8], 2)) # 31
print(distributeCookies([6,1,3,2,2,4,1,2], 3)) # 7

print(distributeCookies([1,2,3,4,5], 1)) # 15
print(distributeCookies([10,20,30,40], 4)) # 40
print(distributeCookies([1,1,1,1,100], 2)) # 100
print(distributeCookies([5,5,5,5,5,5], 3)) # 10
print(distributeCookies([1,1,1,1,1,1,1,1,1,1], 5)) # 2
print(distributeCookies([1000,2000,3000,4000,5000], 2)) # 8000
print(distributeCookies([1,2,3,4,5,6,7,8,9,10], 3)) # 19
print(distributeCookies([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 4)) # 30

