from itertools import compress

def calculate_phase(data, limit):
    filtered = [x % 13 for x in data if x > limit]
    doubled = [x * 2 for x in filtered]
    rolled = doubled[-3:] + doubled[:-3]  # Right rotation by 3
    return sum(rolled[::2])

# Sensor signal processing simulation
timestamps = [117, 204, 99, 312, 415, 58, 69, 73]
signal_data = [t % 25 for t in timestamps]
baseline = 10
threshold = 7

# Irrelevant auxiliary variable (minimal distraction)
status_flags = list(compress(range(len(signal_data)), [x > 5 for x in signal_data]))

phase_shift = calculate_phase(signal_data, threshold)
print(f"Result: {phase_shift}")