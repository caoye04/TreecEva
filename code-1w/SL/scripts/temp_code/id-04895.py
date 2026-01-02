import itertools

# Irrelevant helper function (dead code path)
def calculate_entropy(data):
    return sum(x * x for x in data) / len(data) if data else 0

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x ** 2 for x in seq]
    temp_b = [y % 7 for y in temp_a]
    temp_c = [z + 3 for z in temp_b if z > 2]
    return sorted(temp_c, reverse=True)

# Unused signal processor (distractor)
class SignalProcessor:
    def __init__(self, threshold=5.0):
        self.threshold = threshold
        self.buffer = []

    def process(self, value):
        return value * 1.5 if value > self.threshold else value * 0.5

# Core computation with hidden logic path
def apply_filter(values, mode='low'):
    if mode == 'high':
        return [v * 1.1 for v in values]
    else:
        return [v * 0.9 for v in values]

# Decoy mathematical operation
def compute_harmonic_mean(nums):
    if not nums or any(x == 0 for x in nums):
        return 0
    return len(nums) / sum(1/x for x in nums)

# Real computational chain begins here
raw_input = [3, 7, 12, 18, 25]

# Step 1: Initial transformation with list comprehension
distorted = [x * 2 + 1 for x in raw_input]

# Step 2: Filter irrelevant elements (only even indices matter)
even_indexed = [distorted[i] for i in range(0, len(distorted), 2)]  # [7, 49, 51]

# Step 3: Apply modular arithmetic and shift
twisted = [(val % 11) * 3 for val in even_indexed]  # [7%11=7→21, 49%11=5→15, 51%11=7→21]

# Step 4: Accumulate with offset
accumulated = 0
for num in twisted:
    accumulated += num + 4  # 21+4=25, 15+4=19, 21+4=25 → total 69

# Step 5: Compute secondary path (distractor but looks important)
shadow_value = sum(transform_sequence([4, 8, 15, 16, 23]))  # [64%7=1+3=4, ...] → complex but unused

# Step 6: Correction factor derived from filtered sum
base = accumulated  # 69
filter_result = apply_filter([2, 4, 6], mode='low')  # [1.8, 3.6, 5.4] — looks important, unused

# Step 7: Key dependency on dictionary lookup
correction_map = {k: k*0.1 for k in range(10, 100, 10)}
correction_factor = correction_map.get(len(twisted) * 3, 0.5)  # len=3 → 9 → not in keys → default 0.5

# Step 8: Final adjustment logic
def adjust_flux(b, c):
    intermediate = b * (1 + c)
    # Extra confusion layer
    if intermediate > 100:
        intermediate = intermediate * 0.85
    # Critical rounding step
    return int(intermediate + 0.5)  # round to nearest integer

# Execution point of interest
final_flux = adjust_flux(base, correction_factor)

# Red herring output
print(f"Diagnostics: {shadow_value}, {sum(filter_result)}")

# Target result output
print(f"Target result: {final_flux}")