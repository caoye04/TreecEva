from collections import defaultdict, Counter
import math

def preprocess_records(raw_entries):
    # Irrelevant transformation: convert all names to uppercase (not used in final logic)
    upper_names = [entry['name'].upper() for entry in raw_entries]
    
    # Relevant filtering: only active users with valid readings
    filtered = [e for e in raw_entries if e['status'] == 'active' and e['reading'] > 0]
    
    # Distractor: count occurrences of each device type (not used later)
    device_counter = Counter([f['device'] for f in filtered])
    
    return filtered

def analyze_trends(data):
    daily_avg = defaultdict(float)
    daily_count = defaultdict(int)
    
    for record in data:
        day = record['timestamp'][:8]  # YYYYMMDD
        daily_avg[day] += record['reading']
        daily_count[day] += 1
    
    # Compute averages per day
    for d in daily_avg:
        daily_avg[d] /= daily_count[d]
    
    # Distractor: find max reading day (not used)
    peak_day = max(daily_avg.keys(), key=lambda k: daily_avg[k]) if daily_avg else None
    
    # Sort days chronologically
    sorted_days = sorted(daily_avg.keys())
    trends = []
    for i in range(1, len(sorted_days)):
        change = daily_avg[sorted_days[i]] - daily_avg[sorted_days[i-1]]
        trends.append(change)
    
    return trends, daily_avg

def calculate_final_score(trend_data):
    trends, averages = trend_data
    
    # Base score from average trend
    base_trend = sum(trends) / len(trends) if trends else 0
    
    # Adjustment factor based on volatility
    squared_devs = [(t - base_trend)**2 for t in trends]
    volatility = math.sqrt(sum(squared_devs) / len(squared_devs)) if squared_devs else 0
    
    # Red herring calculation: normalize volatility to 0-1 scale (unused)
    max_possible_vol = 100.0
    normalized_vol = min(volatility / max_possible_vol, 1.0)
    
    # Focus metric: number of positive trend days
    positive_trends = len([t for t in trends if t > 0])
    total_trends = len(trends)
    improvement_rate = positive_trends / total_trends if total_trends else 0
    
    # Final score computation
    stability_bonus = 10 * (1 - normalized_vol)  # This uses normalized_vol but it's capped and indirect
    trend_component = 50 * base_trend
    progress_component = 30 * improvement_rate
    
    # Actual deterministic path:
    # base_trend = 2.0, improvement_rate = 0.75 → final_score = 50*2.0 + 30*0.75 + 10*(something ~0.9) ≈ 100 + 22.5 + 9 = 131.5
    final_score = trend_component + progress_component + stability_bonus
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Simulated dataset
raw_data = [
    {'name': 'sensor_a', 'status': 'active', 'device': 'd1', 'reading': 100, 'timestamp': '202312010800'},
    {'name': 'sensor_b', 'status': 'inactive', 'device': 'd2', 'reading': 150, 'timestamp': '202312010900'},
    {'name': 'sensor_c', 'status': 'active', 'device': 'd1', 'reading': 110, 'timestamp': '202312021000'},
    {'name': 'sensor_d', 'status': 'active', 'device': 'd3', 'reading': 120, 'timestamp': '202312021100'},
    {'name': 'sensor_e', 'status': 'active', 'device': 'd2', 'reading': 140, 'timestamp': '202312031200'},
    {'name': 'sensor_f', 'status': 'active', 'device': 'd1', 'reading': 130, 'timestamp': '202312041300'},
    {'name': 'sensor_g', 'status': 'active', 'device': 'd3', 'reading': 140, 'timestamp': '202312041400'},
    {'name': 'sensor_h', 'status': 'active', 'device': 'd2', 'reading': 160, 'timestamp': '202312051500'}
]

# Processing pipeline
processed_data = preprocess_records(raw_data)
trend_analysis = analyze_trends(processed_data)
final_score = calculate_final_score(trend_analysis)