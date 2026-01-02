def analyze_network_load():
    # Simulated network traffic data (packets per second)
    base_traffic = [120, 150, 130, 170, 200, 220, 190, 210]
    maintenance_mode = False
    threshold_limit = 180

    # Peak hour indices (simulate time slots 4-6 as high traffic)
    peak_hours = {4, 5, 6}
    off_peak_reduction = set([1, 2, 3]).difference({0})

    # Augment traffic with weather impact (simulated sensor input)
    weather_factor = 1.1  # Slight congestion due to rain
    adjusted_traffic = [int(x * weather_factor) for x in base_traffic]

    # Redundant diagnostic logging (distractor)
    diagnostics = []
    for i, val in enumerate(adjusted_traffic):
        if val > threshold_limit:
            diagnostics.append(f"High load at {i}: {val}pps")

    # Apply peak hour multiplier using set membership check
    enhanced_traffic = []
    for i in range(len(adjusted_traffic)):
        if i in peak_hours:
            enhanced_traffic.append(adjusted_traffic[i] * 1.25)
        else:
            enhanced_traffic.append(adjusted_traffic[i] * 0.9)

    # Simulate packet loss compensation (irrelevant to final result)
    packet_loss_rate = 0.02
    compensation_buffer = sum(enhanced_traffic) * packet_loss_rate / len(enhanced_traffic)

    # Critical function definition embedded to increase nesting
    def calculate_bandwidth(traffic, peaks):
        total = 0
        peak_contribution = 0
        base_contribution = 0

        for idx, rate in enumerate(traffic):
            if idx in peaks:
                scaled = int(rate * 1.15)  # Additional QoS scaling during peak
                peak_contribution += scaled
                total += scaled
            else:
                normal = int(rate * 0.95)
                base_contribution += normal
                total += normal

                # Early termination for anomaly detection (unused path)
                if normal > 300:
                    return -1

        # Final bandwidth computed in Mbps (conversion factor)
        final_mbps = total // 100
        return final_mbps

    # Extraneous state tracking (distractor)
    system_health = "nominal"
    uptime_minutes = 1440
    config_version = "v2.1-alpha"

    # Key computation
    final_bandwidth = calculate_bandwidth(enhanced_traffic, peak_hours)
    
    # Print required output
    print(f"Result: {final_bandwidth}")
    
    return final_bandwidth

# Execute function
analyze_network_load()