total_zones = 25
active_sensors = 18
defective_sensors = 3
sensor_range = 4
backup_sensors = 5
zone_scan = [i for i in range(1, total_zones + 1) if i % sensor_range == 0]
overlap_count = len(set(zone_scan)) - len(zone_scan) + 3
operational_sensors = active_sensors - defective_sensors
redundant_calc = backup_sensors * sensor_range // 2
coverage_ratio = operational_sensors / total_zones
final_coverage = (active_sensors - overlap_count) / total_zones
print(f"Result: {final_coverage}")