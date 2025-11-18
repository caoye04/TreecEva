from collections import defaultdict
import statistics

def find_outliers(sorted_data, threshold):
    outliers = []
    n = len(sorted_data)
    for i in range(n):
        # Binary search for left boundary
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if sorted_data[mid] < sorted_data[i] - threshold:
                left = mid + 1
            else:
                right = mid - 1
        left_bound = left
        
        # Binary search for right boundary
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if sorted_data[mid] > sorted_data[i] + threshold:
                right = mid - 1
            else:
                left = mid + 1
        right_bound = right
        
        # Count neighbors within threshold
        count = right_bound - left_bound + 1
        if count < 0.1 * n:  # Less than 10% of data points are neighbors
            outliers.append(sorted_data[i])
    return outliers

# Climate station temperature readings (in Celsius)
temperature_readings = [22.1, 23.4, 22.8, 56.2, 21.9, 23.1, 22.5, 23.0, 22.7, 23.3, 22.9, 23.2, -15.3, 22.6, 23.5]
sorted_temps = sorted(temperature_readings)
outlier_values = find_outliers(sorted_temps, 5.0)

# Remove outliers using set operations
original_set = set(temperature_readings)
outlier_set = set(outlier_values)
cleaned_temps = list(original_set - outlier_set)

# Calculate adjusted variance
adjusted_variance = statistics.variance(cleaned_temps)
print(f"Result: {adjusted_variance}")