import itertools

# Simulate a phased signal processing system with checksum validation
system_id = 5132
activation_threshold = 7
buffer_limit = 200

# Raw sensor inputs (simulated)
sensor_a = [1, 0, 1, 1]
sensor_b = [0, 1, 1, 0]
sensor_c = [1, 1, 0, 0]

# Misleading signal transformations (distractor computations)
temp_shift_a = sum(x << i for i, x in enumerate(sensor_a))  # Bit-weighted sum
temp_shift_b = sum(x << i for i, x in enumerate(sensor_b))
dummy_checksum = (temp_shift_a ^ temp_shift_b) % 17

# Combine signals using XOR folding across all sensors
combined_signal = []
for i in range(len(sensor_a)):
    combined_signal.append(sensor_a[i] ^ sensor_b[i] ^ sensor_c[i])

# Generate all phase permutations to simulate timing variations
phases = list(itertools.permutations(combined_signal[:3]))
collected_signals = []
for idx, phase in enumerate(phases):
    if idx % 2 == 0:
        # Apply phase shift and scale by index (some irrelevant scaling)
        shifted = [(val * (idx + 1)) % 2 for val in phase]
        collected_signals.extend(shifted)

# Truncate to buffer limit (distractor: not actually binding here)
collected_signals = collected_signals[:buffer_limit]

# System key derived from ID and threshold (used later)
system_key = (system_id ^ activation_threshold) & 0xFF  # Keep within byte range

# Red herring computation: simulate fake integrity check
fake_integrity_score = 0
for val in collected_signals:
    fake_integrity_score += (val + system_id) % 5
fake_integrity_score = fake_integrity_score ^ system_key

# Real processing function (depends only on collected_signals and system_key)
def process_phase_results(signals, key):
    # Count active high phases
    active_count = sum(1 for s in signals if s == 1)
    
    # Compute base output using bitwise interaction
    base_output = active_count ^ key
    
    # Secondary transformation: modulate by pattern cycle
    cycle_length = len(signals) if signals else 1
    modulation_factor = (cycle_length // 4) or 1
    intermediate = (base_output * modulation_factor) + 3
    
    # Final nonlinear adjustment using simple polynomial
    final_value = (intermediate ** 2) // 5 - 7
    
    # Dead code branch (never taken - distractor)
    if len(signals) > 1000:
        final_value += system_id % 9
    
    return final_value

# Execute main logic
final_phase_output = process_phase_results(collected_signals, system_key)

# Print result as required
print(f"Result: {final_phase_output}")