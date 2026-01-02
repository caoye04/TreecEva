def calculate_final_score(records):
    total_points = 0
    penalties = set()
    
    for entry in records.split(','):
        cleaned = entry.strip().lower()
        if 'error' in cleaned:
            penalties.add(len(cleaned))
        elif 'warning' in cleaned:
            continue
        else:
            total_points += len(cleaned)
    
    adjustment = sum(penalties) if penalties else 0
    return total_points - adjustment

# Irrelevant utility function (minimal distraction)
def format_timestamp(ts):
    return f"[LOG] {ts}"

# Main data input
data = "UserLogin, error_404, DataSaved, warning_low_memory, SystemReady"
final_score = calculate_final_score(data)
print(f"Result: {final_score}")