import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) == int(math.sqrt(i)) for i in x if i > 0)

# Distractor transformation chain
decoy_transform = lambda lst: [x * 2 + 1 for x in lst if x % 3 != 0]

# Real data processing pipeline
base_seed = [1, 2, 3, 4, 5]
shifted_data = [x + 7 for x in base_seed]
filtered_data = list(filter(lambda x: x > 6, shifted_data))  # Keeps 8,9,10,11,12

# Apply non-linear transformation
mapped_data = [int(math.pow(x, 2)) // 3 for x in filtered_data]  # [21, 27, 33, 40, 48]

# Simulate checksum decoy (irrelevant)
checksum = sum([x ^ 255 for x in mapped_data]) // len(mapped_data)

# Real logic: recursive reduction
def recursive_reduce(arr, acc=0):
    if not arr:
        return acc
    return recursive_reduce(arr[1:], acc + (arr[0] % 19))

# Secondary distractor: string-based red herring
status_log = "Processing complete at level 5"
alert_flag = status_log.upper().count('E') > 3  # False, but looks important

# Data restructuring with tuple unpacking (real step)
primary, secondary = mapped_data[:3], mapped_data[3:]
chunk_sum = sum(primary)  # 21+27+33 = 81

# Set-based filtering to remove duplicates (distractor, no effect here)
unique_candiates = set(secondary)  # {40,48}

# Real computation begins: nested conditional with bit manipulation
interim = 0
for val in primary:
    if val & 1:  # odd?
        interim += val >> 1  # divide by 2 bitwise
    else:
        interim -= val % 7

# Another decoy: unused intermediate buffer
buffer_cache = [math.log(x + 1) for x in range(1, 100, 10)]

# Core aggregation via lambda composition
aggregator = lambda f, g: lambda x: f(g(x))
mod_round = lambda x: round(x / 2.5)
square_op = lambda x: x ** 2
composed = aggregator(mod_round, square_op)

# Apply real transformation
processed_interim = composed(interim)  # interim = (21>>1)+(27>>1)-(33%7) = 10+13-5 = 18 -> 18^2=324 -> 324/2.5=129.6 -> round=130

# Simulated multi-step state machine (mostly irrelevant)
current_state = 'INIT'
for _ in range(3):
    if current_state == 'INIT':
        current_state = 'WAIT'
    elif current_state == 'WAIT':
        current_state = 'READY'
    else:
        current_state = 'ERROR'

# Final pipeline function combining relevant and irrelevant elements
def process_pipeline(stream):
    # Real input transformation
    scaled = [x * 3 for x in stream]
    
    # Distractor: complex string parsing with no impact
    header = "HDR|CHK|LEN|DAT"
    tokens = header.split('|')
    validity = len(tokens) == len([t for t in tokens if 'H' in t])
    
    # Real logic: use recursive_reduce on scaled values
    reduced = recursive_reduce(scaled)  # recursive sum of (scaled[i] % 19)
    
    # More distractions: fake error correction
    syndrome = 0
    for i, x in enumerate(scaled):
        syndrome ^= (x * (i + 1)) % 256
    
    # Final output built from actual result and red herrings
    temp_result = reduced + processed_interim  # 130 + recursive_reduce([24,27,30]) = 130 + ((24%19)+(27%19)+(30%19)) = 130+(5+8+11)=154
    
    # One last misleading rounding
    final_diagnostic = math.floor(temp_result * 1.001)
    
    return temp_result  # Only this matters

# Execution flow
data_stream = base_seed
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")