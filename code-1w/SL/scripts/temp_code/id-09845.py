def calculate_performance(log):
    entries = log.split(',')
    results = {}
    
    for entry in entries:
        key, value = entry.strip().split(':')
        results[key] = int(value)
    
    passed = results.get('passed', 0)
    total = results.get('total', 1)
    efficiency = results.get('efficiency', 100)
    
    # Compute score as weighted performance
    base_score = (passed / total) * 100
    adjusted_score = base_score * (efficiency / 100.0)
    
    bonus = 10 if passed == total else 0
    final_score = adjusted_score + bonus
    
    return final_score

# Irrelevant utility function (minimal distraction)
def format_timestamp(ts):
    return f"[LOG]-{ts}"

# Main execution
log_data = "passed:8,total:10,efficiency:95"
final_score = calculate_performance(log_data)
print(f"Result: {final_score}")