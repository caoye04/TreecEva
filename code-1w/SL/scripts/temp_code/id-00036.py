import math

def modified_fibonacci_sequence(seed_a, seed_b, count):
    seq = [seed_a, seed_b]
    for i in range(2, count):
        next_val = math.sqrt(seq[i-1]**2 + seq[i-2]**2)
        seq.append(next_val)
    return seq

# Generate sequence
portfolio_volatility_series = modified_fibonacci_sequence(1.5, 2.3, 12)

# Calculate product of even-indexed terms (0-based indexing: indices 2,4,6,8,10)
even_index_terms = [portfolio_volatility_series[i] for i in range(2, len(portfolio_volatility_series), 2)]
product_of_evens = math.prod(even_index_terms)

# Compute log adjustment
log_adjustment = math.log10(product_of_evens)
print(f'Result: {log_adjustment}')