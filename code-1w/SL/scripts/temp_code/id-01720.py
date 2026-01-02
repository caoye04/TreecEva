def analyze_feedback(ratings):
    avg_rating = sum(ratings) / len(ratings)
    adjusted = [r * 1.1 for r in ratings if r > 3]
    return sum(adjusted) if adjusted else avg_rating

feedback_scores = [4.2, 3.8, 4.5, 2.9, 4.7]

# Irrelevant string processing (distractor)
user_input = "  Performance Review Q3  "
cleaned = user_input.strip().lower().replace(' ', '_')
date_tag = "q3_2023"
formatted_name = f"report_{cleaned}_{date_tag}.txt"

# More distraction: unused data transformation
raw_data = "4.2,3.8,4.5,2.9,4.7"
data_list = raw_data.split(',')
numeric_data = [float(x) for x in data_list]

# Key metrics computation
base_metric = sum(feedback_scores) * 0.8
bonus_metric = analyze_feedback(feedback_scores) * 0.4
metrics = [base_metric, bonus_metric, len(feedback_scores)]

# Dummy conditional (dead logic path)
if len(formatted_name) > 50:
    overflow_flag = True
else:
    overflow_flag = False  # Not used later

threshold = 5.0

def process_performance(data, limit):
    cap = limit * 2
    temp_result = 0
    
    for val in data:
        if val >= cap:
            temp_result += val // 2
        elif val >= limit:
            temp_result += int(val * 0.75)
        else:
            temp_result += round(val + 1.5)
    
    # Extra logic that doesn't affect outcome
    checksum = ''.join([str(int(v)) for v in data])
    tag = f"result_{checksum}"
    
    return temp_result

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")