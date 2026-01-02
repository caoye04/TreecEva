from itertools import combinations

def analyze_variability(sequence):
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    variability = sum(diffs) / len(diffs) if diffs else 0
    return variability

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    deviances = [abs(x - mean_val) for x in data]
    filtered = [x for x in data if abs(x - mean_val) < threshold * (sum(deviances) / len(deviances))]
    return filtered

def generate_pair_metrics(items):
    pair_sums = [a + b for a, b in combinations(items, 2)]
    pair_products = [a * b for a, b in combinations(items, 2)]
    excess_calc = sum(pair_sums) * 0.1  # Distractor: not used later
    return pair_sums

def calculate_harmonic_aggregate(values):
    reciprocal_sum = sum(1/x for x in values if x != 0)
    harmonic_mean = len(values) / reciprocal_sum
    adjustment = 0.5 if len(values) > 4 else 0
    return harmonic_mean + adjustment

def main():
    raw_input = [12, 7, 15, 10, 22, 8, 14]
    
    # Step 1: Filter outliers based on dynamic threshold
    cleaned_data = filter_outliers(raw_input, threshold=2.0)
    
    # Step 2: Analyze sequential variability (distractor computation)
    trend_metric = analyze_variability(sorted(cleaned_data))
    noise_level = trend_metric * 0.3  # Unused beyond this point
    
    # Step 3: Generate refined dataset using combinatorics
    pair_extrema = [min(cleaned_data), max(cleaned_data)]
    extended_refinement = cleaned_data + pair_extrema
    unique_values = list(set(extended_refinement))  # Remove duplicates
    
    # Step 4: Compute auxiliary metrics (some irrelevant)
    _ = generate_pair_metrics(unique_values)  # Returns unused pair sums
    size_flag = len(unique_values) >= 6
    
    # Step 5: Final transformation before key calculation
    refined_data = sorted([x for x in unique_values if x > 9])
    
    # Key statement
    final_yield = calculate_harmonic_aggregate(refined_data)
    
    # Output result
    print(f"Result: {final_yield}")

if __name__ == "__main__":
    main()