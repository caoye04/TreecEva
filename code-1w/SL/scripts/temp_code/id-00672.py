def calculate_final_score(results, bonus_enabled):
    base_score = sum(results['math'], results['science'])
    if bonus_enabled:
        adjustment = results['math'] // 10
        base_score += adjustment
    
    # Irrelevant distraction: unused variable
    temp_log = {'processed': True, 'user': 'admin'}
    
    penalty = 0
    if results['science'] < 50:
        penalty = 10
    
    final_adjustment = 5 if results['math'] >= 90 else 2
    return base_score - penalty + final_adjustment

# Main execution
class_data = {
    'math': 95,
    'science': 45
}
bonus_active = True

final_score = calculate_final_score(class_data, bonus_active)
print(f"Result: {final_score}")