def calculate_performance(data):
    base_score = 0
    penalties = []
    
    for entry in data['metrics']:
        if entry['status'] == 'failed':
            penalties.append(entry['weight'] * 0.5)
        else:
            base_score += entry['weight'] * entry['efficiency']
    
    adjustment = sum(penalties[:2]) if len(penalties) > 1 else 0
    base_score -= adjustment
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_log = [f'Processed {len(data["metrics"])} entries']
    
    return round(base_score, 3)

# Simulated benchmark dataset
dataset = {
    "name": "ThroughputTestSuite",
    "metrics": [
        {"weight": 10, "efficiency": 0.95, "status": "passed"},
        {"weight": 15, "efficiency": 0.88, "status": "passed"},
        {"weight": 5,  "efficiency": 1.0,  "status": "failed"},
        {"weight": 20, "efficiency": 0.75, "status": "passed"},
        {"weight": 8,  "efficiency": 0.0,  "status": "failed"}
    ]
}

initial_offset = 5.0  # Distractor: not used in final calculation

final_score = calculate_performance(dataset)
print(f"Target result: {final_score}")