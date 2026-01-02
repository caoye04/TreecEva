import itertools

def analyze_irrelevant_metrics(data):
    # Distractor function: computes unused statistical metrics
    mean_val = sum(data) / len(data) if data else 0
    variance = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    return [mean_val, variance]

def generate_decoy_sequence(n):
    # Dead code path: never actually used in main logic
    return [i * i - 2*i + 1 for i in range(n) if i % 3 != 0]

def filter_by_threshold(values, thresh=5):
    # Irrelevant filtering operation
    return [v for v in values if v > thresh]

def shift_cipher(text, shift=3):
    # String manipulation red herring
    return ''.join(chr((ord(c) - 97 + shift) % 26 + 97) if c.isalpha() else c for c in text.lower())

def accumulate_weighted_sum(seq_a, seq_b):
    # Unused complex transformation
    total = 0
    for i, (a, b) in enumerate(zip(seq_a, seq_b)):
        total += a * b + i
    return total

def calculate_optimal_harvest(resources, efficiency):
    # Core logic begins
    adjusted_yield = 0
    for idx, row in enumerate(resources):
        temp_sum = 0
        for j, val in enumerate(row):
            # Apply bitwise masking based on efficiency key
            mask = efficiency.get((idx, j), 1)
            masked_val = val & (mask | 7)  # Keep low bits
            
            # Conditional branching with side irrelevant calc
            if masked_val > 5:
                temp_sum += masked_val ^ 3
            elif masked_val == 4:
                temp_sum += masked_val << 1
            else:
                temp_sum += max(masked_val, 2)
        
        # Accumulate with index weighting
        adjusted_yield += temp_sum * (idx + 1)
    
    # Final transformation using itertools.chain to flatten decoy
    decoy_data = [[i*j for j in range(3)] for i in range(4)]
    flat_decoy = list(itertools.chain.from_iterable(decoy_data))
    adjustment_factor = sum(flat_decoy[:5]) // 4 if flat_decoy else 0  # Mostly irrelevant
    
    result = adjusted_yield - adjustment_factor
    return result

def main():
    # Initialization of multiple variables — many are distractions
    sensor_readings = [12, 8, 15, 3, 22, 17]
    analysis_report = analyze_irrelevant_metrics(sensor_readings)
    
    decoy_nums = generate_decoy_sequence(10)
    filtered_set = filter_by_threshold(decoy_nums, 8)
    
    cipher_tag = shift_cipher("harvestgrid", 7)
    
    # Relevant data structures
    resource_matrix = [
        [9, 12, 5],
        [6, 8, 10],
        [3, 7, 4]
    ]
    
    efficiency_map = {
        (0, 0): 2, (0, 1): 3, (0, 2): 1,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
        (2, 0): 1, (2, 1): 2, (2, 2): 3
    }
    
    intermediate_chain = list(zip([1, 2, 3], [4, 5, 6]))
    weighted_total = accumulate_weighted_sum([1, 2, 3], [3, 2, 1])
    
    # Key execution point
    final_yield = calculate_optimal_harvest(resource_matrix, efficiency_map)
    
    # Output the required result
    print(f"Target result: {final_yield}")

if __name__ == "__main__":
    main()