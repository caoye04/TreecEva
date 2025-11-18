import math

def compute_slope_angle(elevation_diff, distance):
    return math.degrees(math.atan(elevation_diff / distance))

def gcd_of_list(numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
        if result == 1:
            break
    return result

elevation_data = [120, 180, 300, 420, 600, 840]
distance_intervals = [10, 15, 20, 30, 40, 60]
slope_threshold = 45.0
peak_heights_in_steep_regions = []

for idx in range(len(elevation_data)-1):
    diff = elevation_data[idx+1] - elevation_data[idx]
    dist = distance_intervals[idx]
    angle = compute_slope_angle(diff, dist)
    
    if angle >= slope_threshold and diff > 0:
        peak_heights_in_steep_regions.append(elevation_data[idx+1])

sorted_peaks = sorted(peak_heights_in_steep_regions, reverse=True)
steep_region_gcd = gcd_of_list(sorted_peaks)

final_gcd_result = steep_region_gcd if steep_region_gcd > 0 else -1
print(f"Result: {final_gcd_result}")