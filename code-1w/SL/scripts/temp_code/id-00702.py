import itertools

# Simulated sensor array readings (real data)
raw_sensor_data = [14, 28, 19, 25, 31, 17, 22]

def normalize(value):
    return (value - 10) * 1.5

def is_critical(x):
    return x > 25

def filter_outliers(seq):
    return [x for x in seq if x < 30]

def accumulate(values):
    total = 0
    for v in values:
        total += v
    return total

# Irrelevant helper: computes harmonic mean (not used in final result)
def harmonic_mean(seq):
    if not seq:
        return 0
    return len(seq) / sum(1/v for v in seq if v != 0)

# Dead-end function: looks useful but unused
def smooth_signal(data):
    return [sum(data[max(0,i-1):i+1]) / (i+1) for i in range(len(data))]

# Decoy transformation chain
temp_a = [normalize(x) for x in raw_sensor_data]
temp_b = list(map(lambda x: x * 0.9, temp_a))
temp_c = [x for x in temp_b if x > 15]  # filtered but unused

# Actual processing begins here
base_levels = list(map(normalize, raw_sensor_data))
cleaned_levels = filter_outliers(base_levels)

# Misleading accumulation (red herring)
dummy_sum = accumulate(temp_c) * 0.1  # unused downstream

# Real signal processing
processed_signals = []
for val in cleaned_levels:
    if is_critical(val):
        processed_signals.append(int(val) | 3)  # bitwise interference
    else:
        processed_signals.append(int(val) & 15)

# Another decoy: complex but irrelevant structure
decoys = list(itertools.combinations_with_replacement([2,3], 2))
shadow_matrix = [[a*b for a in decays] for b in decays]  # typo + dead code

# Critical analysis function
def analyze_readings(signal_list):
    count = 0
    checksum = 0
    for idx, val in enumerate(signal_list):
        if idx % 2 == 0:
            count += 1
            checksum ^= val  # XOR accumulation
        else:
            checksum += val % 3
    # Final transformation
    return (checksum * count) % 97

# Unused recursive red herring
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

# Unused logical trap
flag_state = (len(raw_sensor_data) > 5) and (harmonic_mean(temp_a) < 20) or False

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Print required output
print(f"Result: {final_diagnostic}")