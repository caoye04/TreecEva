import re
from collections import defaultdict

def analyze_dolphin_behavior(sonar_log):
    state_machine = {
        'scattered': {'ping_frequency_high': 'grouping', 'duration_exceeded': 'scattered'},
        'grouping': {'proximity_met': 'consolidating', 'dispersal_detected': 'scattered'},
        'consolidating': {'stability_achieved': 'pod_formed', 'instability_detected': 'grouping'},
        'pod_formed': {'cohesion_maintained': 'pod_formed', 'fragmentation_occurred': 'scattering'}
    }
    
    current_state = 'scattered'
    pod_stability_score = 0
    consolidation_events = []
    
    for entry in sonar_log:
        if current_state == 'scattered' and entry['ping_rate'] > 10:
            current_state = state_machine[current_state]['ping_frequency_high']
        elif current_state == 'grouping' and entry['avg_distance'] < 50:
            current_state = state_machine[current_state]['proximity_met']
        elif current_state == 'consolidating':
            stability = entry['cohesion_index'] * 0.7 + entry['duration'] * 0.3
            if stability > 80:
                current_state = state_machine[current_state]['stability_achieved']
                pod_stability_score += stability
                consolidation_events.append(entry['timestamp'])
            else:
                current_state = 'grouping'
        elif current_state == 'pod_formed' and entry['fragmentation'] > 0.3:
            current_state = 'scattering'
        
        if entry['observation_period'] > 120 and current_state not in ['pod_formed', 'consolidating']:
            current_state = 'scattered'
    
    pattern = r'\d{2}:\d{2}'
    temporal_clusters = defaultdict(int)
    
    for time in consolidation_events:
        hour = re.match(pattern, time).group()
        temporal_clusters[hour] += 1
    
    consolidated_pod_count = 0
    for count in temporal_clusters.values():
        if count >= 2:
            consolidated_pod_count += count * 2
        else:
            consolidated_pod_count += count
    
    return consolidated_pod_count

sonar_readings = [
    {'timestamp': '14:32', 'ping_rate': 12, 'avg_distance': 100, 'cohesion_index': 0, 'duration': 0, 'fragmentation': 0, 'observation_period': 30},
    {'timestamp': '14:45', 'ping_rate': 0, 'avg_distance': 40, 'cohesion_index': 0, 'duration': 0, 'fragmentation': 0, 'observation_period': 45},
    {'timestamp': '14:55', 'ping_rate': 0, 'avg_distance': 0, 'cohesion_index': 85, 'duration': 25, 'fragmentation': 0, 'observation_period': 55},
    {'timestamp': '15:10', 'ping_rate': 0, 'avg_distance': 0, 'cohesion_index': 90, 'duration': 35, 'fragmentation': 0, 'observation_period': 70},
    {'timestamp': '15:30', 'ping_rate': 0, 'avg_distance': 0, 'cohesion_index': 0, 'duration': 0, 'fragmentation': 0.5, 'observation_period': 90},
    {'timestamp': '16:05', 'ping_rate': 15, 'avg_distance': 120, 'cohesion_index': 0, 'duration': 0, 'fragmentation': 0, 'observation_period': 20},
    {'timestamp': '16:22', 'ping_rate': 0, 'avg_distance': 30, 'cohesion_index': 0, 'duration': 0, 'fragmentation': 0, 'observation_period': 37},
    {'timestamp': '16:35', 'ping_rate': 0, 'avg_distance': 0, 'cohesion_index': 82, 'duration': 20, 'fragmentation': 0, 'observation_period': 50},
    {'timestamp': '16:50', 'ping_rate': 0, 'avg_distance': 0, 'cohesion_index': 78, 'duration': 15, 'fragmentation': 0, 'observation_period': 65}
]

consolidated_pod_count = analyze_dolphin_behavior(sonar_readings)
print(f"Result: {consolidated_pod_count}")