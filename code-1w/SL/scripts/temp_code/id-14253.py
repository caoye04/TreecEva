def analyze_network_state():
    node_ids = [101, 102, 103, 104, 105]
    status_map = {101: 'active', 102: 'inactive', 103: 'active', 104: 'active', 105: 'active'}
    
    # Extract active nodes using dictionary comprehension
    active_nodes = {nid: status for nid, status in status_map.items() if status == 'active'}
    
    # Auxiliary variable - used in unrelated diagnostic check
    diagnostic_log = set()
    diagnostic_log.add('initial_scan_complete')
    
    # Compute XOR checksum of active node IDs
    checksum = 0
    for node_id in active_nodes:
        checksum ^= node_id
    
    # Mask for bit validation (simulates hardware register behavior)
    mask = 101
    
    # Determine threshold compliance
    threshold_flag = not (len(active_nodes) < 5) and (checksum ^ mask) == 10
    
    # Unrelated statistic
    avg_id = sum(active_nodes.keys()) / len(active_nodes)
    
    # Final output
    print(f"Result: {threshold_flag}")

analyze_network_state()