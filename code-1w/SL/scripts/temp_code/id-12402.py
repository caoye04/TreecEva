def evaluate_performance(log_entries, threshold):
    # Track various metrics (some are distractions)
    total_chars = 0
    valid_records = []
    temp_sum = 0
    debug_flag = False
    
    for entry in log_entries:
        stripped = entry.strip().lower()
        if not stripped.startswith("log:"):
            continue
            
        # Extract message part
        message = stripped[4:].strip()
        total_chars += len(message)
        
        # Count specific keywords (relevant for scoring)
        warning_count = message.count("warning")
        error_count = message.count("error")
        info_count = message.count("info")
        
        # Distraction: unused statistical counters
        char_frequency = {c: message.count(c) for c in set(message) if c.isalpha()}
        avg_char_code = sum(ord(c) for c in message) / len(message) if message else 0
        
        # Only entries with errors or warnings above threshold are valid
        severity = error_count * 3 + warning_count * 2
        if severity >= threshold:
            temp_sum += severity
            valid_records.append((message, severity))
    
    # Secondary loop: process valid records (distraction: could be merged)
    adjustment_factor = 1.0
    if len(valid_records) > 5:
        adjustment_factor = 0.9
    elif len(valid_records) == 0:
        adjustment_factor = 0.0
    
    base_score = temp_sum * 10
    penalty = len([r for r in valid_records if "critical" in r[0]]) * 15
    final_score = int((base_score - penalty) * adjustment_factor)
    
    # Irrelevant transformation (dead-end variable)
    summary_report = " | ".join([f"{s}" for _, s in valid_records[-3:]])
    report_hash = hash(summary_report) % 1000
    
    return final_score

# Input data
log_data = [
    "Log: System initialized successfully - info",
    "Log: Memory usage at 78% - warning",
    "Log: Disk I/O latency high - warning - warning",
    "Log: Network timeout detected - error",
    "Log: User authentication failed - error - warning",
    "Log: Backup completed - info",
    "Log: Database connection lost - error - critical",
    "Log: Retry attempt 1 - warning",
    "Log: Retry attempt 2 - warning",
    "Log: Service restored - info"
]
threshold = 3

final_score = evaluate_performance(log_data, threshold)
print(f"Result: {final_score}")