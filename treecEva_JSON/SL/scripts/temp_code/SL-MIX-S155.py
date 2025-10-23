from functools import reduce

def compute_transform(x, factor):
    return x * factor + 1

signals = [3, 7, 2, 9]
factors = {i: v for i, v in enumerate([2, 3, 1, 4], 1)}
base_threshold = 5

processed_signals = []
for idx, sig in enumerate(signals):
    factor_key = (idx % len(factors)) + 1
    if sig >= base_threshold and factor_key in factors:
        transformed = compute_transform(sig, factors[factor_key])
        processed_signals.append(transformed)
    elif sig < base_threshold or factor_key not in factors:
        processed_signals.append(sig + factors.get(factor_key, 0))

amplification_map = {k: v+1 for k, v in factors.items()}
combined_map = {**factors, **amplification_map}

final_amplification = reduce(lambda acc, val: acc + (val if val > 5 else 0), processed_signals, 0)
final_amplification += sum(combined_map.values()) if any(x > 6 for x in processed_signals) else 0

print(f"Result: {final_amplification}")