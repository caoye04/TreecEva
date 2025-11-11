from dataclasses import dataclass
from typing import List

token_weights = {'N': 3, 'S': -3, 'E': 2, 'W': -2, 'NE': 5, 'NW': 1, 'SE': -1, 'SW': -5}

@dataclass
class SensorData:
    id: str
    tokens: List[str]

def process_sensor_data(sensor: SensorData) -> int:
    cumulative = 0
    max_cumulative = float('-inf')
    for token in sensor.tokens:
        if token in token_weights:
            cumulative += token_weights[token]
            if cumulative > max_cumulative:
                max_cumulative = cumulative
        else:
            cumulative = 0
    return max_cumulative

def classify_zone(score: int) -> str:
    match score:
        case s if s >= 10:
            return 'A'
        case s if s >= 5:
            return 'B'
        case s if s >= 0:
            return 'C'
        case _:
            return 'D'

sensor_readings = [
    SensorData('S1', ['N', 'NE', 'E', 'SE', 'S']),
    SensorData('S2', ['W', 'NW', 'N', 'NE', 'E']),
    SensorData('S3', ['SW', 'W', 'NW', 'N', 'NE'])
]

zone_classifications = []
for sensor in sensor_readings:
    score = process_sensor_data(sensor)
    zone = classify_zone(score)
    zone_classifications.append(zone)

# Convert to frozenset for immutable set operations
zones_set = frozenset(zone_classifications)
target_zones = frozenset(['A', 'B'])

# Greedy selection: count overlapping zones
optimal_zone_score = len(zones_set.intersection(target_zones)) * 10 + sum(1 for z in zones_set if z in target_zones)

print(f"Result: {optimal_zone_score}")