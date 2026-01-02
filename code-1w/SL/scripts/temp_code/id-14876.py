def compute_security_token():
    # System user IDs and active session IDs
    all_users = set(range(1000, 2000))
    flagged_users = set(range(1000, 1200)) | set(range(1300, 1350))
    valid_ids = all_users - flagged_users

    # Current active sessions
    active_ids = set(range(1250, 1360)) | set(range(1400, 1420))

    # Security threshold based on bitwise properties
    base_threshold = 57
    adjustment = (17 & 23) | 8  # Simple bitwise logic
    threshold = base_threshold + adjustment

    # Core computation with mixed set and bitwise operations
    result = len(valid_ids.intersection(active_ids)) ^ threshold
    
    # Irrelevant logging variable (minor distraction)
    log_entry = f"Processed {len(all_users)} users"
    
    print(f"Result: {result}")

compute_security_token()