def analyze_network_coverage():
    base_stations = {101, 102, 103, 104, 105}
    redundant_nodes = {103, 104, 106, 107}
    active_sectors = {x for x in base_stations if x % 2 == 1}
    maintenance_lock = {101, 102}
    signal_regions = base_stations - maintenance_lock
    diagnostic_mode = True
    system_log = "Diagnostic active: proceeding with zone analysis"
    critical_zones = {102, 103, 104, 108}
    coverage_overlap = signal_regions & critical_zones
    temp_buffer = [x * 2 for x in redundant_nodes]
    final_output = sum(active_sectors)
    print(f"Result: {coverage_overlap}")
analyze_network_coverage()