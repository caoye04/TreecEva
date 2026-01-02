def calculate_peak_usage(bandwidth_fluctuations):
    recent_loads = [x for x in bandwidth_fluctuations if x > 75]
    peak_capacity = 0
    temp_buffer = 1
    for load in sorted(recent_loads, reverse=True):
        temp_buffer *= 2
        if load > 90:
            peak_capacity += load * 1.1
        elif load > 80:
            peak_capacity += load * 1.05
        else:
            peak_capacity += load
        if peak_capacity >= 200:
            break
    return f"Target result: {int(peak_capacity)}"

print(calculate_peak_usage([60, 82, 93, 70, 88, 96, 77]))