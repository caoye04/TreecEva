from itertools import compress

def calculate_performance(base, data):
    # Normalize readings relative to baseline
    normalized = [round(val / base, 3) for val in data]
    
    # Determine which readings meet or exceed baseline
    success_mask = [norm >= 1.0 for norm in normalized]
    
    # Extract successful readings
    successes = list(compress(normalized, success_mask))
    
    # Calculate performance score as average of successful normalized values
    if successes:
        avg_success = sum(successes) / len(successes)
    else:
        avg_success = 0.0
    
    # Weighted contribution: 70% success average, 30% participation rate
    participation_rate = len(successes) / len(data)
    performance = avg_success * 0.7 + participation_rate * 0.3
    
    return round(performance, 3)

# Experimental sensor readings
baseline = 23.5
readings = [24.1, 22.8, 25.6, 23.5, 21.9, 26.3, 20.4, 24.7]

# Irrelevant auxiliary variable (minor distraction)
temp_log = [round(x - baseline, 2) for x in readings]

final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")