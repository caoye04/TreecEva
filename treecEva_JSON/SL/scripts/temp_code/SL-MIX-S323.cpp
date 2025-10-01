#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base = 4;
    int exp = 3;
    double log_val = log2(64);
    int xor_result = 0;
    
    // Step 1: Perform exponentiation and logarithmic calculation
    int power_result = pow(base, exp);
    int log_int = static_cast<int>(log_val);
    
    // Step 2: Bitwise XOR of all elements in the matrix
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            xor_result ^= matrix[i][j];
        }
    }
    
    // Step 3: String manipulation
    string s1 = "Hello";
    string s2 = "World";
    string combined = s1 + s2;
    int str_length = combined.length();
    
    // Step 4: Complex arithmetic expression
    int expr_result = (power_result + log_int * str_length - xor_result) % 100;
    
    // Step 5: Nested conditional logic
    int final_result = 0;
    if (expr_result > 20) {
        if ((expr_result & 1) == 0) {
            final_result = expr_result * 2;
        } else {
            final_result = expr_result + 10;
        }
    } else {
        final_result = expr_result - 5;
    }
    
    // Final adjustment based on prime check
    bool is_prime = true;
    if (final_result <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i <= sqrt(final_result); ++i) {
            if (final_result % i == 0) {
                is_prime = false;
                break;
            }
        }
    }
    
    if (is_prime) {
        final_result += 1;
    } else {
        final_result -= 1;
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}