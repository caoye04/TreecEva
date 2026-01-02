from collections import defaultdict

# Simulate patient health metrics over time
def analyze_trends(data, limit):
    trends = defaultdict(int)
    volatility = 0
    baseline = data[0] if data else 0
    
    for val in data:
        if val > limit:
            trends['high'] += 1
        elif val < limit:
            trends['low'] += 1
        else:
            trends['stable'] += 1
        volatility += abs(val - baseline)
        baseline = val

    # Irrelevant smoothing calculation (distractor)
    smoothed = sum(data) / len(data) if data else 0
    adjustment = (smoothed * 0.1) if smoothed > 50 else 0
    
    return dict(trends), volatility, adjustment

# Process multiple streams of health data
def process_metrics(records, thresh):
    aggregated = {}
    total_points = 0
    debug_log = []
    
    for key, values in records.items():
        trend_map, flux, adj = analyze_trends(values, thresh)
        score = 0
        
        # Core logic: scoring based on trend distribution
        if trend_map.get('high', 0) > trend_map.get('low', 0):
            score += 10
        if trend_map.get('stable', 0) >= 2:
            score += 5
        
        # Distractor: complex but unused transformation
        inverse_weight = list(map(lambda x: round(1/(x+1), 3), values))
        normalized = [v/thresh for v in values if v > 0]
        entropy_proxy = sum([n*n for n in normalized]) if normalized else 0
        
        aggregated[key] = {
            'score': score,
            'flux': flux,
            'entropy': entropy_proxy
        }
        total_points += score
    
    # Secondary processing with conditional branching
    multiplier = 1
    if total_points > 15:
        multiplier = 2
    elif total_points == 0:
        multiplier = 0
    
    # Final computation - only this matters
    final_score = total_points * multiplier
    
    # Dead code path (never executed under current logic)
    if False:
        fallback = sum([v['flux'] for v in aggregated.values()])
        final_score = int(fallback % 100)
    
    # Unused diagnostic output
    debug_summary = {k: v['score'] for k, v in aggregated.items()}
    
    return final_score

# Input data
health_data = {
    'patient_A': [80, 90, 85, 70],
    'patient_B': [40, 30, 35, 45],
    'patient_C': [60, 60, 55, 65]
}
threshold = 60

# Execute main logic
final_score = process_metrics(health_data, threshold)
print(f"Result: {final_score}")