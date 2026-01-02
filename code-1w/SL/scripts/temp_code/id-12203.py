import math

# Irrelevant helper function (dead code path)
def unused_calculate_entropy(data):
    return sum([-x * math.log2(x) for x in data if x > 0])

# Misleading intermediate computation
temp_offset = 17.3
counter_weights = [0.1, 0.3, 0.2, 0.4]
weighted_sum = sum([w * (i + 1) for i, w in enumerate(counter_weights)])

# Real data pipeline begins
raw_signals = [5, 8, 12, 15, 9, 3]

# Distractor: complex-looking but unused signal transformation
smoothed = list(map(lambda x: (x + temp_offset) / 2.0, raw_signals))

# Actual relevant transformation
transformed_data = [x ** 2 - 2 * x + 1 for x in raw_signals]  # (x-1)^2

# Decoy list comprehension with no side effects
_ = [math.sqrt(z) for z in transformed_data if z > 10 and z % 2 == 0]

# Bit manipulation red herring
obfuscation_key = 247 | (13 << 2)
deobfuscated_flag = obfuscation_key ^ 251 & 17

# Conditional dead end
if deobfuscated_flag > 100:
    redundant_calc = sum(smoothed) / len(smoothed)
elif deobfuscated_flag < 5:
    redundant_calc = max(smoothed)
else:
    pass  # No assignment occurs here

# Core logic hidden among noise
def apply_correction(seq, factor=0.9):
    corrected = []
    for val in seq:
        if val > 100:
            corrected.append(int(val * factor))
        else:
            corrected.append(val + 10)
    return corrected

adjusted_data = apply_correction(transformed_data)

# Higher-order function distraction
threshold_func = lambda level: (lambda x: x > level * 1.5)(12)

# Another irrelevant mapping
dummy_analysis = list(map(lambda x: x % 7 == 0, adjusted_data))

# Central processing function with nested logic
def process_metrics(data, threshold_strategy):
    base_ref = 0
    peak_memory = []

    for i, item in enumerate(data):
        if i % 2 == 0:
            base_ref += item // (i + 1) if i != 0 else item
        else:
            base_ref -= item % 5

        # Nested condition tree (some branches are never taken)
        if item < 0:
            category = 'negative'
        elif item == 0:
            category = 'zero'
        elif item < 50:
            category = 'medium'
            peak_memory.append(item * 1.2)
        else:
            category = 'high'
            peak_memory.append(item * 1.1)

    # Secondary aggregation obscured by complexity
    aggregate = base_ref
    if len(peak_memory) >= 3:
        adjustment = sum(peak_memory) / len(peak_memory)
        aggregate += int(adjustment)
    else:
        adjustment = sum(peak_memory) * 1.5
        aggregate -= int(adjustment)

    # Final branching with logical twist
    if threshold_strategy(aggregate):  # Always False due to lambda binding
        final_score = aggregate * 0.8
    else:
        final_score = aggregate + 23

    return final_score

# Key execution point
final_diagnostic = process_metrics(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")