def preprocess_log(data):
    # Irrelevant transformation: counts digits but not used in final result
    digit_count = sum(c.isdigit() for c in data)
    normalized = data.replace('-', '').replace(':', '').lower()
    return normalized


def validate_sequence(seq):
    # Dead-end validation function (never called)
    if len(seq) < 5:
        return False
    return all(c.isalnum() for c in seq)

# Simulated system log with embedded patterns
raw_logs = [
    "LOG-2023-CHK:AB7F",
    "LOG-2023-CHK:CD3E",
    "LOG-2023-CHK:AB7F",  # duplicate
    "LOG-2023-CHK:EF9G",
    "LOG-2023-CHK:CD3E",  # duplicate
    "LOG-2023-CHK:AB7F",  # duplicate
]

# Misleading aggregation (not directly useful)
temp_aggregate = {}
for log in raw_logs:
    key = log[-4:]
    temp_aggregate[key] = temp_aggregate.get(key, 0) + 1

# Decoy statistical analysis
avg_repeats = sum(temp_aggregate.values()) / len(temp_aggregate) if temp_aggregate else 0
decoys = [x * 2 for x in temp_aggregate.values() if x > 1]
phantom_score = sum(decoys) - avg_repeats

# Actual processing begins here
processed_entries = [preprocess_log(entry) for entry in raw_logs]

# Extract numeric suffix and convert to integer using string methods
numeric_parts = []
for entry in processed_entries:
    digits = ''.join([c for c in entry if c.isdigit()])
    if digits:
        numeric_parts.append(int(digits))

# Bit manipulation red herring
shifted_values = []
for num in numeric_parts:
    shifted = (num << 2) ^ 0xA  # XOR with magic number
    shifted_values.append(shifted)

# Real computation path
unique_numbers = list(set(numeric_parts))  # Remove duplicates
sorted_uniques = sorted(unique_numbers, reverse=True)

# Apply recursive filtering: keep only numbers where sum of digits is even
def sum_of_digits_even(n):
    return sum(int(d) for d in str(n)) % 2 == 0

filtered_diagnostics = []
def recursive_filter(nums, index=0):
    if index >= len(nums):
        return
    if sum_of_digits_even(nums[index]):
        filtered_diagnostics.append(nums[index])
    recursive_filter(nums, index + 1)  # Simple recursion

recursive_filter(sorted_uniques)

# Final pattern analysis
running_total = 0
for val in filtered_diagnostics:
    running_total += val * 3
    running_total -= 5  # adjustment factor

# Key statement
final_diagnostic = running_total + len(filtered_diagnostics)

# Distractor: unused checksum
checksum = 0
for c in str(final_diagnostic):
    checksum ^= ord(c)

print(f"Result: {final_diagnostic}")