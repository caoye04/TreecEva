import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading precomputed table (partially unused)
lookup_cache = {i: (i * i) % 17 for i in range(50)}

# Unused signal weights (red herring)
signal_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Real data stream with embedded patterns
data_stream = [12, 8, 15, 3, 7, 14, 6, 9]

# Distractor: complex-looking but unused transformation pipeline
class DataProcessor:
    def __init__(self):
        self.history = []
        self.active = True

    def absorb(self, x):
        return x ^ 25

    def flush(self):
        return sum(self.history) // len(self.history) if self.history else 0

# Unused instance (dead object)
processor = DataProcessor()

# String-based control flag (irrelevant to logic but looks important)
mode_flag = "ENHANCED_VERIFICATION_ACTIVE"

# Conditional toggle based on string check (distractor)
if mode_flag.lower().startswith("enh") and len(mode_flag) > 10:
    activation_level = 2
else:
    activation_level = 1

# Bit manipulation lookup (some entries used, others not)
bit_shift_map = {}
for idx, val in enumerate([2, 3, 1, 4]):
    bit_shift_map[idx] = val << (idx % 3)

# Real processing begins here
filtered_data = []
for num in data_stream:
    if num & 1:  # Only odd numbers proceed
        filtered_data.append(num)

# Secondary filter: keep only those > average
avg_before = sum(data_stream) / len(data_stream)
trimmed = [x for x in filtered_data if x > avg_before]

# Use of enumerate and zip (required python features)
indexed_trimmed = list(enumerate(trimmed))
shift_pairs = list(zip(trimmed, trimmed[1:] + [trimmed[0]]))

# Actual computation path
rolling_result = 0
for i, (val, shift_val) in enumerate(shift_pairs):
    # Mix arithmetic and bitwise ops
    temp = (val ^ shift_val) + i
    if i % 2 == 0:
        temp = temp * 3
    rolling_result += temp

# Set of unique values (set operation - required feature)
unique_cycle_vals = set(trimmed)

# Additional red herring: string method chain that does nothing
status_log = "Processing complete. Finalizing..."
status_log.upper().replace(" ", "_").lstrip("P")

# Core calculation using modular arithmetic and combinatorics
combinatoric_factor = 1
for j in range(1, len(unique_cycle_vals) + 1):
    combinatoric_factor = (combinatoric_factor * j) % 10007

# Final transformation
intermediate = rolling_result ^ combinatoric_factor
intermediate = intermediate + (len(trimmed) << 3)

# Decoy branch (never executed)
if activation_level > 5:
    final_output = intermediate / 100
else:
    # This is the real assignment
    final_output = int(intermediate)

# Additional distraction: unused list comprehension with string methods
_ = [ch.lower() for ch in "ABC123" if ch.isalpha()]

# Print result as required
print(f"Result: {final_output}")