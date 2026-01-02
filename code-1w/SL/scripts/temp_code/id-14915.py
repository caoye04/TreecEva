def analyze_metrics(values):
    # Irrelevant analysis function (dead end)
    temp = [v ** 0.5 for v in values if v > 10]
    avg = sum(temp) / len(temp) if temp else 0
    return avg * 2.5

# Misleading data transformations
decoy_data = [3, 7, 11, 15, 19]
shadow_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
fake_result = analyze_metrics(decoy_data)

# Actual computation inputs
data = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Red herring: unused normalization
def normalize(arr):
    total = sum(arr)
    return [x / total for x in arr] if total else arr

# Conditional expression and weighted logic
def calculate_final_score(entries, coeffs):
    if not entries or not coeffs:
        return 0.0
    
    # Apply weights conditionally based on parity (distractor logic)
    adjusted = [
        e * c if i % 2 == 0 else e * (c + 0.05) 
        for i, (e, c) in enumerate(zip(entries, coeffs))
    ]
    
    # Secondary adjustment: boost scores above 85 (but only on even indices)
    boosted = [
        val * 1.1 if idx % 2 == 0 and entries[idx] > 85 else val
        for idx, val in enumerate(adjusted)
    ]
    
    # Linear search for first score over 90 (unused result)
    first_high_idx = -1
    for i in range(len(entries)):
        if entries[i] > 90:
            first_high_idx = i
            break
    
    # Dummy bit manipulation (irrelevant)
    magic_offset = (len(entries) << 2) ^ 7
    decoy_score = sum(boosted) + magic_offset - 12.5
    
    # Core logic: compute weighted average with conditional override
    base_score = sum(boosted)
    
    # Override if all weights are above threshold (never triggered)
    override = all(w > 0.25 for w in weights)
    final = base_score if not override else 100.0
    
    # Final correction: subtract mean of original data
    mean_correction = sum(entries) / len(entries)
    return final - mean_correction

# Unused recursive helper (dead path)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Key execution point
temp_var = [x for x in data if x > 80]
flag = len(temp_var) > 3
initial_score = sum(weights) * 100 if flag else 0

final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")