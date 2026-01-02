def compute_filtration_efficiency(readings):
    threshold = 50
    purity_scores = [r * 1.5 for r in readings]
    high_quality = lambda x: x > threshold
    filtered_purities = [p for p in purity_scores if high_quality(p)]
    baseline = 45.0
    adjustment_factor = 0.9
    adjusted_baseline = baseline * adjustment_factor
    filtration_yield = sum(filtered_purities)
    return filtration_yield

sensor_data = [20, 35, 60, 80, 40]
result = compute_filtration_efficiency(sensor_data)
print(f"Target result: {result}")