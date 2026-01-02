def calculate_net_flow(nodes):
    # Initialize tracking variables
    total_inbound = 0
    total_outbound = 0
    temp_buffer = []
    adjustment_factor = 0.85
    decay_rate = 0.02
    
    # Auxiliary lambda for dynamic weighting (not used in final calculation)
    weight_fn = lambda x, t: x * (adjustment_factor ** t) if t > 5 else x
    
    # Simulate transient fluctuations (distractor loop)
    transient_peak = 0
    for i in range(8):
        fluctuation = (i * 0.3) ** 1.5
        if fluctuation > transient_peak:
            transient_peak = fluctuation
    
    # Main processing: compute net flow based on node type
    for node in nodes:
        node_id = node['id']
        inflow = node['inflow']
        outflow = node['outflow']
        node_type = node['type']
        
        # Distractor: buffer unused intermediate values
        temp_buffer.append({'node': node_id, 'delta': inflow - outflow})
        
        # Only 'active' and 'relay' nodes contribute to final flux
        if node_type in ['active', 'relay']:
            total_inbound += inflow
            total_outbound += outflow
        
        # Early exit red herring: irrelevant condition
        if node_id == 'N001':
            base_anchor = inflow * 0.1

    # Secondary distractor computation: simulate calibration
    calibration_sum = 0
    for i in range(1, 6):
        calibration_sum += (i * decay_rate) ** 1.1
    
    # Core logic: net flow only from relevant nodes
    net_flow = total_inbound - total_outbound
    
    # Apply fixed transformation (not dependent on calibration or transient)
    final_flux = int(abs(net_flow * 0.75))

    return final_flux

# Define energy nodes with mixed types
energy_nodes = [
    {'id': 'N001', 'inflow': 120, 'outflow': 45, 'type': 'active'},
    {'id': 'N002', 'inflow': 88, 'outflow': 33, 'type': 'passive'},      # won't count
    {'id': 'N003', 'inflow': 105, 'outflow': 67, 'type': 'relay'},
    {'id': 'N004', 'inflow': 50, 'outflow': 20, 'type': 'active'},
    {'id': 'N005', 'inflow': 200, 'outflow': 180, 'type': 'standby'},   # won't count
]

# Execute main logic
final_flux = calculate_net_flow(energy_nodes)
print(f"Result: {final_flux}")