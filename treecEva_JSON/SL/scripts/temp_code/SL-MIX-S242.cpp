#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int sum_primes = 0;
    
    // Sum all elements in the matrix
    for (const auto& row : matrix) {
        for (int val : row) {
            sum_primes += val;
        }
    }
    
    // Perform a complex mathematical expression
    double expr = pow(sum_primes, 1.0/3.0);
    int rounded_expr = static_cast<int>(round(expr));
    
    // Bitwise operations
    int shifted = (rounded_expr << 2) ^ 0xF;
    int masked = shifted & 0x3F;
    
    // String manipulation
    string s = "compute";
    reverse(s.begin(), s.end());
    int str_hash = 0;
    for (char c : s) {
        str_hash += static_cast<int>(c);
    }
    
    // Final computation using all derived values
    int final_result = (masked * 3) + (str_hash % 100) - static_cast<int>(sqrt(sum_primes));
    
    cout << "Result: " << final_result << endl;
    return 0;
}