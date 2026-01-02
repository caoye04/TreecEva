def evaluate_performance(log_entries):
    char_count = lambda s: sum(1 for c in s if c.isalpha())
    
    total_chars = 0
    error_count = 0
    bonus = 0
    
    for entry in log_entries:
        if 'ERROR' in entry:
            error_count += 1
        total_chars += char_count(entry)
    
    base_score = total_chars - (error_count * 10)
    
    if error_count == 0 and total_chars > 50:
        bonus = 25
    
    final_score = base_score + bonus
    return final_score

# Simulated system log entries
log_data = [
    "INFO: System started successfully",
    "DEBUG: Initializing connection pool",
    "ERROR: Failed to connect to database",
    "INFO: Retrying connection...",
    "INFO: Connection established"
]

# Execution point
final_score = evaluate_performance(log_data)
print(f"Result: {final_score}")