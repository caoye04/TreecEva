from itertools import compress

# Simulate sensor data with timestamped readings
timestamps = list(range(10, 91, 10))  # 10 to 90 in steps of 10
data_readings = [98.1, 107.4, 92.3, 115.6, 99.2, 101.8, 93.4, 104.7, 96.9]

# Irrelevant auxiliary variable (minor distraction)
status_flags = [True, False, True, True, False, True, False, True, True]

# Extract every other reading starting from index 0
even_index_readings = data_readings[::2]

# Reverse the selected elements for chronological backtracking
reversed_elements = even_index_readings[::-1]

# Sum every second element from the reversed list starting at index 1
filtered_sum = sum(reversed_elements[1::2])

# Print result as required
print(f"Result: {filtered_sum}")