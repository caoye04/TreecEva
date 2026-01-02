from collections import defaultdict, Counter
import math

# Simulated health monitoring system with sensor fusion and noise filtering

def collect_sensor_data():
    return {
        'temp': [36.8, 37.1, 37.2, 36.9, 38.0, 37.0],
        'pulse': [72, 75, 78, 80, 82, 74],
        'resp_rate': [16, 18, 17, 19, 20, 16],
        'oxygen': [98, 97, 96, 98, 95, 97]
    }

def apply_noise_filter(data_list):
    # Irrelevant smoothing function (not used in final computation)
    return [x * 0.98 for x in data_list]

def compute_trend(values):
    if len(values) < 2:
        return 0
    return sum(values[-3:]) / 3 - sum(values[:3]) / 3

def classify_risk(trend, mean_val, threshold_low, threshold_high):
    if mean_val > threshold_high or trend > 1.0:
        return 'high'
    elif mean_val < threshold_low or trend < -1.0:
        return 'low'
    else:
        return 'normal'

def calculate_entropy(values):
    # Distractor: computes entropy of distribution (not used in final logic)
    counts = Counter([round(v, 1) for v in values])
    total = len(values)
    probs = [count / total for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs)

def validate_consistency(data):
    # Dead code path — never actually called
    for key, values in data.items():
        if len(set(map(type, values))) > 1:
            return False
    return True

def merge_readings(sensor_data):
    merged = {}
    for k, v in sensor_data.items():
        merged[k] = {
            'mean': sum(v) / len(v),
            'trend': compute_trend(v),
            'variance': sum((x - sum(v)/len(v))**2 for x in v) / len(v),
            'entropy': calculate_entropy(v)  # Computed but unused
        }
    return merged

def generate_report_card(metrics):
    # Unused reporting function (red herring)
    report = defaultdict(str)
    for param, vals in metrics.items():
        score = int((vals['mean'] - 36) * 10) if param == 'temp' else int(vals['mean'])
        report[param] = f'Score: {score}'
    return report

def analyze_anomaly_score(metrics):
    # Decoy analysis with complex logic but no impact on result
    score = 0
    for param, m in metrics.items():
        if m['variance'] > 2.0:
            score += 10
        if abs(m['trend']) > 0.5:
            score += 5
    adjusted = max(0, score - 15)
    normalized = round(adjusted / 2, 2)
    return normalized  # Never used

def process_metrics(data, limits):
    fused = merge_readings(data)
    
    # Irrelevant set operations (distractors)
    all_params = set(fused.keys())
    critical_params = {'temp', 'oxygen'}
    secondary_params = {'pulse', 'resp_rate'}
    cross_check = all_params & critical_params | secondary_params
    
    risk_levels = {}
    for param in fused:
        mean_val = fused[param]['mean']
        trend_val = fused[param]['trend']
        low, high = limits[param]
        risk_levels[param] = classify_risk(trend_val, mean_val, low, high)
    
    # Core logic disguised among distractions
    temp_deviation = abs(fused['temp']['mean'] - 37.0)
    oxygen_trend = fused['oxygen']['trend']
    pulse_variability = fused['pulse']['variance']
    
    # Real decision logic buried here
    if risk_levels['temp'] == 'high' and oxygen_trend < 0:
        base_score = 85 + int(temp_deviation * 10)
    elif risk_levels['oxygen'] == 'low':
        base_score = 40 - int(abs(oxygen_trend) * 15)
    else:
        base_score = 72 + int(pulse_variability * 2)
    
    # Final transformation using conditional expression
    adjustment = 1.5 if 'temp' in cross_check and len(cross_check) > 2 else 0.8
    final_score = base_score * adjustment
    
    # Secondary processing chain (misleading intermediate results)
    aggregated_entropy = sum(fused[p]['entropy'] for p in fused)
    stability_index = 100 - aggregated_entropy * 5
    
    # The actual target variable
    final_diagnostic = int(final_score + stability_index * 0.1) % 1000
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_data = collect_sensor_data()
    
    # Unused data transformations
    filtered_data = {k: apply_noise_filter(v) for k, v in raw_data.items()}
    consistency_flag = validate_consistency(raw_data)  # Never computed
    
    thresholds = {
        'temp': (36.0, 37.5),
        'pulse': (60, 100),
        'resp_rate': (12, 20),
        'oxygen': (95, 99)
    }
    
    # Key execution point
    final_diagnostic = process_metrics(raw_data, thresholds)