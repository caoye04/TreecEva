def main():
    # Simulate sensor readings and threshold deviations
    readings = [104, 95, 110, 88, 98]
    threshold = 100
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]

    # Compute absolute deviation from threshold
    deviation_map = list(map(lambda x: abs(x - threshold), readings))

    # Irrelevant distractor: unused transformation
    squared_readings = [x**2 for x in readings]

    # Function to compute weighted total score
    def calculate_total(devs):
        sorted_devs = sorted(devs)  # Sort deviations
        trimmed = sorted_devs[1:-1]  # Remove highest and lowest
        weighted_sum = sum(w * d for w, d in zip(weights, trimmed))
        return round(weighted_sum, 3)

    final_score = calculate_total(deviation_map)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()