temperature_readings = [15.2, 16.8, 18.1, 20.5, 22.3, 25.7]
new_reading = 27.4

# Process new reading
def find_insertion_point(sorted_list, value):
    low, high = 0, len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low

insertion_index = find_insertion_point(temperature_readings, new_reading)
is_extreme = insertion_index == len(temperature_readings)

print(f"Result: {int(is_extreme)}")