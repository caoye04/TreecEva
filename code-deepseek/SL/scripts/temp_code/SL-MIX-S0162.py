def data_processor(input_data):
    # Distractor: unused lambda for different calculation
    alt_calc = lambda x: (x * 3 - 7) % 11
    
    # Main processing logic
    if isinstance(input_data, str):
        parts = input_data.split(':')
        if len(parts) >= 2:
            # Distractor: unused intermediate calculation
            temp_sum = sum(ord(c) for c in parts[0]) % 100
            
            # Actual relevant processing
            nums = list(map(int, parts[1].split(',')))
            result = nums[0] * nums[1] - nums[2] + nums[3] // nums[4]
            
            # Distractor: dead code path
            if result > 1000:
                result += temp_sum  # Never executed
                
            return result
    return -999

# Irrelevant helper functions for distraction
def unused_validator(x):
    return x > 0 and x < 100

def misleading_calc(values):
    return sum(values) * 2 - 5

# Main execution
raw_input = "header:8,4,15,12,3"
processed_input = raw_input.replace("header:", "")

# Distractor: unused intermediate result
intermediate = misleading_calc([5, 10, 15])

final_result = data_processor(raw_input)

# More distractor operations
unused_var = (intermediate + 25) * 2
backup_calc = final_result * 3 - 7

print(f"Result: {final_result}")