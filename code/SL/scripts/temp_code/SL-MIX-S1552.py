import math
from functools import wraps

call_tracker = {}

def track_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        call_tracker[name] = call_tracker.get(name, 0) + 1
        return func(*args, **kwargs)
    return wrapper

@track_calls
def compute_mean(values):
    return sum(values) / len(values) if values else 0

@track_calls
def compute_variance(values, mean_val):
    return sum((x - mean_val) ** 2 for x in values) / len(values) if values else 0

@track_calls
def find_peak_temp(temperatures):
    peak = float('-inf')
    for temp in temperatures:
        if temp > peak:
            peak = temp
    return peak

@track_calls
def calculate_seasonal_index(temp_readings):
    # Binary search for median-like value
    sorted_temps = sorted(temp_readings)
    n = len(sorted_temps)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_temps[mid-1] + sorted_temps[mid]) / 2
    else:
        median = sorted_temps[mid]
    
    avg_temp = compute_mean(temp_readings)
    temp_variance = compute_variance(temp_readings, avg_temp)
    peak_temperature = find_peak_temp(temp_readings)
    
    # Seasonal index calculation combining multiple factors
    seasonal_factor = (peak_temperature - median) * math.sqrt(temp_variance + 1)
    return int(seasonal_factor)

# Climate data for a 30-day period
monthly_readings = [18, 22, 25, 27, 30, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 42, 41, 40, 39, 38, 37, 35, 33, 30, 28, 26, 24, 22, 20, 19]

seasonal_index = calculate_seasonal_index(monthly_readings)
print(f"Result: {seasonal_index}")