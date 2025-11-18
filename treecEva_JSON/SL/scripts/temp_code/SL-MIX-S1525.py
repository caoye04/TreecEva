import math
import itertools

def transform_sequence(input_chars):
    # Step 1: Create hash values for each character
    char_hashes = [hash(c) % 1000 for c in input_chars]
    
    # Step 2: Apply exponential transformation
    exp_hashes = [math.exp(h/100) for h in char_hashes]
    
    # Step 3: Generate pairwise combinations and apply logarithmic operations
    log_combinations = []
    for a, b in itertools.combinations(exp_hashes, 2):
        if a > 0 and b > 0:
            log_val = math.log(a) + math.log(b)
            log_combinations.append(log_val)
    
    # Step 4: Filter values using set operations
    threshold = sum(log_combinations) / len(log_combinations)
    high_values = {val for val in log_combinations if val > threshold}
    low_values = frozenset(val for val in log_combinations if val <= threshold)
    
    # Step 5: Apply final transformation using both sets
    combined_set = high_values.union(low_values)
    transformed_values = [math.log(x+1) for x in combined_set if x > 0]
    
    # Step 6: Calculate final key using list comprehension
    final_key = sum([int(v*100) for v in transformed_values])
    
    return final_key

# Protocol execution
protocol_input = "SECURITY"
final_key = transform_sequence(protocol_input)
print(f"Result: {final_key}")