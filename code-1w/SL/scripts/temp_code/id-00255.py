def analyze_survey_overlap():
    group_a_responses = {2, 3, 5, 7, 11, 13, 17}
    group_b_responses = {3, 7, 11, 15, 19, 23}
    group_c_responses = {2, 3, 7, 13, 17, 19}

    common_ab = group_a_responses & group_b_responses
    common_ac = group_a_responses & group_c_responses
    
    all_common = common_ab & common_ac
    final_correction = 2 * len(all_common)
    final_overlap = len(common_ab)
    final_overlap += final_correction // 2
    
    return final_overlap

result = analyze_survey_overlap()
print(f"Result: {result}")