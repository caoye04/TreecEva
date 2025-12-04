def analyze_medical_compounds(compounds):
    # Track active ingredients across all compounds
    active_ingredients = set()
    inactive_ingredients = set()
    compound_frequencies = {}
    
    # Process each compound and its ingredients
    for idx, compound in enumerate(compounds):
        name, ingredients = compound
        # Count ingredient occurrences
        for ingredient in ingredients:
            if ingredient.startswith('A') or ingredient.endswith('ol'):
                active_ingredients.add(ingredient)
            else:
                inactive_ingredients.add(ingredient)
                
            if ingredient in compound_frequencies:
                compound_frequencies[ingredient] += 1
            else:
                compound_frequencies[ingredient] = 1
    
    # Calculate some statistics (not all are used)
    total_ingredients = len(active_ingredients) + len(inactive_ingredients)
    avg_ingredients = total_ingredients / max(1, len(compounds))
    
    # Find ingredients that appear in multiple compounds
    multi_compound_ingredients = {k for k, v in compound_frequencies.items() if v > 1}
    overlap_count = len(multi_compound_ingredients)
    
    # Determine uniqueness ratio (not used in final calculation)
    uniqueness_ratio = len(active_ingredients) / total_ingredients if total_ingredients > 0 else 0
    
    # Calculate final metrics
    unique_chars_count = len(active_ingredients)
    effectiveness_score = unique_chars_count * 10 - overlap_count
    
    return {
        "active_count": len(active_ingredients),
        "inactive_count": len(inactive_ingredients),
        "effectiveness": effectiveness_score
    }

# Test with sample compounds
compound_data = [
    ("CompoundA", ["Acetaminophen", "Caffeine", "Menthol"]),
    ("CompoundB", ["Ibuprofen", "Paracetamol", "Ethanol"]),
    ("CompoundC", ["Aspirin", "Menthol", "Propanol"])
]

result = analyze_medical_compounds(compound_data)
print(f"Result: {result['active_count']}")