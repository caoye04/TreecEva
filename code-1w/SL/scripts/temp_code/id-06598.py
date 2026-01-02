from collections import defaultdict
import math

def analyze_efficiency(logs):
    counts = defaultdict(int)
    for entry in logs:
        if 'ERROR' in entry:
            counts['errors'] += 1
        elif 'WARNING' in entry:
            counts['warnings'] += 1
        if len(entry.strip()) > 0:
            counts['total'] += 1
    return counts

def calculate_stability_index(events):
    # Irrelevant helper function (dead weight)
    if not events:
        return 0.0
    severity_sum = 0
    for e in events:
        if 'CRITICAL' in e:
            severity_sum += 3
        elif 'MAJOR' in e:
            severity_sum += 2
        elif 'MINOR' in e:
            severity_sum += 1
    return round(severity_sum / len(events), 3) if events else 0.0

def evaluate_performance(output_count, volatility):
    base = output_count * 1.5
    penalty = 0
    if volatility > 0.7:
        penalty += 30
    elif volatility > 0.5:
        penalty += 15
    elif volatility > 0.3:
        penalty += 5
    adjusted = base - penalty
    return int(adjusted)

def main():
    # Simulated system telemetry
    system_logs = [
        'INFO: System boot',
        'WARNING: High memory usage',
        'INFO: User login',
        'ERROR: Disk write failed',
        '',
        'WARNING: CPU spike detected',
        'INFO: Scheduled task completed'
    ]
    
    event_timeline = [
        'MINOR: UI lag',
        'MAJOR: API timeout',
        'CRITICAL: Authentication failure',
        'MINOR: Cache miss'
    ]

    # Analyze log patterns
    analysis = analyze_efficiency(system_logs)
    total_entries = analysis['total']
    error_rate = analysis['errors'] / total_entries if total_entries else 0
    warning_rate = analysis['warnings'] / total_entries if total_entries else 0

    # Compute auxiliary metrics (mostly irrelevant)
    stability = calculate_stability_index(event_timeline)
    noise_ratio = sum(1 for c in str(stability) if c.isdigit()) / 5  # Distractor

    # Core productivity signal
    raw_productivity = len([x for x in system_logs if 'INFO' in x and x.strip()])
    data_string = "productivity_log_v1"
    version_digit = int(data_string[-1])  # Minor distraction

    # Risk assessment with string processing
    risk_indicators = []
    for log in system_logs:
        words = log.upper().split()
        for word in words:
            if word in ['ERROR', 'WARNING', 'CRITICAL']:
                risk_indicators.append(word)
    
    unique_risks = list(set(risk_indicators))
    risk_factor = len(unique_risks) / 3.0  # Normalize to 0-1 scale

    # Key computation
    productivity = raw_productivity + version_digit  # Boost from version logic
    final_score = evaluate_performance(productivity, risk_factor)

    # Additional red herring calculations
    phantom_score = 0
    for i in range(3):
        phantom_score ^= i * 2
    phantom_score = math.sqrt(phantom_score) if phantom_score > 0 else 0

    # Output target result
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()