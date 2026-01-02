from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_data(raw):    filtered = [x for x in raw if 10 <= x <= 100]
    noise_count = len(raw) - len(filtered)
    adjusted = [x + 1.5 for x in filtered]  # calibration offset
    return adjusted, noise_count

def generate_pairs(values):
    # Generate all pairs but only use sum of first three for score
    all_pairs = list(combinations(values, 2))
    pair_sums = [sum(pair) for pair in all_pairs]
    top_three_sum = sum(sorted(pair_sums)[:3])  # Irrelevant: not used in final logic
    return top_three_sum

def calculate_weighted_average(vals, wts):
    # Unused helper function - red herring
    return sum(v * w for v, w in zip(vals, wts)) / sum(wts) if wts else 0

def calculate_final_score(data, weights):
    processed, dropped = preprocess_data(data)
    
    # Dummy tracking variables
    total_elements = len(data)
    valid_ratio = len(processed) / total_elements if total_elements else 0
    
    # Core logic: find all triplets, compute their product, filter > threshold
    triplet_products = []
    for i in range(len(processed)):
        for j in range(i+1, len(processed)):
            for k in range(j+1, len(processed)):
                product = processed[i] * processed[j] * processed[k]
                if product > 50000:
                    triplet_products.append(product)
    
    # Secondary filtering based on weighted thresholds (weights partially used)
    base_threshold = sum(weights) * 2.5
    refined_products = [p for p in triplet_products if p % 5 == 0]
    
    # Accumulation with conditional scaling
    cumulative = 0
    for val in refined_products:
        if val > 80000:
            cumulative += val * 0.1
        else:
            cumulative += val * 0.05
    
    # Final adjustment using unused ratio and dummy pair logic
    pair_bonus = generate_pairs(processed) * 0.01  # Computationally heavy but irrelevant
    final_score = int(cumulative - base_threshold + valid_ratio * 100)
    
    # These variables are tracked but unused in result
    debug_info = {"dropped": dropped, "pairs_generated": len(list(combinations(processed, 2)))}
    
    return final_score

# Input data and weights
data = [8, 12, 15, 20, 9, 25, 30, 11, 100, 45]
weights = [1, 2, 1, 3]

# Execute main computation
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")