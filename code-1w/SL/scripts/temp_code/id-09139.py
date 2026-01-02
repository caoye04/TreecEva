system_active = True
startup_time = 12
performance_score = 984
latency_factor = 7

diagnostic_log = "System boot successful. Latency: 7ms"
log_entries = diagnostic_log.split('. ')

# Key computation with conditional expression and string analysis
detected_issues = len([entry for entry in log_entries if "Error" in entry])
performance_score -= detected_issues * 100

# Conditional assignment based on system status
efficiency_ratio = performance_score / (latency_factor + 1) if system_active else 0

# Additional unrelated metric (minor distraction)
reliability_index = (len(log_entries) + startup_time) % 5

Result: efficiency_ratio