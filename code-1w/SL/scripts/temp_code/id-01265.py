def preprocess_logs(raw):
    processed = []
    for entry in raw:
        if 'ERROR' in entry:
            processed.append(entry.lower().replace('error', 'alert'))
        elif 'WARNING' in entry:
            processed.append(entry.strip().upper())
    return processed

# Irrelevant helper function (decoy)
def validate_checksum(data):
    checksum = 0
    for char in data:
        checksum ^= ord(char) % 256
    return checksum == 42

# Another decoy: unused transformation
def encrypt_sequence(seq):
    return [((x << 2) | (x >> 6)) ^ 0xA5 for x in seq]

# Fake data aggregation (dead path)
class LogAggregator:
    def __init__(self):
        self.counts = {'INFO': 0, 'WARN': 0, 'ERR': 0}
        self.history = []

    def update(self, record):
        pass  # Never used

# Misleading intermediate calculation
temp_offset = sum([i * 2 for i in range(7)])  # evaluates to 42, red herring
scaling_factor = temp_offset / 2  # 21, irrelevant

# Real data pipeline begins
raw_log_data = [
    "ERROR: Disk usage at 95%",
    "INFO: System uptime 12h",
    "WARNING: Temperature rising",
    "ERROR: Failed to read sensor",
    "DEBUG: Polling interval 5s"
]

filtered_logs = [log for log in raw_log_data if 'ERROR' in log or 'WARNING' in log]

def count_severity(lines):
    err_count = 0
    warn_count = 0
    for line in lines:
        if 'ERROR' in line:
            err_count += 1
        if 'WARNING' in line:
            warn_count += 1
    return err_count, warn_count

errors, warnings = count_severity(filtered_logs)

# Bit manipulation distraction
bit_flag = (errors << 3) | warnings
bit_flag = bit_flag ^ 0xFF  # flip bits, unused later

# Core analysis function
lookup_table = {i: (i * i) + (i % 3) for i in range(10)}

def analyze_pattern(entries):
    total_length = 0
    alert_level = 0
    for entry in entries:
        total_length += len(entry)
        if 'alert' in entry or 'ERROR' in entry:
            alert_level += 1
    
    # Key computation: uses string length and alert count
    base_score = total_length // (alert_level or 1)
    
    # Apply lookup using number of errors (not obvious)
    modifier = lookup_table.get(errors, 0)
    
    # Actual answer derived here
    result = base_score * 2 - modifier
    
    # Distractor: unused complex expression
    secondary_metric = (total_length + modifier) / (errors + 1) if errors else 0
    
    return int(result)

# Simulate preprocessing (modifies content but not used directly)
processed_entries = preprocess_logs(raw_log_data)

# Critical assignment — this is the key execution point
final_diagnostic = analyze_pattern(filtered_logs)

# Print final result as required
print(f"Result: {final_diagnostic}")