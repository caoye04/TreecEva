import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Distractor: complex-looking but unused transformation
decoy_transform = lambda z: [i ** 0.5 for i in z if i % 2 == 0]

# Real processing begins here
raw_input = [8, 12, 14, 15, 18, 21, 22]

# Misleading intermediate: looks important but only partially used
temp_analysis = {
    'evens': [x for x in raw_input if x % 2 == 0],
    'odds': [x for x in raw_input if x % 2 == 1],
    'sum_even': sum([x for x in raw_input if x % 2 == 0]),
    'sum_odd': sum([x for x in raw_input if x % 2 == 1])
}

# Bitwise manipulation red herring
bit_fiddling = [(x << 1) ^ 3 & x for x in temp_analysis['evens']]

# Unused recursive decoy
def bad_recursion(n):
    if n <= 1:
        return 1
    return n + bad_recursion(n - 2)

# Key data segments derived from raw_input
data_segments = [
    {'val': raw_input[1], 'flag': True},
    {'val': raw_input[3], 'flag': False},
    {'val': raw_input[5], 'flag': True}
]

# Another irrelevant computation with sets
phantom_set_ops = set(temp_analysis['evens']) ^ set([10, 16, 18, 20])

# Core logic hidden among noise
shifted_values = list(map(lambda item: (item['val'] >> 1) + 2, data_segments))

# Conditional filtering that actually matters
effective_vals = []
for entry in data_segments:
    if entry['flag']:
        effective_vals.append(entry['val'])

# Decoy list comprehension with case conversion (irrelevant string ops)
mock_text_flow = ''.join([chr(97 + (x % 26)).upper() for x in raw_input])

# Real transformation chain
transform_chain = [
    math.log(x, 2) for x in effective_vals if x > 10
]

rounded_steps = [round(x) for x in transform_chain]

# Actual answer derivation buried in distractions
aggregated = 0
for step in rounded_steps:
    aggregated += step * 3

# Final pipeline function that uses only specific parts
def process_pipeline(segments):
    extracted = [s['val'] for s in segments if s['flag']]
    logs = [math.log(v, 2) for v in extracted if v in [12, 21]]  # selective use
    floored = [int(l) for l in logs]  # truncates, not rounds
    total = sum(floored) * 5
    
    # Distractor inside function
    side_calc = [x ** 2 for x in range(len(segments))]  # unused
    dummy_tuple = ('ignore', 'this', 'path')  # red herring
    
    return total

# Execution point of interest
final_output = process_pipeline(data_segments)

# Output as required
print(f"Target result: {final_output}")