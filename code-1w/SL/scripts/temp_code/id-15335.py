import itertools

# Simulated sensor array data from environmental monitoring system
data_stream = [14, 17, 23, 18, 20, 25, 16, 19, 22, 24, 21, 15]

# Irrelevant baseline constants for red herring (distractor)
baseline_offset = 3.14159
reference_power = 2 ** 8
legacy_mode_flag = False
calibration_curve = lambda x: x ** 2 - 4 * x + 4  # (x-2)^2, unused in logic

# Real processing begins here
filtered_data = list(filter(lambda x: x > 17, data_stream))

# Generate sliding window averages (relevant)
def sliding_window_avg(seq, size=3):
    return [sum(seq[i:i+size]) / size for i in range(len(seq) - size + 1)]

moving_averages = sliding_window_avg(filtered_data)

# Apply transformation using itertools to pair with indices (meaningful but indirect)
indexed_avgs = list(itertools.starmap(lambda i, v: (i, round(v, 2)), enumerate(moving_averages)))
processed_data = [val for idx, val in indexed_avgs if val > 20.0]

# Decoy function - looks important but never called
def legacy_diagnostic(data):
    total = 0
    for x in data:
        total += x << 2  # bit shift red herring
    return total % 1000

# Threshold logic based on dynamic condition
threshold_func = lambda x: x > 21.5

# Secondary distractor: complex-looking but unused control flow
temp_state = 0
for i in range(5):
    if temp_state % 7 == 0:
        temp_state += i * 2
    else:
        temp_state = temp_state // 2
    # Dead code path - misleading state update

# Core diagnostic analyzer (uses relevant data and threshold)
def analyze_readings(readings, threshold_check):
    count_above = 0
    cumulative_deviation = 0.0
    base_reference = 20.5

    # Distractor variables inside function
    dummy_stack = []
    for _ in range(3):
        dummy_stack.append({"level": _, "active": False})

    # Actual logic
    for reading in readings:
        if threshold_check(reading):
            count_above += 1
            cumulative_deviation += reading - base_reference

        # Fake branch with no impact (short-circuit distraction)
        if reading < 19 and not legacy_mode_flag and (lambda: False)():
            dummy_stack.pop()

    # Final computation - only this matters
    significance_score = count_above * 100 + int(cumulative_deviation * 10)
    return significance_score

# Execute key statement
final_diagnostic = analyze_readings(processed_data, threshold_func)

# Output result as required
print(f"Target result: {final_diagnostic}")