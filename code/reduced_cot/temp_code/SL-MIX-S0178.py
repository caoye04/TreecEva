from functools import reduce

document = "algorithm optimization requires mathematical analysis and logical reasoning"

# Tokenize and clean
words = document.split()
tokens = list(map(lambda w: w.strip('.').lower(), words))

# Unique token set
unique_tokens = frozenset(tokens)

# Frequency mapping
token_freq = {token: tokens.count(token) for token in unique_tokens}

# Apply transformation using ternary logic
adjusted_freq = {k: v*2 if v > 1 else (v+1 if 'a' in k else v) for k, v in token_freq.items()}

# Compute base metric
frequency_sum = sum(adjusted_freq.values())
unique_count = len(unique_tokens)

# Decorator for complexity adjustment
def complexity_adjustment_factor(func):
    def wrapper(*args, **kwargs):
        base_value = func(*args, **kwargs)
        return base_value * 1.5 if base_value % 2 == 0 else base_value * 2.0
    return wrapper

@complexity_adjustment_factor
def calculate_base_index(freq_sum, unique_cnt):
    return freq_sum + unique_cnt

# Calculate final index
base_index = calculate_base_index(frequency_sum, unique_count)
final_complexity_index = int(base_index) if base_index > 10 else int(base_index * 3)

print(f'Result: {final_complexity_index}')