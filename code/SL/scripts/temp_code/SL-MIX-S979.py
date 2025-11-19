import itertools

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def calculate_optimized_loads(package_weights, max_capacity):
    optimized_load_count = 0
    
    # Generate all possible combinations of packages
    for r in range(1, len(package_weights) + 1):
        for combo in itertools.combinations(package_weights, r):
            if sum(combo) <= max_capacity:
                optimized_load_count += 1
    
    return optimized_load_count

# Main execution
if __name__ == "__main__":
    # Generate first 8 Fibonacci numbers as package weights
    package_weights = fibonacci_sequence(8)
    
    # Truck maximum capacity
    max_capacity = 20
    
    # Calculate optimized loads using dynamic programming concept
    optimized_load_count = calculate_optimized_loads(package_weights, max_capacity)
    
    # Apply set operations to filter unique load configurations
    valid_configs = set()
    for r in range(1, len(package_weights) + 1):
        for combo in itertools.combinations(package_weights, r):
            if sum(combo) <= max_capacity:
                valid_configs.add(combo)
    
    # Final adjustment using stack principles (LIFO)
    config_stack = list(valid_configs)
    while config_stack:
        current_config = config_stack.pop()
        if sum(current_config) % 2 == 0:
            optimized_load_count += 1
    
    print(f"Result: {optimized_load_count}")