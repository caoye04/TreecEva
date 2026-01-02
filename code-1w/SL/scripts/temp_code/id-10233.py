def calculate_performance(data):
    # Preprocessing: filter valid entries and normalize names
    valid_entries = [d for d in data if d['status'] == 'active']
    normalized_names = [name.strip().lower().replace(' ', '_') for name in data[0]['aliases']]

    # Irrelevant string transformation (distractor)
    encoded_name = ''.join([chr(ord(c) + 1) for c in normalized_names[0]])
    temp_checksum = sum([ord(c) for c in encoded_name]) % 100

    # Extract metrics with conditional logic
    response_times = []
    success_count = 0
    for entry in valid_entries:
        rt = entry['response_time']
        if rt < 500:
            response_times.append(rt)
            if entry['success']:
                success_count += 1
        else:
            # Simulate fallback processing (not used)
            backup_flag = True
            adjusted_rt = rt * 0.95  # dead computation

    # Distractor: unused dictionary operations
    metadata_map = {i: len(name) for i, name in enumerate(normalized_names)}
    avg_length = sum(metadata_map.values()) / len(metadata_map)

    # Core logic: compute performance score
    if response_times:
        avg_response = sum(response_times) / len(response_times)
        success_rate = success_count / len(valid_entries)
        efficiency_bonus = 10 if avg_response < 300 else 5
    else:
        avg_response = 0
        success_rate = 0
        efficiency_bonus = 0

    # Final scoring with multiple factors
    base_score = success_rate * 100
    time_penalty = 50 * (avg_response / 1000)  # scales with slowness
    final_score = base_score - time_penalty + efficiency_bonus

    return final_score

# Input data
benchmark_data = [
    {
        'id': 'A1',
        'status': 'active',
        'response_time': 250,
        'success': True,
        'aliases': ['Module Alpha', 'Core Engine']
    },
    {
        'id': 'B2',
        'status': 'inactive',
        'response_time': 450,
        'success': True,
        'aliases': ['Beta Runner']
    },
    {
        'id': 'C3',
        'status': 'active',
        'response_time': 320,
        'success': True,
        'aliases': ['Gamma Unit']
    },
    {
        'id': 'D4',
        'status': 'active',
        'response_time': 600,
        'success': False,
        'aliases': ['Delta Node']
    }
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")