def main():
    temperatures = [23.5, 19.0, 25.8, 21.3, 18.7]
    baseline = 20.5
    
    # Calculate deviations from baseline
    deviation_map = list(map(lambda temp: round(temp - baseline, 2), temperatures))
    
    # Filter significant deviations (above threshold)
    significant_devs = [dev for dev in deviation_map if abs(dev) > 2.0]
    
    # Count how many times temperature crossed baseline
    cross_count = 0
    for i in range(1, len(temperatures)):
        if (temperatures[i-1] - baseline) * (temperatures[i] - baseline) < 0:
            cross_count += 1

    # Compute weighted impact of deviations
    weights = [1.0, 0.8, 0.6, 0.4, 0.2]
    weighted_dev = sum(d * w for d, w in zip(deviation_map, weights))

    def calculate_total(devs):
        base_total = sum(devs)
        penalty = len([d for d in devs if d < 0]) * 0.5
        return round(base_total - penalty, 2)

    final_score = calculate_total(deviation_map)
    
    # Irrelevant helper variable (minimal distraction)
    average_temp = sum(temperatures) / len(temperatures)
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()