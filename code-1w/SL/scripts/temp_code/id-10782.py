def process_string(s):
    # Irrelevant string processing with red herring logic
    if len(s) % 2 == 0:
        s = s[::-1]
    s = s.upper().replace('A', 'X')
    return s  # Never used in final computation

# Distractor data structures
telemetry_logs = [
    {'timestamp': 1001, 'value': 42, 'type': 'debug'},
    {'timestamp': 1002, 'value': -15, 'type': 'info'},
    {'timestamp': 1003, 'value': 88, 'type': 'debug'}
]

useless_counter = 0
for log in telemetry_logs:
    if log['type'] == 'debug':
        useless_counter += log['value'] * 2  # Dead path: not used later

# Actual relevant data
raw_inputs = [12, -7, 3.5, 4.0, 9, 2]

# Decoy function that looks important but isn't called correctly
def analyze_outliers(seq, threshold=5):
    return [x for x in seq if abs(x) > threshold]

# Another decoy using string methods (meets language feature requirement)
status_flags = ['active', 'idle', 'pending', 'ACTIVE']
flag_summary = ''.join([f[0] for f in status_flags]).upper()
decoded = flag_summary.replace('A', 'T').count('T')  # Misleading intermediate

# Core calculation chain
filtered = [x for x in raw_inputs if x > 0]
squared = [x ** 2 for x in filtered]
sum_sq = sum(squared)
mean_sq = sum_sq / len(squared)

# Bit manipulation red herring
bit_fiddling = 0
for i in range(5):
    bit_fiddling |= (1 << i)
    bit_fiddling ^= i  # Complex but irrelevant

# Conditional data transformation
if mean_sq > 50:
    adjustment_factor = 0.8
else:
    adjustment_factor = 1.2

adjusted_rms = (mean_sq ** 0.5) * adjustment_factor

# Simultaneous assignment distraction
alpha, beta = 10, 20
gamma, delta = beta + 5, alpha - 3  # Unused variables

# Main composite logic
def calculate_composite_score(data):
    base_values = [x for x in data if isinstance(x, (int, float))]
    
    # String method used meaningfully (though disguised)
    magic_key = "threshold"
    shift_val = len(magic_key)  # Uses string length as numeric input
    
    # Logical operations and comparisons
    valids = [v for v in base_values if v >= (shift_val - 2)]
    
    # Min/max/average calculations
    if not valids:
        return 0
    
    peak = max(valids)
    trough = min(valids)
    avg_val = sum(valids) / len(valids)
    
    # Complex formula with logical conditions
    score = 0
    if peak > 5 and avg_val > 3:
        score += peak * 2
    if trough < 4:
        score += 15
    
    # Short-circuit evaluation pattern
    bonus = (len(valids) > 2) and (avg_val > 4) and 22 or 0
    score += bonus
    
    # Final adjustment using bitwise (looks complex but deterministic)
    score = score ^ 7  # XOR to obscure reasoning
    score = score & 1023  # Clamp with bitmask
    
    return score

# Execution point of interest
data = [12, -7, 3.5, 4.0, 9, 2]
intermediate = adjusted_rms  # Distraction
final_score = calculate_composite_score(data)

print(f"Result: {final_score}")