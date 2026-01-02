from itertools import compress

# Simulate sensor data and quality flags
def main():
    raw_data = [105, 210, 98, 0, 157, 301, 250, 0, 190, 88]
    data_flags = [True, True, True, False, True, False, True, False, True, True]

    # Threshold logic for acceptable readings
    threshold_function = lambda x: 50 <= x <= 250

    # Filter valid data based on flags and threshold
    filtered_by_flag = list(compress(raw_data, data_flags))
    filtered_by_threshold = list(filter(threshold_function, filtered_by_flag))

    # Scoring function: average of remaining valid readings
    def calculate_filtration(data, condition):
        if not data:
            return 0
        passed = [x for x in data if condition(x)]
        return sum(passed) / len(passed) if passed else 0

    filtration_score = calculate_filtration(raw_data, threshold_function)
    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main()