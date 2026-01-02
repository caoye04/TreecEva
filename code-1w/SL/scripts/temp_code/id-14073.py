def calculate_performance(data):
    processed = [float(x.split(':')[1]) for x in data if 'active' in x]
    averages = [sum(processed[i:i+2]) / len(processed[i:i+2]) for i in range(0, len(processed), 2)]
    scaling_factor = 1.5 if len(averages) > 2 else 1.2
    adjusted = [val * scaling_factor for val in averages]
    return int(sum(adjusted))

# Irrelevant auxiliary data (minimal distraction)
status_flags = ['enabled', 'disabled', 'active', 'inactive']
metadata_log = {'version': '2.1', 'mode': 'diagnostic'}

benchmark_data = [
    'moduleA:active:value:85.0',
    'moduleB:active:value:90.0',
    'moduleC:inactive:value:78.0',
    'moduleD:active:value:92.0',
    'moduleE:active:value:88.0'
]

# Key computation
extracted_values = [entry for entry in benchmark_data if 'active' in entry]
final_score = calculate_performance(extracted_values)
print(f'Result: {final_score}')