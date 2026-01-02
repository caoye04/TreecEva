def calculate_efficiency(logs):
    total_ops = 0
    critical_count = 0
    
    for idx, entry in enumerate(logs):
        op_code = entry & 0xFF
        timestamp_valid = (entry >> 24) & 0x01
        
        if timestamp_valid:
            total_ops += op_code
            if op_code > 128:
                critical_count += 1
    
    safety_factor = 1.75 if critical_count > 2 else 1.25
    efficiency = total_ops * safety_factor
    energy_threshold = int(efficiency // (critical_count + 1))
    return energy_threshold

# Simulated system log entries (32-bit words)
log_entries = [
    0x1A2B0010,
    0x2C4D0085,
    0x3E6F0040,
    0x4A8C00AA,
    0x5B9D0030
]

energy_threshold = calculate_efficiency(log_entries)
print(f"Result: {energy_threshold}")