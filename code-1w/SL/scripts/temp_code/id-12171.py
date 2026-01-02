import math

# Sensor simulation parameters (irrelevant to final result)
base_frequency = 42.5
harmonic_noise = [0.1, -0.3, 0.7, -0.2]
dummy_thresholds = {k: k**2 for k in range(10)}

# Real data pipeline starts here
raw_data_stream = [18, 24, 15, 42, 12, 36, 27, 33, 21, 30]
scaling_factor = 3
offset_correction = 6

# Step 1: Apply scaling and offset (relevant)
adjusted_readings = [(x * scaling_factor) + offset_correction for x in raw_data_stream]

# Irrelevant noise modeling
noise_profile = []
for i in range(len(harmonic_noise)):
    noise_profile.append(math.sin(harmonic_noise[i] * base_frequency))

# Step 2: Filter values above threshold (relevant)
filtered_readings = [val for val in adjusted_readings if val > 50]

# Decoy signal transformation (dead path)
transformed_signal = []
for x in raw_data_stream:
    if x % 3 == 0:
        transformed_signal.append(x ** 0.5)

# Step 3: Group into chunks of 3 and compute averages (relevant)
def chunk_and_average(data, size=3):
    chunks = [data[i:i+size] for i in range(0, len(data), size)]
    return [sum(chunk)/len(chunk) for chunk in chunks if len(chunk) == size]

chunk_averages = chunk_and_average(filtered_readings)

# Misleading statistical analysis (distractor)
spurious_correlation = 0
for i in range(min(5, len(noise_profile))):
    spurious_correlation += noise_profile[i] * (i + 1)

# Step 4: Process signals through nonlinear activation (relevant)
activation_log = []
processed_signals = []
for avg in chunk_averages:
    activated = math.log(avg) * 10
    activation_log.append(activated)
    if activated > 20:
        processed_signals.append(activated)

# Red herring: unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Step 5: Analyze readings with bit manipulation twist (relevant)
def analyze_readings(signals):
    cumulative_score = 0
    for sig in signals:
        # Map signal to integer bucket
        bucket = int(sig)
        # Extract bits at positions 1, 3, and 5 (LSB index 0)
        extracted = (bucket >> 1) & 1
        extracted += (bucket >> 3) & 1
        extracted += (bucket >> 5) & 1
        # Accumulate based on bit density
        cumulative_score += extracted * (sig / 5)
    
    # Final adjustment using sum of digits (relevant)
    digit_sum = sum(int(d) for d in str(int(cumulative_score)))
    return cumulative_score + digit_sum

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Print result for evaluation
print(f"Target result: {final_diagnostic}")