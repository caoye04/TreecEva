def analyze_efficiency(metrics):
    efficiency = 0
    temp_factor = 0
    for m in metrics:
        if m > 50:
            efficiency += m * 0.3
        else:
            efficiency -= m * 0.1
    return efficiency


def extract_key_signals(raw_data):
    signals = []
    buffer = []
    for item in raw_data:
        cleaned = item.strip().lower()
        if 'error' not in cleaned and len(cleaned) > 2:
            signals.append(len(cleaned))
    return signals


def evaluate_performance(log_entries):
    cycle_data = []
    total_length = 0
    phantom_sum = 0  # Distractor variable
    
    for entry in log_entries:
        total_length += len(entry)
        if entry.isdigit():
            cycle_data.append(int(entry))
        elif 'cycle' in entry.lower():
            parts = entry.split(':')
            if len(parts) > 1:
                numeric_part = ''.join(filter(str.isdigit, parts[1]))
                if numeric_part:
                    cycle_data.append(int(numeric_part))
    
    # Irrelevant transformation (distractor)
    adjusted_cycle = [x + 1 for x in cycle_data if x % 2 == 0]
    phantom_sum = sum(adjusted_cycle) * 0.1
    
    # Core logic begins
    base_score = sum(cycle_data) * 0.5
    deviation = 0
    for val in cycle_data:
        if val > 30:
            deviation += (val - 30) * 0.2
    
    # Secondary adjustment
    if len(cycle_data) > 4:
        base_score -= len(cycle_data) * 1.5
    else:
        base_score += 10
    
    # Final computation
    final_score = int(base_score - deviation + 5)
    
    # Dead code path (misleading)
    if phantom_sum > 1000:
        final_score *= 2
    
    return final_score

# Input data with mixed types
log_input = [
    "System: cycle-78",
    "status_update_123",
    "95",
    "INFO: cycle:45",
    "debug_msg",
    "67",
    "Data packet received"
]

# Extract and process (irrelevant to final result but adds cognitive load)
data_metrics = [len(x) for x in log_input]
useless_efficiency = analyze_efficiency(data_metrics)
signals = extract_key_signals(log_input)

# Key execution point
cycle_data = [78, 45, 67]  # Derived implicitly through parsing above
def evaluate_performance(log_entries):  # Re-definition for clarity in flow
    cycle_data = []
    total_length = 0
    phantom_sum = 0
    for entry in log_entries:
        total_length += len(entry)
        if entry.isdigit():
            cycle_data.append(int(entry))
        elif 'cycle' in entry.lower():
            parts = entry.split(':')
            if len(parts) > 1:
                numeric_part = ''.join(filter(str.isdigit, parts[1]))
                if numeric_part:
                    cycle_data.append(int(numeric_part))
    adjusted_cycle = [x + 1 for x in cycle_data if x % 2 == 0]
    phantom_sum = sum(adjusted_cycle) * 0.1
    base_score = sum(cycle_data) * 0.5
    deviation = 0
    for val in cycle_data:
        if val > 30:
            deviation += (val - 30) * 0.2
    if len(cycle_data) > 4:
        base_score -= len(cycle_data) * 1.5
    else:
        base_score += 10
    final_score = int(base_score - deviation + 5)
    if phantom_sum > 1000:
        final_score *= 2
    return final_score

result = evaluate_performance(log_input)
print(f"Result: {result}")