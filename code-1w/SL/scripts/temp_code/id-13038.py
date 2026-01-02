import math

# Simulated sensor data processing with embedded logic chain and distractions
def analyze_pulse_sequence(raw_readings):
    filtered = [x for x in raw_readings if x > 0]  # Ignore non-positive readings
    baseline = sum(filtered) / len(filtered)
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - baseline) * 1.05, 2) for x in filtered]
    inverted = [abs(x - max(normalized)) for x in normalized]  # Unused path

    # Core signal extraction
    signal_energy = 0
    for i in range(len(filtered)):
        if i % 2 == 0:
            signal_energy += filtered[i] * math.log(i + 1.5)
        else:
            signal_energy -= filtered[i] ** 0.5

    return signal_energy


def generate_phase_shifts(n):
    # Distractor: generates unused phase array
    phases = []
    for i in range(n):
        val = (i * 17) % 13
        phases.append(val)
    return phases  # Never used

def encrypt_key(sequence):
    # Bit manipulation red herring
    key = 0
    for num in sequence:
        key ^= int(num * 3.7) & 255
    return key  # Computed but irrelevant

def transform_signal(data):
    # Real transformation affecting result
    shifted = [(data[i] + data[-i-1]) for i in range(len(data))]
    amplified = [x * 1.1 for x in shifted]
    return [round(x, 2) for x in amplified]

def decode_entropy(signature):
    # Complex-looking but unused entropy decoder
    total = 0
    for c in str(signature):
        if c.isdigit():
            total += int(c) ** 2
    return total % 100

def process_sequence(seq):
    # Critical recursive reduction function
    def reduce_recursive(arr):
        if len(arr) <= 1:
            return arr[0] if arr else 0
        mid = len(arr) // 2
        left = reduce_recursive(arr[:mid])
        right = reduce_recursive(arr[mid:])
        return left + right * 0.9  # Weighted merge

    # Destructuring distraction
    first, *rest = seq
    last = rest[-1] if rest else first
    peak = max(seq)
    stats_sum = first + last + peak

    # Actual computation path
    processed = [x * 0.85 for x in seq if x > 50]  # Filter and scale
    temp_result = reduce_recursive(processed)

    # Final adjustment using bitwise masking (real use)
    mask = 0b111111
    masked_value = int(abs(temp_result)) & mask
    final_score = masked_value * 1.25

    return round(final_score, 6)

# Main execution block
if __name__ == "__main__":
    # Input data (simulated diagnostic readings)
    sensor_input = [12, 45, 67, 89, 112, 98, 55, 43, 78, 91]

    # Step 1: Analyze pulse (used)
    energy_level = analyze_pulse_sequence(sensor_input)

    # Step 2: Generate useless phase shifts (distractor)
    phase_array = generate_phase_shifts(len(sensor_input))

    # Step 3: Encrypt key (red herring)
    security_key = encrypt_key(sensor_input)

    # Step 4: Transform signal (used later)
    transformed_data = transform_signal(sensor_input)

    # Step 5: Decode entropy (dead end)
    fingerprint = decode_entropy(energy_level)

    # Step 6: Process the sequence to get final diagnostic (TARGET STATEMENT)
    final_diagnostic = process_sequence(transformed_data)

    # Output target result
    print(f"Result: {final_diagnostic}")