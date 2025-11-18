import itertools

def is_valid_signal(sequence):
    if len(sequence) < 2:
        return True
    sum_squared_diff = sum((sequence[i] - sequence[i-1]) ** 2 for i in range(1, len(sequence)))
    return sum_squared_diff < 50

candidate_signals = [(1, 3, 2), (4, 1, 0, 2), (5,)]
total_valid_permutations = 0

for signal in candidate_signals:
    valid_count = 0
    for perm in itertools.permutations(signal):
        valid_count += 1 if is_valid_signal(perm) else 0
    total_valid_permutations += valid_count

signal_compliance_score = total_valid_permutations
print(f"Result: {signal_compliance_score}")