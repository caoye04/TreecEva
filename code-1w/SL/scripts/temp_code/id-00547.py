import math

def preprocess_readings(readings):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in readings if x > 0]

def validate_checksum(data):
    # Distractor: checksum validation not actually used in main logic
    return sum(data) % 256 == data[-1]

def decode_quantum_state(signal):
    # Misleading intermediate transformation (unused)
    return [int((s ** 0.5) * 10) % 7 for s in signal]

def compute_entropy(seq):
    # Red herring function with complex logic but no impact on result
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def analyze_system_efficiency(energy, states):
    # Core function — relevant to final answer
    
    # Step 1: Filter active nodes
    active_nodes = {i for i, s in enumerate(states) if s in ('active', 'standby')}
    
    # Step 2: Map node indices to tier levels (dictionary usage)
    tier_map = {i: i % 4 + 1 for i in range(len(states))}
    tiers_in_use = {tier_map[i] for i in active_nodes}  # set operation
    
    # Step 3: Compute base efficiency using arithmetic and min/max
    base_efficiency = 0
    for i in active_nodes:
        base_efficiency += energy[i] * (tier_map[i] ** 0.5)
    
    # Step 4: Apply correction factor based on tier diversity
    tier_diversity_factor = len(tiers_in_use) / 4.0
    
    # Step 5: Adjust for system load (conditional adjustment)
    system_load = sum(energy[i] for i in active_nodes)
    if system_load > 1000:
        base_efficiency *= 0.9
    elif system_load < 300:
        base_efficiency *= 1.1
    
    # Step 6: Incorporate phase shift from dummy signal analysis (distractor integration)
    dummy_signal = [7, 14, 21, 28, 35]
    phase_shift = sum(decode_quantum_state(dummy_signal)) % 10  # uses decoy function
    adjusted_efficiency = base_efficiency - phase_shift * 2.5
    
    # Step 7: Final cap and flooring
    adjusted_efficiency = max(50, min(adjusted_efficiency, 950))
    
    # Step 8: Add constant offset derived from unused entropy calculation
    fake_entropy = compute_entropy([1, 2, 2, 3, 3, 3])  # red herring
    final_value = adjusted_efficiency + (fake_entropy * 0)  # neutralized
    
    return int(final_value)

# Main execution block
if __name__ == "__main__":
    
    # Initialize sensor data (some irrelevant)
    temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
    pressure_levels = {"p1": 101.3, "p2": 102.1, "p3": 99.7}
    
    # Unused configuration map
    config_flags = {
        "debug_mode": False,
        "log_level": "verbose",
        "buffer_size": 4096,
        "timeout_ms": 500
    }
    
    # Key input data (relevant)
    energy_flux = [120, 85, 210, 95, 300, 75]
    state_vector = ["active", "idle", "active", "standby", "active", "offline"]
    
    # Dummy checksum test (distractor execution)
    test_data = [10, 20, 30, 40, 235]
    is_valid = validate_checksum(test_data)  # returns False, unused
    
    # Preprocess dummy readings (irrelevant execution)
    processed = preprocess_readings(temperature_readings)
    
    # Critical statement
    thermal_capacity = analyze_system_efficiency(energy_flux, state_vector)
    
    # Output result as required
    print(f"Result: {thermal_capacity}")