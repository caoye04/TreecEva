def analyze_performance(metrics):
    baseline = sum([m * (1.1 ** i) for i, m in enumerate(metrics)])
    adjusted_metrics = [m * 0.95 for m in metrics if m > 75]
    
    # Irrelevant transformation
    noise_filter = set([i for i in range(len(metrics)) if i % 3 == 0])
    filtered_data = [val for idx, val in enumerate(metrics) if idx not in noise_filter]

    peak = max(metrics)
    duration = len(metrics)
    
    # Dummy recursive helper (not used in final result)
    def dampen_signal(x, depth=2):
        if depth == 0 or x < 10:
            return x
        return dampen_signal(x * 0.8, depth - 1)

    # Real computation path
    avg_metric = sum(adjusted_metrics) / len(adjusted_metrics) if adjusted_metrics else 0
    efficiency_ratio = (avg_metric / peak) if peak else 0
    efficiency_log = [efficiency_ratio] + [baseline, duration]

    return efficiency_log


def compute_thermal_rating(log_data):
    base_rating = log_data[0] * 1000
    temporal_factor = (log_data[2] ** 0.5) * 10
    
    # Red herring calculation
    decay_chain = [temporal_factor / (2 ** i) for i in range(1, 5)]
    residual = sum(decay_chain) / 4
    
    # Actual formula
    rating = base_rating + temporal_factor
    
    # Extra state tracking (unused)
    status_flags = {"stable": True, "peak_load": False}
    status_flags["calibrated"] = (rating > 500)
    
    return rating

# Input data
sensor_readings = [88, 92, 76, 85, 94, 80, 72]

# Processing steps
analysis_result = analyze_performance(sensor_readings)

# Key assignment statement
thermal_capacity = compute_thermal_rating(analysis_result)

# Final output
print(f"Result: {thermal_capacity}")