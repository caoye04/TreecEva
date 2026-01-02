def analyze_storage_efficiency(zones, stock):
    efficiency_map = {}
    total_utilization = 0
    
    for zone, capacity in zones.items():
        occupied = stock.get(zone, 0)
        utilization = occupied / capacity if capacity > 0 else 0
        efficiency_map[zone] = round(utilization * 100, 2)
        total_utilization += utilization

    avg_efficiency = total_utilization / len(zones) if zones else 0
    return efficiency_map, avg_efficiency


def validate_zone_integrity(zones):
    valid_zones = set()
    invalid_flagged = []
    
    for z in zones:
        if z.startswith('A') or z.startswith('B'):
            if zones[z] > 0 and zones[z] <= 1000:
                valid_zones.add(z)
        else:
            invalid_flagged.append(z)
    
    # Irrelevant aggregation
    summary_report = {"valid_count": len(valid_zones), "issues": len(invalid_flagged)}
    return valid_zones, summary_report

def calculate_remaining_capacity(layout, inventory):
    remaining = 0
    reserved_buffer = 0
    
    # Primary logic
    for area in layout:
        base_cap = layout[area]
        current_load = inventory.get(area, 0)
        
        # Buffer logic (some areas require reserve)
        if area in ['A1', 'A2', 'B1']:
            buffer = 0.1 * base_cap
        elif area in ['C1', 'C2']:
            buffer = 0.25 * base_cap
        else:
            buffer = 0.05 * base_cap
        
        available = base_cap - current_load - buffer
        if available > 0:
            remaining += available
        
        # Dead code - never used further
        if available < 0:
            reserved_buffer += abs(available)

    # Distractor computation
    phantom_slots = [base - inventory.get(a, 0) for a, base in layout.items() if base > 500]
    phantom_total = sum(phantom_slots)
    adjusted_phantom = phantom_total * 0.9 if phantom_total > 0 else 0
    
    # Final relevant assignment
    final_capacity = int(remaining)
    
    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Main execution block
if __name__ == "__main__":
    # Warehouse configuration (key-value: area -> max capacity)
    warehouse_layout = {
        'A1': 800, 'A2': 600, 'B1': 1000, 'B2': 400,
        'C1': 700, 'C2': 900, 'D1': 300
    }
    
    # Current inventory levels per area
    inventory_levels = {
        'A1': 700, 'A2': 500, 'B1': 850, 'B2': 300,
        'C1': 600, 'C2': 720, 'D1': 150
    }
    
    # Trigger distractor analysis
    efficiency_metrics, avg_usage = analyze_storage_efficiency(warehouse_layout, inventory_levels)
    valid_areas, audit_log = validate_zone_integrity(warehouse_layout)
    
    # Key state-tracking variables (some irrelevant)
    audit_flags = []
    compliance_score = 0
    for area in warehouse_layout:
        if area not in valid_areas:
            audit_flags.append(f"{area}_review")
        compliance_score += 1 if area in valid_areas else 0
    
    # Core calculation point
    final_capacity = calculate_remaining_capacity(warehouse_layout, inventory_levels)