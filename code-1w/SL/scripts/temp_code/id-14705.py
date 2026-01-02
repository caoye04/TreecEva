def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    normalized = [x / 10.0 for x in filtered]
    return [int(x * 2) for x in normalized]


def generate_checksum(sequence):
    checksum = 0
    for val in sequence:
        checksum ^= val  # Bitwise XOR across values
    return checksum + len(sequence)


def recursive_reduce(n):
    if n <= 1:
        return 1
    return n - recursive_reduce(n - 2)

# Irrelevant helper that's never called
def deprecated_filter(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

# Misleading auxiliary computation
baseline_metrics = {
    'peak': 127,
    'floor': -64,
    'gain': 3.141592,
    'dither': 0.001
}

raw_sensor_data = [i * (i - 10) for i in range(17)]

# Distractor transformation with no impact on final result
shadow_copy = [x + 5 for x in raw_sensor_data]
shadow_copy = [x for x in shadow_copy if x % 3 != 0]

transformed_data = preprocess_signal(raw_sensor_data)

# Dead code path — only partially connected
intermediate_checksum = generate_checksum(transformed_data)

# Create confusion with multiple sets
allowed_range = set(range(-10, 11))
temp_exclusions = {0, 1, -1, 5, -5}
threshold_set = allowed_range - temp_exclusions  # Effective threshold

# Unused but plausible-looking diagnostic
rolling_stats = []
for i in range(1, len(transformed_data)):
    rolling_stats.append(transformed_data[i] - transformed_data[i-1])

# Another red herring: complex bit manipulation with no downstream use
bit_analysis = 0
for val in transformed_data:
    bit_analysis += (val & 7) ^ 5
    bit_analysis = bit_analysis % 100

# Simulated control flow decoy
if len(transformed_data) > 5:
    scalar_offset = recursive_reduce(6)  # evaluates to 5, but unused
else:
    scalar_offset = 0

# Actual key logic buried among distractions
status_flags = set()
for val in transformed_data:
    if val > 0 and abs(val) in threshold_set:
        status_flags.add(val % 4)

# Secondary processing with set operations
complement_mask = {0, 1, 2, 3} - status_flags

# Final analysis combining boolean logic, recursion side-effects, and set ops
def analyze_pattern(data, limit_set):
    count = 0
    for v in data:
        if abs(v) in limit_set and v % 2 == 0:
            count += 1
    # Inject subtle dependency on complement_mask from outside
    adjustment = len(complement_mask) * 2
    return count * 3 - adjustment

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_set)

print(f"Target result: {final_diagnostic}")