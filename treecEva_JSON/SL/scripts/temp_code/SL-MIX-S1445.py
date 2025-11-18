from collections import defaultdict
import statistics

def calculate_movement_anomalies():
    # Simulated wildlife tracking data: device_id -> list of (x, y) coordinates
    tracking_data = {
        'WT-001': [(0, 0), (1, 2), (3, 4), (6, 8)],
        'WT-002': [(10, 10), (12, 11), (15, 13), (18, 17)],
        'WT-003': [(5, 5), (7, 6), (9, 9), (12, 12)]
    }
    
    distance_deviations = []
    anomaly_score = 0
    
    for device_id, coordinates in tracking_data.items():
        segment_distances = []
        
        # Calculate distances between consecutive points
        for i in range(len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i+1]
            distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
            segment_distances.append(distance)
        
        if len(segment_distances) > 1:
            mean_distance = statistics.mean(segment_distances)
            std_distance = statistics.stdev(segment_distances) if len(segment_distances) > 1 else 0
            
            # Check for anomalous segments (more than 1.5 std dev from mean)
            for dist in segment_distances:
                deviation = abs(dist - mean_distance)
                if deviation > 1.5 * std_distance:
                    distance_deviations.append(deviation)
    
    # Compute final anomaly score using geometric and statistical measures
    if distance_deviations:
        avg_deviation = statistics.mean(distance_deviations)
        max_deviation = max(distance_deviations)
        anomaly_score = int(avg_deviation * max_deviation)
    else:
        anomaly_score = 42  # Default baseline score
    
    return anomaly_score

# Main execution
anomaly_score = calculate_movement_anomalies()
print(f"Result: {anomaly_score}")