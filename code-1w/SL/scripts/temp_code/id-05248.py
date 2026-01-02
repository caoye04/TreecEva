def calculate_final_score(log_entries):
    score = 0
    penalties = {'timeout': 3, 'retry': 2, 'fail': 5}
    status_map = {k: v for v, k in enumerate('ABCDE')}
    
    for entry in log_entries:
        tokens = entry.split('|')
        event_type = tokens[1].strip().lower()
        status_char = tokens[2].strip()
        
        if event_type in penalties:
            score += penalties[event_type]
        
        if status_char in status_map and status_map[status_char] < 3:
            score += 1
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_result = [x.upper() for x in log_entries if 'retry' in x]
    
    normalized_score = max(0, 50 - score)
    final_score = int(normalized_score * 1.5)  # Apply scaling
    return final_score

# Main execution
log_data = [
    "ERR|timeout|B",
    "NET|retry|C",
    "SYS|ok|A",
    "IO|fail|E",
    "NET|retry|B"
]

result_var = sum(len(x) for x in log_data)  # Slight distraction
final_score = calculate_final_score(log_data)
print(f"Target result: {final_score}")