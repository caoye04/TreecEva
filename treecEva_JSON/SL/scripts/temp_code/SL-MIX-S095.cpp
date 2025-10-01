#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize variables
    int a = 15, b = 7;
    double x = 3.5, y = 2.0;
    string s = "HelloWorld";
    
    // Complex arithmetic and bitwise operations
    int step1 = (a * b) + static_cast<int>(pow(x, y)) - (a & b);
    int step2 = (step1 >> 2) ^ (a | b);
    
    // Vector operations
    vector<int> nums = {step1, step2, a, b};
    int vec_sum = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        vec_sum += nums[i] * (i + 1);
    }
    
    // String manipulation
    int str_len = s.length();
    char mid_char = s[str_len / 2];
    int ascii_val = static_cast<int>(mid_char);
    
    // Trigonometric and logarithmic operations
    double trig_result = sin(M_PI / 4) * cos(M_PI / 4);
    double log_result = log10(step1 > 100 ? step1 : step2);
    
    // Complex conditional logic
    int conditional_val = 0;
    if ((step1 % 2 == 0) && (step2 > 50)) {
        conditional_val = static_cast<int>(trig_result * 100);
    } else if ((vec_sum > 1000) || (ascii_val < 100)) {
        conditional_val = static_cast<int>(log_result * 50);
    } else {
        conditional_val = (step1 + step2) % 7;
    }
    
    // Final calculation combining all previous results
    int final_result = ((vec_sum / 10) + ascii_val) ^ conditional_val;
    
    // Adjust based on mathematical properties
    if (final_result < 0) {
        final_result = abs(final_result);
    }
    
    // Apply one last transformation
    final_result = (final_result * 3) - (static_cast<int>(sqrt(final_result)) % 5);
    
    cout << "Result: " << final_result << endl;
    return 0;
}