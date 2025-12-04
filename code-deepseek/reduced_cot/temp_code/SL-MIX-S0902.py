def calculate_data_points():
    raw_data = [12, 8, 15, 6, 20, 3, 18]
    filtered_points = [x for x in raw_data if x > 10]
    result = sum(filtered_points) // len(filtered_points)
    adjustment = min(raw_data) + 2
    final_value = result * 2 - adjustment
    print(f"Target result: {final_value}")

calculate_data_points()