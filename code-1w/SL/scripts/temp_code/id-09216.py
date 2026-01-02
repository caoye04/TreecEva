import math

# Simulated network security evaluation system
def analyze_packet_flow(traffic):
    base_load = sum([t % 7 for t in traffic if t > 50])
    adjustment = len([t for t in traffic if t < 20]) * 3
    return base_load - adjustment  # Irrelevant to final result

# Decoy function – never called
def legacy_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d * 3
    return checksum % 1000

# Another decoy: unused transformation
transform_matrix = [[1, -1], [2, 0]]
def apply_transform(value):
    return (value * transform_matrix[0][0]) + (value // 2 * transform_matrix[1][0])

# Critical configuration
firewall_rules = [64, 32, 16, 8, 4]
encryption_key = [5, 12, 13, 84, 85]  # Pythagorean triples mixed

# Red herring variables
dummy_counter = 0
buffer_overflow_flag = False
interference_sum = 0

# Simulate false dependency chain
def compute_stability_index(rules):
    global interference_sum, dummy_counter
    index = 1
    for i in range(len(rules)):
        if rules[i] % 2 == 0:
            index *= (rules[i] // 4)
            dummy_counter += 1
        else:
            index += rules[i]
    # Dead-end calculation
    for _ in range(3):
        interference_sum += index % 10
        index = (index + 7) // 3
    return index  # Not used in main logic

# Core evaluation logic
valid_pairs = []
for i in range(len(encryption_key) - 1):
    a, b = encryption_key[i], encryption_key[i+1]
    if a < b:
        hypotenuse = math.sqrt(a*a + b*b)
        if abs(hypotenuse - round(hypotenuse)) < 0.001:
            valid_pairs.append(int(hypotenuse))

# Secondary filter using bitwise distraction
temp_filtered = []
bitwise_tracer = 0
for val in valid_pairs:
    temp_val = val ^ 15
    if temp_val & 8:  # Check if 4th bit is set
        temp_filtered.append(temp_val)
    else:
        bitwise_tracer += temp_val

# List comprehension with filtering and red herring accumulation
decoy_list = [x * 2 + 1 for x in firewall_rules if x > 10]
side_effect_sum = sum(decoy_list) // 2

# Actual answer derivation path
pair_product = 1
for p in valid_pairs:
    pair_product *= p

# Final computation disguised among distractions
def evaluate_security_protocol(key, rules):
    rule_sum = sum([r // 2 for r in rules if r >= 8])
    key_entropy = 0
    for k in key:
        if k % 3 == 0:
            key_entropy += math.log(k, 3)
    
    # Real answer contribution
    core_metric = len(valid_pairs) * pair_product
    adjustment = int(math.fsum([key_entropy, rule_sum]) % 17)
    
    # Multiple misleading operations
    fake_dependency = compute_stability_index(rules)
    noise = side_effect_sum - interference_sum + bitwise_tracer
    
    # Final formula - only core_metric and adjustment matter
    result = core_metric - adjustment
    
    # Intentionally misleading trace
    debug_log = f"Metrics: {core_metric}, adj={adjustment}, noise={noise}, fake={fake_dependency}"
    return result

# Execution point of interest
target_intermediate = analyze_packet_flow([10, 55, 60, 15, 80])
threshold_score = evaluate_security_protocol(encryption_key, firewall_rules)

# Print required output
print(f"Result: {threshold_score}")