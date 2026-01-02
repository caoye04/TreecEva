def analyze_readings(data):
    cumulative = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            cumulative += val * 2
        elif i % 5 == 0:
            cumulative -= val
        else:
            cumulative += (val % 7)
    return cumulative

readings = [12, 15, 21, 8, 44, 7, 19, 33, 50, 11]

# Irrelevant signal processing branch (dead logic path)
def filter_noise(signal):
    return [x for x in signal if x > 10]

filtered = filter_noise(readings)
signal_power = sum(x**2 for x in readings[::2])

# Unused transformation chain
decoded = ''.join([chr((x + 4) % 26 + 97) for x in readings[:5]])
reversed_data = [readings[-i-1] for i in range(len(readings))]

# Real computation begins
baseline = sum(readings[i] for i in range(len(readings)) if i % 2 == 1)
offset = len([x for x in readings if x > 20])

shifted_vals = [readings[i] + offset for i in range(len(readings))]

aggregated = 0
for idx, (a, b) in enumerate(zip(shifted_vals, reversed_data)):
    if a < b:
        aggregated += (a * idx) % 11
    else:
        aggregated += (b + idx) // 3

# Secondary red herring: checksum with no impact
csum = 0
for c in decoded:
    csum = (csum + ord(c)) % 101

# Core diagnostic signature
health_signature = analyze_readings(shifted_vals)

# Distractor: complex but unused formula
compression_ratio = 3.14159
scaling_factor = (len(readings) * offset) / (sum(shifted_vals) / max(readings))
compression_level = int(scaling_factor * 10) % 9

# Actual compression factor used (simple but obscured)
compression_factor = 7

# Final computation buried among distractions
final_diagnostic = process_metrics(health_signature, baseline) // compression_factor

# Simulate missing function (must be inferred as identity-like)
def process_metrics(hs, bl):
    return hs + bl + 5

# Reset final to force re-evaluation
final_diagnostic = process_metrics(health_signature, baseline) // compression_factor

print(f"Result: {final_diagnostic}")