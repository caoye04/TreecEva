import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

# Another decoy: unused transformation
def mirror_sequence(seq):
    return seq + seq[::-1]

# Core processing pipeline
initial_seed = [3, 7, 12, 15, 21, 22, 29, 31]
dummy_weights = [0.1, 0.5, 0.3, 0.9, 0.2, 0.7, 0.4, 0.6]

# Distractor: complex-looking but unused weighted sum
total_weighted = sum(initial_seed[i] * dummy_weights[i] for i in range(len(initial_seed)))
scaling_factor = 1.75

# Actual signal path begins here
transformed = []
for val in initial_seed:
    temp = val ^ 5  # Bitwise XOR with 5
    if temp % 3 == 0:
        transformed.append(temp * 2)
    elif temp > 10:
        transformed.append(int(math.sqrt(temp)))
    else:
        transformed.append(temp + 4)

# Intermediate filtering based on parity and magnitude
intermediate_filtered = list(filter(lambda x: x % 2 == 1 and x < 15, transformed))

# Misleading accumulation (dead code path)
cumulative_xor = 0
for num in intermediate_filtered:
    cumulative_xor ^= num * 3

# Real computation: apply logarithmic scaling only to selected elements
log_mapped = []
for x in intermediate_filtered:
    if x > 5:
        log_mapped.append(math.log(x, 2))
    else:
        log_mapped.append(x ** 0.5)

# Secondary filter: retain only those close to integer values
almost_integer_mask = [abs(y - round(y)) < 0.15 for y in log_mapped]
refined_values = [log_mapped[i] for i in range(len(log_mapped)) if almost_integer_mask[i]]

# Apply final non-linear transformation
final_transformation = lambda data: [round(z ** 3, 4) for z in data]
processed_data = [x + 0.1 for x in refined_values]  # Small perturbation

# Critical assignment
filtered_result = sum(final_transformation(processed_data))

# Distractor: unused nested structure
redundant_matrix = [[i*j + 2 for j in range(3)] for i in range(4)]
shadow_sum = sum(sum(row) for row in redundant_matrix)

# Decoy statistical check
mean_decoy = sum(intermediate_filtered) / len(intermediate_filtered) if intermediate_filtered else 0

# Output the actual target result
print(f"Result: {filtered_result}")