def assess_purification(elements, contaminants):
    raw_set = set(elements)
    dangerous_contaminants = set(contaminants)
    
    # Identify elements that are both stable and uncontaminated
    stable_elements = {e for e in raw_set if e % 2 == 0}
    purified_elements = stable_elements - dangerous_contaminants
    
    # Irrelevant distraction: unused calculation
    avg_atomic_weight = sum(raw_set) / len(raw_set) if raw_set else 0
    
    filtration_score = len(purified_elements)
    return filtration_score

# Execute with test data
element_pool = [18, 22, 34, 13, 27, 44, 8, 6]
common_pollutants = [13, 44, 18]

result = assess_purification(element_pool, common_pollutants)
print(f"Target result: {result}")