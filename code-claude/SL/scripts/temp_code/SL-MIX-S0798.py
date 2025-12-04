def parse_log_timestamp(timestamp):
    # Parse timestamp in format 'HH:MM:SS'
    parts = timestamp.split(':')
    if len(parts) != 3:
        return -1
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        
        # Validate time components
        if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
            return hours * 3600 + minutes * 60 + seconds
        return -1
    except ValueError:
        return -1

def is_valid_entry(entry):
    # Check if log entry follows the correct format and occurred during business hours (9:00-17:00)
    if not entry or len(entry.strip()) < 10:
        return False
    
    # Extract timestamp from the beginning of the log entry
    timestamp = entry[:8]
    seconds = parse_log_timestamp(timestamp)
    
    if seconds == -1:
        return False
    
    # Business hours: 9:00 (32400 seconds) to 17:00 (61200 seconds)
    business_start = 9 * 3600
    business_end = 17 * 3600
    
    # Check if timestamp is within business hours
    is_business_hours = business_start <= seconds < business_end
    
    # Calculate priority score (not used for validation)
    priority_score = 0
    if 'ERROR' in entry:
        priority_score = 3
    elif 'WARNING' in entry:
        priority_score = 2
    elif 'INFO' in entry:
        priority_score = 1
    
    # Check if entry contains required fields
    has_required_fields = '[' in entry and ']' in entry
    
    return is_business_hours and has_required_fields

# Sample log entries
log_entries = [
    '08:30:00 [SERVER] System startup',           # Before business hours
    '09:15:22 [DATABASE] Connected successfully',   # Valid
    '10:45:16 [AUTH] WARNING: Failed login attempt', # Valid
    '12:32:45 [API] Request processed',             # Valid
    '14:05:32 [NETWORK] ERROR: Connection timeout',  # Valid
    '15:45:00 [SERVER] INFO: Cache cleared',        # Valid
    '17:05:18 [DATABASE] Backup completed',         # After business hours
    '11:23:XX [AUTH] User login',                   # Invalid timestamp
    '13:40:30 SERVER: Status check'                 # Missing required brackets
]

# Process entries with different methods
total_entries = len(log_entries)
error_count = len([e for e in log_entries if 'ERROR' in e])
warning_count = len([e for e in log_entries if 'WARNING' in e])

# Calculate statistics (not used in final result)
avg_entry_length = sum(len(e) for e in log_entries) / total_entries if total_entries > 0 else 0
max_entry_length = max(len(e) for e in log_entries) if log_entries else 0

# Count valid entries (those within business hours and with correct format)
valid_entries = sum(1 for i in range(len(log_entries)) if is_valid_entry(log_entries[i]))

# Final processing
processed_ratio = (valid_entries / total_entries) * 100 if total_entries > 0 else 0

print(f"Result: {valid_entries}")