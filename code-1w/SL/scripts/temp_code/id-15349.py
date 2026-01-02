from collections import defaultdict, Counter
import math

# Simulated system log analysis with heavy distractions
def analyze_system_health():
    raw_logs = [
        'INFO:cpu_load=0.75|mem=82%|disk_io=45',
        'WARN:cpu_load=0.88|mem=91%|disk_io=67',
        'ERROR:cpu_load=0.92|mem=96%|disk_io=89',
        'INFO:cpu_load=0.60|mem=70%|disk_io=30',
        'INFO:cpu_load=0.55|mem=65%|disk_io=25'
    ]

    # Irrelevant transformation - red herring
    decoy_matrix = [[i*j for j in range(5)] for i in range(5)]
    temp_shadow = sum(sum(row) for row in decoy_matrix)

    # Parsing logs into structured format (relevant)
    log_entries = []
    for entry in raw_logs:
        parts = entry.split(':')
        level = parts[0]
        metrics = {}
        data = parts[1].split('|')
        for d in data:
            k, v = d.split('=')
            if k == 'mem':
                metrics[k] = float(v.strip('%'))
            else:
                metrics[k] = float(v)
        metrics['severity'] = 1 if level == 'INFO' else (2 if level == 'WARN' else 3)
        log_entries.append(metrics)

    # Distractor: unused function
    def deprecated_aggregator(x):  
        return sum(math.sin(i) for i in x) * 0.1

    # System state with decoy fields
    system_state = {
        'uptime': 123456,
        'user_count': 847,
        'active_services': ['auth', 'storage', 'compute'],
        'config_flags': { 'debug_mode': False, 'tracing_enabled': True },
        'last_reset': '2023-05-10',
        'baseline_cpu': 0.65,
        'decoy_entropy': [math.log(i+2) for i in range(100)],  # Heavy distraction
        'cache_stats': { 'hits': 1024, 'misses': 128 }
    }

    # Irrelevant counters
    performance_tally = defaultdict(int)
    for log in log_entries:
        if log['cpu_load'] > 0.8:
            performance_tally['high_cpu'] += 1
        if log['mem'] > 90:
            performance_tally['high_mem'] += 1

    snapshot_series = [len(raw_logs), len(system_state['active_services']), system_state['user_count']]
    shadow_index = math.floor(sum(snapshot_series) / len(snapshot_series))

    # Real processing begins here
    def extract_patterns(entries):
        patterns = Counter()
        for e in entries:
            load_bin = min(int(e['cpu_load'] / 0.1), 9)
            mem_bin = min(int(e['mem'] / 10), 9)
            patterns[(load_bin, mem_bin)] += 1
        return patterns

    pattern_counter = extract_patterns(log_entries)

    # Heavily obscured core logic
    def compute_stability_score(patterns, baseline):
        score = 100.0
        total_patterns = sum(patterns.values())
        
        # Distractor loop - calculates but isn't used
        anti_entropy = 0.0
        for i in range(total_patterns + 1):
            if i > 0:
                anti_entropy += math.log(i)
        
        for (load_bin, mem_bin), count in patterns.items():
            load_factor = load_bin * 0.1
            stress_weight = count * (load_factor - baseline)**2
            score -= stress_weight * 10
            
            # Dead code branch - misleading
            if load_factor < baseline and False:
                score += 5  # Never executed

        return round(score, 4)

    base_metric = system_state['baseline_cpu']
    stability = compute_stability_score(pattern_counter, base_metric)

    # Complex distractor - string manipulation maze
    service_names = ''.join(system_state['active_services']).upper()
    rotated = service_names[3:] + service_names[:3]
    frequency_map = Counter(rotated)
    hash_value = 0
    for char, freq in frequency_map.items():
        hash_value += ord(char) * freq
    
    # Decoy final calculation that looks important
    phantom_risk = (hash_value % 100) / 10.0

    # Actual key function buried among distractions
    def process_metrics(entries, state):
        # Extract meaningful time-series data
        cpu_readings = [e['cpu_load'] for e in entries]
        mem_readings = [e['mem'] for e in entries]
        
        # Real computation chain
        avg_cpu = sum(cpu_readings) / len(cpu_readings)
        max_mem = max(mem_readings)
        severity_peaks = len([e for e in entries if e['severity'] >= 2])
        
        # Primary diagnostic formula
        base_diagnostic = avg_cpu * 1000
        if max_mem > 90:
            base_diagnostic += 200
        if severity_peaks > 1:
            base_diagnostic += 150
        
        # Final adjustment using system uptime (only relevant part of state)
        uptime_factor = (state['uptime'] % 500) / 100.0
        final_adjustment = math.floor(base_diagnostic + uptime_factor)
        
        # Critical red herring: this variable looks like answer but isn't
        transient_score = final_adjustment + int(phantom_risk)
        
        # ACTUAL answer
        return final_adjustment

    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_state)
    
    # Multiple irrelevant print statements removed in production
    # DEBUG: print(f'Shadow index: {shadow_index}')
    # DEBUG: print(f'Transient score: {transient_score}')
    
    print(f"Result: {final_diagnostic}")

analyze_system_health()