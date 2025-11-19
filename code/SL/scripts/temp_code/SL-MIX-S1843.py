import statistics

def hex_to_int_list(hex_string):
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def compute_security_flags(packet_sizes):
    flags = 0
    for size in packet_sizes:
        if size > 128:
            flags |= 1 << 0  # Large packet flag
        if size % 4 == 0:
            flags |= 1 << 1  # Alignment flag
        if size < 32:
            flags |= 1 << 2  # Small packet flag
    return flags

# Network traffic data (hex encoded)
traffic_log = "4142434445464748494a4b4c4d4e4f505152535455565758595a"

# Process traffic data
packet_data = hex_to_int_list(traffic_log)

# Compute statistical profile
mean_size = statistics.mean(packet_data)
variance = statistics.variance(packet_data)

# Apply security analysis
security_flags = compute_security_flags(packet_data)

# Calculate final anomaly score using statistical variance and security flags
anomaly_score = int(variance) ^ (security_flags & 0xFF)

print(f"Result: {anomaly_score}")