def calculate_error_metric(transmitted, received):
    if len(transmitted) != len(received):
        return -1
    
    errors = [t ^ r for t, r in zip(transmitted, received)]
    
    # Early return if no errors
    if all(e == 0 for e in errors):
        return 0
    
    # Calculate error positions using bitwise operations
    error_positions = []
    for i, e in enumerate(errors):
        if e & 0xFF:  # Check if any bit is set in the byte
            error_positions.append(i)
    
    # If more than half the packets have errors, break for recalibration
    if len(error_positions) > len(transmitted) // 2:
        return -2
    
    # Calculate aggregate metric using statistical measures
    import statistics
    mean_error = statistics.mean(errors)
    if len(errors) > 1:
        variance_error = statistics.variance(errors)
    else:
        variance_error = 0
    
    # Apply bit shifts for normalization
    normalized_mean = int(mean_error) >> 2
    normalized_variance = int(variance_error) << 1
    
    # Final metric combines mean and variance with XOR
    aggregate_metric = normalized_mean ^ normalized_variance
    
    return aggregate_metric

# Simulate packet transmission
transmitted_packets = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70]
received_packets = [0x1A, 0x2F, 0x3C, 0x49, 0x5E, 0x6B, 0x70]

aggregate_metric = calculate_error_metric(transmitted_packets, received_packets)
print(f"Result: {aggregate_metric}")