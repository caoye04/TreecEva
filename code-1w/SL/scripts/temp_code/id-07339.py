from itertools import compress

def optimize_distribution(excess, deficit):
    # Sort in descending order for optimal pairing
    excess.sort(reverse=True)
    deficit.sort()
    
    # Calculate transfer efficiency using greedy matching
    transfers = []
    for e in excess:
        for d in deficit:
            if d > 0:
                transfer_amount = min(e, d)
                transfers.append(transfer_amount)
                d -= transfer_amount
                e -= transfer_amount
                if e == 0:
                    break
    
    total_used = sum(transfers)
    peak_demand = max(transfers) if transfers else 0
    
    # Irrelevant distraction: unused variable (minimal interference)
    unused_buffer = [x * 0.5 for x in excess]
    
    final_capacity = total_used + peak_demand * 0.5
    return final_capacity

# System load data (in MW)
supply_surplus = [120, 75, 90, 110]
demand_deficit = [80, 95, 60, 100]

# Normalize data using slicing to exclude last element for calibration
excess_list = supply_surplus[:3]
deficit_list = demand_deficit[1:]

final_capacity = optimize_distribution(excess_list, deficit_list)
print(f"Result: {final_capacity}")