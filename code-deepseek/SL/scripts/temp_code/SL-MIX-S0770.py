def process_data_log(log_content):
    # Parse log entries and extract relevant data
    entries = log_content.strip().split('\n')
    total_records = len(entries)
    
    # Distractor: Process timestamps (irrelevant to main logic)
    timestamp_list = []
    for entry in entries:
        if '|' in entry:
            parts = entry.split('|')
            if len(parts) > 1:
                timestamp_list.append(parts[0].strip())
    
    # Distractor: Analyze error codes (misleading computation)
    error_codes = []
    for entry in entries:
        if 'ERROR' in entry:
            error_part = entry.split('ERROR')[-1].strip()
            error_codes.append(len(error_part))
    
    # Main logic: Validate entries based on specific criteria
    valid_entries = []
    for entry in entries:
        if '|' in entry and 'COMPLETED' in entry:
            data_parts = entry.split('|')
            if len(data_parts) >= 3:
                status_field = data_parts[2].strip()
                if status_field.isalpha() and len(status_field) > 2:
                    valid_entries.append(entry)
    
    # Distractor: Calculate average error length (dead code path)
    avg_error_length = sum(error_codes) // len(error_codes) if error_codes else 0
    
    # Critical computation: Calculate data quality score
    data_quality_score = (len(valid_entries) * 100) // total_records
    
    # Final result
    print(f"Result: {data_quality_score}")

# Sample log data (deterministic input)
log_data = """
2024-01-15 10:30:00 | USER_LOGIN | COMPLETED
2024-01-15 10:31:15 | DATA_UPLOAD | FAILED | ERROR: Connection timeout
2024-01-15 10:32:30 | FILE_PROCESS | COMPLETED
2024-01-15 10:33:45 | USER_LOGOUT | COMPLETED
2024-01-15 10:34:20 | BACKUP_TASK | FAILED | ERROR: Insufficient space
2024-01-15 10:35:10 | DATA_SYNC | COMPLETED
"""

process_data_log(log_data)