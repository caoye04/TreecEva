def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            peaks += 1
    return peaks

sequence_data = [1, 3, 2, 4, 6, 5, 8, 7, 9]
smoothed_data = [x * 1.5 for x in sequence_data]
dummy_calc_1 = sum(x ** 0.5 for x in smoothed_data if x > 4)

# Misleading intermediate transformation
transformed = [int(x // 1) for x in smoothed_data]
dummy_calc_2 = max(transformed) - min(transformed)

convergence = 0
for i, val in enumerate(transformed):
    if i == 0:
        continue
    diff = abs(val - transformed[i-1])
    if diff <= 2:
        convergence += 1

# Distractor: unused but plausible computation
snapshot = {i: transformed[i] for i in range(0, len(transformed), 2)}
compression_ratio = len(snapshot) / len(transformed)

status_flags = [True if x % 3 == 0 else False for x in transformed]
flag_summary = sum(1 for f in status_flags if f)

# Real logic starts here — counting oscillations in a windowed slice
data_slice = transformed[2:8]
oscillations = 0
for i in range(1, len(data_slice)):
    if (data_slice[i] - data_slice[i-1]) * ((data_slice[i-1] - data_slice[i-2]) if i >= 2 else 1) < 0:
        oscillations += 1

baseline = sum(data_slice) / len(data_slice)
adjusted_baseline = baseline * (1 + 0.1 * oscillations)

# Another red herring — complex but unused structure
metadata_map = dict(zip(['a', 'b', 'c'], [sum(smoothed_data), peaks := analyze_pattern(sequence_data), dummy_calc_2]))
peaks  # dead reference, no effect

# Actual core function
def calculate_rating(conv, stream):
    rating = 0
    for idx, value in enumerate(stream):
        if idx % 2 == 0 and value > 5:
            rating += 2
        elif conv > 3 and value % 2 == 1:
            rating += 1
    # Secondary adjustment based on density
    density = len([v for v in stream if v > 4]) / len(stream)
    if density > 0.6:
        rating += 3
    return int(rating * 1.5)  # Final scaling

# Critical statement
final_score = calculate_rating(convergence, data_slice)

print(f"Target result: {final_score}")