def calculate_score(base_score, multiplier, bonus_flag):
    total = 0                           # Line 2
    adjusted_score = base_score         # Line 3
    
    if base_score > 50:                 # Line 5
        adjusted_score = base_score * 1.2  # Line 6
        bonus_flag = True               # Line 7
    elif base_score > 20:               # Line 8
        adjusted_score = base_score * 1.1  # Line 9
    else:                               # Line 10
        adjusted_score = base_score * 0.9  # Line 11
    
    if bonus_flag:                      # Line 13
        total = adjusted_score * multiplier + 10  # Line 14
    else:                               # Line 15
        total = adjusted_score * multiplier       # Line 16
    
    return total                        # Line 18


