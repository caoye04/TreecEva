def calculate_forensic_impact(hour):
    return ((hour << 2) ^ 0x1F) % 17

def process_access_log():
    access_hours = [3, 7, 11, 15, 19, 23]
    hourly_scores = {}
    
    # First pass: Calculate individual scores
    for hr in access_hours:
        score = calculate_forensic_impact(hr)
        hourly_scores[hr] = score
    
    # Second pass: Apply correction using set operations
    prime_hours = frozenset([3, 7, 11, 19])
    even_hours = frozenset([15])
    night_hours = frozenset([23])
    
    adjustment_factor = len(prime_hours.intersection(set(access_hours)))
    
    # Third pass: Compute weighted sum with context manager
    forensic_score = 0
    
    class ScoreTracker:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def add(self, value):
            nonlocal forensic_score
            forensic_score += value
    
    with ScoreTracker() as tracker:
        for hr in sorted(hourly_scores.keys()):
            base = hourly_scores[hr]
            if hr in prime_hours:
                tracker.add(base * 3)
            elif hr in even_hours:
                tracker.add(base << 1)
            else:  # night hours
                tracker.add(base ^ 0xFF)
        
        # Final adjustment
        forensic_score = (forensic_score + adjustment_factor) & 0xFF
    
    return forensic_score

# Execution
forensic_score = process_access_log()
print(f"Result: {forensic_score}")