import re
from collections import deque

def calculate_environmental_weight(traits):
    return len([t for t in traits if t.isupper()])

# Plant lineage tree representation
plant_tree = {
    'root': 'ROSA',
    'children': [
        {
            'name': 'ALBA',
            'traits': 'FlOrAlWhItE',
            'children': [
                {'name': 'MAXIMA', 'traits': 'ThOrNyStEm'},
                {'name': 'CANINA', 'traits': 'EdIbLeHiPs'}
            ]
        },
        {
            'name': 'RUBUS',
            'traits': 'BrAmBlEsPuRs',
            'children': [
                {'name': 'IDAEOUS', 'traits': 'ReDBeRRyInG'},
                {'name': 'CAESIUS', 'traits': 'BlUeFrUiTiNg'}
            ]
        }
    ]
}

# Stack for DFS traversal
stack = deque()
stack.append(plant_tree)

# Compatibility tracking
compatibility_patterns = [r'[A-Z][a-z]+', r'[aeiouAEIOU]{2,}', r'[0-9]+']
compatibility_score = 0

visited_species = set()

while stack:
    current_node = stack.pop()
    
    if isinstance(current_node, dict) and 'name' in current_node:
        species_name = current_node['name']
        if species_name in visited_species:
            continue
        visited_species.add(species_name)
        
        # Get traits if available
        species_traits = current_node.get('traits', '')
        
        # Calculate base compatibility using lambda
        weight_func = lambda traits: sum(1 for c in traits if c.isalpha())
        base_weight = weight_func(species_traits)
        
        # Pattern matching score
        pattern_matches = 0
        for pattern in compatibility_patterns:
            matches = re.findall(pattern, species_traits)
            pattern_matches += len(matches)
        
        # Environmental adjustment
        env_adjustment = calculate_environmental_weight(species_traits)
        
        # Update compatibility score
        compatibility_score += base_weight * pattern_matches + env_adjustment
        
        # Add children to stack
        children = current_node.get('children', [])
        for child in reversed(children):  # Reverse for correct DFS order
            stack.append(child)
    elif isinstance(current_node, dict) and 'root' in current_node:
        # Handle root node
        root_name = current_node['root']
        if root_name not in visited_species:
            visited_species.add(root_name)
            # Root has no traits, so minimal contribution
            compatibility_score += 1
            # Add children
            children = current_node.get('children', [])
            for child in reversed(children):
                stack.append(child)

print(f"Result: {compatibility_score}")