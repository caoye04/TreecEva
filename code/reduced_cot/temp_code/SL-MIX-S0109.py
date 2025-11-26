def calculate_performance(values, adjustments, cutoff):
    threshold = cutoff * 2
    filtered_values = [v for v in values if v > threshold]
    adjustment_factors = [adj * 0.5 for adj in adjustments[:len(filtered_values)]]
    final_metric = sum([x**2 - y for x, y in zip(filtered_values, adjustment_factors) if x > threshold])
    print(f"Result: {final_metric}")

# Main execution
performance_data = [8, 12, 5, 15, 3, 20]
adjustment_values = [4, 6, 2, 8, 1, 10]
base_cutoff = 7

calculate_performance(performance_data, adjustment_values, base_cutoff)