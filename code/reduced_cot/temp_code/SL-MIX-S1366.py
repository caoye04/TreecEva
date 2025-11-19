import math
import itertools

def process_signal_spectrum(base_frequencies):
    # Apply logarithmic transformation to base frequencies
    log_transformed = {freq: math.log(freq) for freq in base_frequencies if freq > 0}
    
    # Generate all possible pairs and calculate their exponential product
    frequency_pairs = list(itertools.combinations(log_transformed.keys(), 2))
    pair_products = {}
    for f1, f2 in frequency_pairs:
        # Exponential of sum equals product of exponentials
        pair_products[(f1, f2)] = math.exp(log_transformed[f1] + log_transformed[f2])
    
    # Merge dictionaries with priority to pair_products
    merged_data = {**log_transformed, **pair_products}
    
    # Calculate metric as sum of all values raised to power of 1.5
    spectral_sum = sum(value ** 1.5 for value in merged_data.values())
    
    # Apply normalization using natural logarithm
    final_metric = math.log(spectral_sum) if spectral_sum > 0 else 0
    
    return final_metric

# Test with acoustic frequency data
acoustic_data = [2, 3, 5, 7]
signal_result = process_signal_spectrum(acoustic_data)
final_metric = round(signal_result, 6)
print(f"Result: {final_metric}")