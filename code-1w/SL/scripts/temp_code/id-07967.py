from collections import Counter

# Simulate sensor reading processing with bit flags and string-based diagnostics
data_stream = ['OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK']
status_counter = Counter(data_stream)
status_count = status_counter['OK']

flow_rate = len(data_stream) * 12.5
flow_rate = int(flow_rate) if flow_rate > 50 else flow_rate

# Bitwise check on odd/even status count and logical thresholding
diagnostic_code = 0b1101
mask_result = diagnostic_code & 0b0101  # Extract bits

# Key decision logic based on both numeric threshold and bit parity
threshold_flag = (flow_rate > 75) and (status_count & 1 == 1)

# Irrelevant string transformation (minimal distraction)
diag_msg = "System nominal" if threshold_flag else "Review required"
diag_msg = diag_msg.lower().replace(" ", "_")

Result: threshold_flag