import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([x ** 2 for x in data if x > 0])

# Decoy transformation with misleading intermediate results
def transform_signal(values):
    shifted = [v << 2 for v in values]  # Bit shift distraction
    normalized = [s / 4 for s in shifted]
    return [round(n + 0.5) for n in normalized]  # Not actually used

# Another decoy: character counting in a debug label (irrelevant)
def count_caps(label):
    return len([c for c in label if c.isupper()])

# Lambda for dynamic threshold (used once, but looks important)
adaptive_limit = lambda x, base: x > (base * 1.5)

# Core calculation chain
logic_weights = [3, 7, 9, 12, 15]
scaling_factor = 0
for i in range(len(logic_weights)):
    if i % 2 == 0:
        scaling_factor += logic_weights[i] // 3
    else:
        scaling_factor *= 2  # Early effect that matters later

# Simulate sensor array (red herring)
sensor_grid = [[i + j for j in range(4)] for i in range(4)]
total_sensors = sum(sum(row) for row in sensor_grid)

# Case conversion distraction (meaningless string op)
diag_tag = "CALIBRATE_SAFETY_CHECK"
lower_tag = diag_tag.lower()

# Real computation begins: weighted signal response
weighted_sum = 0
for idx, w in enumerate(logic_weights):
    contribution = w * (idx + 1)
    if adaptive_limit(contribution, 10):
        weighted_sum += int(math.sqrt(contribution))
    else:
        weighted_sum -= contribution % 4

# Secondary transformation (partially relevant)
intermediate_flux = 0
for val in logic_weights:
    intermediate_flux += val ^ 5  # XOR bit manipulation red herring
    if val > 10:
        intermediate_flux += 1

# Actual efficiency formula buried in distractions
def calculate_efficiency(weights):
    base = 0
    for w in weights:
        base += w ** 0.5
    adjustment = len([w for w in weights if w % 3 == 0])
    return int(base) + adjustment * 2

# Critical assignment embedded in noise
debug_mode = False
if total_sensors > 100 or debug_mode:
    print("Diagnostic mode active")  # Dead branch
else:
    thermal_capacity = calculate_efficiency(logic_weights)  # KEY STATEMENT

# Print result as required
print(f"Result: {thermal_capacity}")