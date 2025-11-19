from collections import defaultdict

def process_packet_path(priority_level):
    path_scores = defaultdict(int)
    path_scores['base'] = 10
    
    match priority_level:
        case x if 1 <= x <= 3:
            path_scores['low_priority'] = 5
            adjustments = [i**2 for i in range(1, priority_level+1)]
            path_scores['adjustment'] = sum(adjustments) >> 1
        case x if 4 <= x <= 7:
            path_scores['medium_priority'] = 15
            adjustments = [i**3 for i in range(1, priority_level-2)]
            path_scores['adjustment'] = sum(adjustments) & 0xF
        case x if 8 <= x <= 10:
            path_scores['high_priority'] = 25
            adjustments = [i<<1 for i in range(1, priority_level-6)]
            path_scores['adjustment'] = sum(adjustments) ^ 0xFF
        case _:
            path_scores['unknown'] = -10
            path_scores['adjustment'] = 0
    
    return path_scores

def calculate_tree_branch_modifiers(path_dict, level):
    modifiers = {
        1: lambda d: d['base'] + d.get('low_priority', 0),
        2: lambda d: d['base'] + d.get('medium_priority', 0) + d['adjustment'],
        3: lambda d: d['base'] + d.get('high_priority', 0) * (d['adjustment'] % 7)
    }
    return modifiers.get(level, lambda d: d['base'])(path_dict)

# Main execution
packet_priority = 6
security_path = process_packet_path(packet_priority)
branch_modifier = calculate_tree_branch_modifiers(security_path, 2)
final_security_score = branch_modifier + (security_path['adjustment'] << 2)
print(f"Result: {final_security_score}")