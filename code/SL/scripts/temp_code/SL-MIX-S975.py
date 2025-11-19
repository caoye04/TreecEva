import math

def compute_normalized_cross_correlation(signal_a, signal_b):
    # Calculate dot product
    dot_product = sum(a * b for a, b in zip(signal_a, signal_b))
    
    # Calculate magnitudes
    magnitude_a = math.sqrt(sum(a**2 for a in signal_a))
    magnitude_b = math.sqrt(sum(b**2 for b in signal_b))
    
    # Normalize
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)

# Signal data
signal_x = [1.0, 2.0, 3.0, 4.0]
signal_y = [4.0, 3.0, 2.0, 1.0]

# Compute using a lambda for preprocessing
preprocess = lambda s: [v - sum(s)/len(s) for v in s]  # Zero-mean normalization
normalized_signal_x = preprocess(signal_x)
normalized_signal_y = preprocess(signal_y)

# Apply sorting to one signal to simulate a phase shift correction
normalized_signal_y.sort()

# Compute final result
normalized_cross_correlation_result = compute_normalized_cross_correlation(normalized_signal_x, normalized_signal_y)

print(f"Result: {normalized_cross_correlation_result}")