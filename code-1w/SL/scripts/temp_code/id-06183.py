def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant function: pattern analysis on noise data
noise_signal = [1, 3, 2, 4, 1, 7, 5]
trend_peaks = analyze_pattern(noise_signal)

# Decoy data structures
decoys = {
    'trap_1': [x**2 for x in range(10)],
    'trap_2': {i: i*3 for i in range(5)},
    'useless_flag': True
}

# Core problem: Resource allocation with efficiency caps and constraints
resources = [120, 200, 150, 300]
efficiency_caps = [0.85, 0.92, 0.78, 0.88]
overhead_costs = [15, 22, 18, 30]
base_multiplier = 1.1

# Distractor: Unused cost calculation
projected_cost = sum([r * 0.05 for r in resources]) + 100

# Misleading intermediate score (not used in final result)
temp_score = sum(resources) / len(efficiency_caps) * 0.75

# Conditional expression with set operations
flags = {True, False, True}
enabled = 'active' if len(flags) > 1 else 'inactive'

# Early return simulation in dummy function
def validate_entry(entry):
    if not entry:
        return False
    if entry < 0:
        return False
    return True

# Unused validation loop
corrupted = False
for res in resources:
    if not validate_entry(res):
        corrupted = True
        break

# Key logic chain: Efficiency-weighted allocation with overhead deduction
adjusted_values = []
for i in range(len(resources)):
    adjusted = resources[i] * efficiency_caps[i]
    adjusted -= overhead_costs[i]  # Net effective resource
    adjusted_values.append(max(adjusted, 0))  # No negative resources

# Secondary adjustment based on global multiplier only if conditions met
if sum(adjusted_values) > 300:
    adjusted_values = [val * base_multiplier for val in adjusted_values]

# Final scoring using conditional expression and aggregation
final_sum = sum(adjusted_values)
penalty = 50 if any(x < 100 for x in adjusted_values) else 0
resource_score = final_sum - penalty

# Red herring: character counting in string representation (unused)
data_string = ''.join(map(str, resources))
char_count = len(data_string)  # Distraction

# Another decoy: set difference operation with no impact
s1 = {120, 200, 150, 300}
s2 = {100, 150, 200}
unused_diff = s1 - s2

# Critical statement
resource_score = evaluate_allocation(resources, efficiency_caps)

# Dummy function to simulate complexity
def evaluate_allocation(rsc, caps):
    # Simulate complex processing
    total = 0
    for i in range(len(rsc)):
        contribution = rsc[i] * caps[i]
        if contribution > 100:  # Threshold filter
            total += contribution * 1.05  # Bonus for high contributors
    # Apply hidden offset
    offset = 42 if len(rsc) == 4 else 0
    return int(total - offset)

print(f"Target result: {resource_score}")