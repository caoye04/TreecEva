from collections import Counter

def process_temperatures(data):
    # Convert all temperatures to Celsius from mixed-case string format
    cleaned_data = []
    for temp_str in data:
        temp_str = temp_str.strip().lower()
        if temp_str.endswith('c'):
            celsius = float(temp_str[:-1])
        elif temp_str.endswith('f'):
            # Convert Fahrenheit to Celsius
            fahrenheit = float(temp_str[:-1])
            celsius = (fahrenheit - 32) * 5.0 / 9.0
        else:
            celsius = 0.0  # default fallback
        cleaned_data.append(round(celsius, 2))

    # Find most frequent temperature reading
    freq_counter = Counter(cleaned_data)
    mode_temp = freq_counter.most_common(1)[0][1]  # frequency of most common

    # Calculate average deviation from mode
    deviations = [abs(t - freq_counter.most_common(1)[0][0]) for t in cleaned_data]
    avg_deviation = sum(deviations) / len(deviations)

    # Final result: sum of mode frequency and average deviation
    result = mode_temp + avg_deviation
    return result

# Input data with mixed units and formatting
temperature_data = ['25C', '77F', '  25.0c ', '86F', '25C', '77.0f']

result = process_temperatures(temperature_data)
print(f"Result: {result}")