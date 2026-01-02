from itertools import compress, count

def analyze_demand(patterns):
    peak = max(patterns)
    avg = sum(patterns) / len(patterns)
    volatility = (peak - avg) / avg if avg else 0
    return peak, volatility

def calculate_efficiency(runs):
    total_ops = sum(runs)
    effective_ops = sum(x * 0.9 for x in runs if x > 100) + sum(x * 0.6 for x in runs if x <= 100)
    efficiency = effective_ops / total_ops if total_ops else 0
    return efficiency

def simulate_failure_modes(loads):
    failures = []
    for load in loads:
        if load > 950:
            failures.append(load * 0.02)
    return sum(failures)

def adjust_capacity(base, factor):
    adjusted = base * factor
    if adjusted < 500:
        adjusted = 500
    elif adjusted > 2000:
        adjusted = 2000
    return round(adjusted)

def main():
    # Realistic system load data (in MW)
    hourly_loads = [420, 560, 610, 700, 890, 950, 930, 880, 720]
    maintenance_cycles = [120, 80, 150, 90]
    stress_tests = [1020, 980, 1100]

    # Distractor: Irrelevant computation on maintenance
    avg_maintenance_duration = sum(maintenance_cycles) / len(maintenance_cycles)
    total_maintenance_impact = avg_maintenance_duration * 0.15

    # Key data processing
    peak_demand, fluctuation = analyze_demand(hourly_loads)
    
    # Simulate system responses under stress
    all_runs = hourly_loads + stress_tests
    efficiency_factor = calculate_efficiency(all_runs)
    
    # Distractor: Failure simulation not used in final calculation
    expected_downtime = simulate_failure_modes(stress_tests)
    recovery_cost_estimate = expected_downtime * 500

    # Auxiliary tracking (semi-relevant)
    growth_projector = count(peak_demand, 50)
    projected_peaks = [next(growth_projector) for _ in range(3)]  # [950, 1000, 1050]

    # Determine base load with safety margin
    base_load = peak_demand * 1.1

    # Adjust base load based on efficiency
    final_capacity = adjust_capacity(base_load, efficiency_factor)

    # Distractor: Unused optimization path
    temp_buffer = {i: x * 0.1 for i, x in enumerate(hourly_loads) if x > 600}
    compression_mask = [x > 700 for x in hourly_loads]
    filtered_loads = list(compress(hourly_loads, compression_mask))

    # Final result output
    print(f"Result: {final_capacity}")

if __name__ == "__main__":
    main()