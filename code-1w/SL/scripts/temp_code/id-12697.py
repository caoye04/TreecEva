def main():
    # Simulate a distributed sensor network node load analysis
    node_readings = [14, 25, 18, 30, 22, 40, 35]
    threshold = 20
    cluster_load = 0
    temp_buffer = []

    # Accumulate loads above threshold (relevant)
    for reading in node_readings:
        if reading > threshold:
            cluster_load += reading * 0.8  # Weighted contribution

    # Irrelevant: Buffer processing for hypothetical smoothing (dead logic)
    for reading in node_readings:
        smoothed = (reading + 5) * 0.9
        temp_buffer.append(round(smoothed))

    # Misleading computation: simulates alternate path not used
    fallback_capacity = sum([x**2 for x in temp_buffer if x > 25]) // 100

    # Higher-order function that's defined but unused (distractor)
    transform = lambda x: x * 1.5 if x < 30 else x * 0.7

    # Actual key computation
    def calculate_efficiency(load, thresh):
        base_eff = load / (thresh + 10)
        adjustment = 0.95 if load > 50 else 1.05
        return int(load * adjustment) + 5

    energy_capacity = calculate_efficiency(cluster_load, threshold)

    # Redundant print for distraction
    print(f"Fallback capacity: {fallback_capacity}")
    print(f"Temp buffer summary: {sum(temp_buffer)}")

    print(f"Result: {energy_capacity}")

if __name__ == "__main__":
    main()