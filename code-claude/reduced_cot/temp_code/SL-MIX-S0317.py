from collections import Counter

def normalize_string(text):
    # Clean and normalize the text for comparison
    return text.lower().strip()

def calculate_similarity(str1, str2):
    # Calculate similarity between two strings (not used in final calculation)
    str1, str2 = normalize_string(str1), normalize_string(str2)
    common_chars = set(str1) & set(str2)
    return len(common_chars) / max(len(set(str1)), len(set(str2)))

def calculate_weighted_score(student_answers, answer_key):
    base_points = 100
    penalty = 0
    bonus = 0
    
    # Count correct answers
    correct_count = 0
    partial_points = 0
    
    for question_id, student_answer in student_answers.items():
        if question_id in answer_key:
            correct_answer = answer_key[question_id]
            
            # Calculate a similarity score (distraction - not used)
            similarity = calculate_similarity(student_answer, correct_answer)
            
            # Check if answer is correct (case-insensitive)
            if normalize_string(student_answer) == normalize_string(correct_answer):
                correct_count += 1
                # Questions with IDs divisible by 3 are worth more
                if question_id % 3 == 0:
                    partial_points += 15
                else:
                    partial_points += 10
    
    # Apply difficulty adjustment (distraction)
    difficulty_factor = 1.2
    theoretical_max = 150 * difficulty_factor
    
    # Calculate penalties based on incorrect answers
    incorrect_count = len(answer_key) - correct_count
    penalty = incorrect_count * 5
    
    # Apply bonus for answering difficult questions
    difficult_questions = [q for q in student_answers.keys() if q % 5 == 0]
    correct_difficult = [q for q in difficult_questions if q in answer_key and 
                         normalize_string(student_answers[q]) == normalize_string(answer_key[q])]
    bonus = len(correct_difficult) * 8
    
    # Compute raw score with bitwise operations
    raw_score = partial_points - (penalty & 0x3F)  # Apply bitwise AND to limit penalty
    
    # Apply bonus with bitwise OR to ensure bonus is added
    adjusted_score = raw_score | bonus
    
    # Final score calculation
    final_score = min(100, adjusted_score)
    return final_score

# Test data
student_answers = {
    1: "Photosynthesis",
    2: "mitochondria",
    3: "DARWIN",
    5: "cell membrane",
    6: "DNA",
    9: "Krebs cycle",
    10: "ecosystem"
}

answer_key = {
    1: "photosynthesis",
    2: "mitochondria",
    3: "Darwin",
    4: "meiosis",
    5: "cell wall",
    6: "dna",
    7: "protein",
    8: "lipid",
    9: "krebs cycle",
    10: "ecosystem"
}

# Calculate the score
final_score = calculate_weighted_score(student_answers, answer_key)
print(f"Result: {final_score}")