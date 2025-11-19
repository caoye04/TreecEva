from collections import defaultdict
import statistics

def process_audio_signal(readings):
    # Stage 1: Apply lambda filter for outlier removal
    filtered_readings = list(filter(lambda x: abs(x - statistics.mean(readings)) < 2 * statistics.stdev(readings), readings))
    
    # Stage 2: Group readings by magnitude using defaultdict
    magnitude_groups = defaultdict(list)
    for reading in filtered_readings:
        magnitude = int(abs(reading) // 10)
        magnitude_groups[magnitude].append(reading)
    
    # Stage 3: Process groups with switch-like logic
    processed_values = []
    for mag, values in magnitude_groups.items():
        # Simulate switch-case with dictionary mapping
        case_handler = {
            0: lambda v: sum(v) / len(v),
            1: lambda v: max(v) - min(v),
            2: lambda v: statistics.variance(v) if len(v) > 1 else 0,
            3: lambda v: sum(x**2 for x in v),
        }
        handler = case_handler.get(mag, lambda v: sum(v))
        processed_values.append(handler(values))
    
    # Stage 4: Final aggregation with list comprehension
    squared_deviations = [(x - statistics.mean(processed_values)) ** 2 for x in processed_values]
    processed_signal_strength = sum(squared_deviations) / len(squared_deviations) if squared_deviations else 0
    
    return processed_signal_strength

# Input data representing amplitude readings
amplitude_readings = [12.5, -8.3, 45.2, 15.7, -42.1, 9.8, 10.2, 11.1, -9.5, 50.0, 13.4, -7.6]

# Execute processing pipeline
final_result = process_audio_signal(amplitude_readings)
print(f"Result: {final_result}")