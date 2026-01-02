def analyze_productivity(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_buffer = []
    efficiency_sum = 0.0

    for log in logs:
        if not log.strip():
            continue
        parts = log.split(',')
        if len(parts) < 3:
            continue
        
        status = parts[0].strip()
        duration_str = parts[1].strip()
        priority = parts[2].strip()
        
        # Irrelevant string processing (distractor)
        cleaned_priority = priority.upper().replace('HIGH', 'URGENT').replace('LOW', 'NORMAL')
        temp_buffer.append(cleaned_priority)
        
        try:
            duration = float(duration_str)
        except ValueError:
            duration = 0.0

        if status == "completed" and duration > 0:
            valid_count += 1
            efficiency_sum += 1 / duration  # higher efficiency for shorter durations

    avg_efficiency = efficiency_sum / valid_count if valid_count else 0.0
    return total_entries, valid_count, avg_efficiency, temp_buffer


def evaluate_performance(metrics, base_factor):
    total, valid, efficiency, _ = metrics
    if valid == 0:
        return 0
    
    # Complex weighting with some red herring calculations
    saturation_level = total / (valid + 1)  # artificial dampener
    adjustment = 1 + (base_factor * 0.1)
    raw_score = valid * efficiency * adjustment
    
    # Distractor: unused intermediate values
    theoretical_max = total * 100
    overhead_penalty = len(str(theoretical_max)) * 0.05
    
    final_score = int(raw_score + 0.5)  # round to nearest integer
    return final_score

# Simulated system logs (real data)
logs_data = [
    "completed, 2.5, high",
    "failed, 1.0, low",
    "completed, 0.8, medium",
    "completed, 3.2, high",
    "",  # empty entry
    "completed, 1.1, low",
    "completed, 0.9, high",
    "invalid_entry"  # malformed
]

# Extraneous variable (distraction)
config_settings = {"timeout": 30, "retries": 3, "debug_mode": False}

# Core analysis pipeline
task_metrics = analyze_productivity(logs_data)
efficiency_factor = 2.0

# Key statement
final_score = evaluate_performance(task_metrics, efficiency_factor)

# Unused computation path (dead code - distractor)
if config_settings["debug_mode"]:
    debug_trace = [x for x in range(10) if x % 2 == 0]
    print("Debug trace:", debug_trace)

print(f"Result: {final_score}")