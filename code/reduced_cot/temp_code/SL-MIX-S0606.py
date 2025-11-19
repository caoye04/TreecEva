from itertools import product
from functools import reduce

def simulate_circuit():
    # Lambda functions modeling gate delays (in nanoseconds)
    and_delay = lambda x, y: 2 if x and y else 1
    or_delay = lambda x, y: 1 if x or y else 0
    not_delay = lambda x: 1 if not x else 0
    
    # Generate all possible 4-bit input combinations
    inputs = list(product([0, 1], repeat=4))
    valid_combinations = []
    
    # Process each input combination through the circuit logic
    for a, b, c, d in inputs:
        # First layer: AND gates
        ab_and = a and b
        cd_and = c and d
        
        # Second layer: OR gate with one inverted input
        inverted_cd = not cd_and
        or_result = ab_and or inverted_cd
        
        # Final output check
        if or_result:
            # Calculate propagation delay for this path
            delay_path = [
                and_delay(a, b),
                and_delay(c, d),
                not_delay(cd_and),
                or_delay(ab_and, inverted_cd)
            ]
            valid_combinations.append((a, b, c, d, sum(delay_path)))
    
    # Early return if no valid combinations found
    if not valid_combinations:
        return 0
    
    # Extract delay values from valid combinations
    delays = [combo[4] for combo in valid_combinations]
    
    # Apply functional programming to compute total delay
    total_delay = reduce(lambda acc, x: acc + (x * 2 if x > 2 else x), delays, 0)
    
    return total_delay

# Execute simulation
final_delay = simulate_circuit()
print(f"Result: {final_delay}")