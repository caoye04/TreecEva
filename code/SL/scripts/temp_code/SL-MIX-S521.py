import re
from collections import namedtuple

tree_node = namedtuple('tree_node', ['location_id', 'species_list', 'children'])

# Tree representing bird sighting data
migration_tree = tree_node(
    location_id="LOC_001",
    species_list=["sparrow", "robin", "finch"],
    children=[
        tree_node(
            location_id="LOC_002",
            species_list=["hawk", "eagle"],
            children=[]
        ),
        tree_node(
            location_id="LOC_003",
            species_list=["owl", "sparrow", "robin", "finch"],
            children=[
                tree_node(
                    location_id="LOC_004",
                    species_list=["warbler", "thrush", "wren"],
                    children=[]
                )
            ]
        )
    ]
)

def count_species_patterns(node):
    count = 0
    # Check if current node matches the pattern (exactly 3 species)
    if len(set(node.species_list)) == 3:
        count += 1
    
    # Recursively check children
    for child in node.children:
        count += count_species_patterns(child)
    
    return count

matching_locations = count_species_patterns(migration_tree)
print(f"Result: {matching_locations}")