import itertools

def process_data(primary, secondary):
    # Relevant computation: filter and transform data
    filtered = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, primary))
    transformed = [x * 2 - 1 for x in filtered]
    
    # Distractor: complex but unused secondary processing
    secondary_sum = sum(secondary) * 3
    unused_permutations = list(itertools.permutations(secondary[:3]))
    misleading_total = len(unused_permutations) * secondary_sum
    
    # Core logic with early return
    if len(transformed) == 0:
        return misleading_total  # Dead code path
    
    # Relevant: pairwise combinations and final calculation
    pairs = list(itertools.combinations(transformed, 2))
    valid_pairs = [(a, b) for a, b in pairs if a > b and (a + b) % 4 == 0]
    
    if not valid_pairs:
        return misleading_total  # Another dead path
    
    # Final relevant computation
    result_values = [a * b - (a - b) for a, b in valid_pairs]
    return sum(result_values) % 47

# Main execution with mixed relevant and distracting data
main_values = [8, 15, 22, 30, 41, 45, 52, 60]
secondary_data = [7, 12, 18, 25]

# Distracting intermediate calculations
unused_calculation = (sum(main_values) * len(secondary_data)) // 3
misleading_counter = len([x for x in main_values if x < 20]) * 100

# Key execution point
result = process_data(main_values, secondary_data)

# More distractions before final output
final_adjustment = (result * 3 + 17) % 23  # Irrelevant transformation
final_output = result + 0  # Critical variable - answer is just result

print(f"Target result: {final_output}")