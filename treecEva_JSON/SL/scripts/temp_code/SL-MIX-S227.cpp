#define M_PI 3.14159265358979323846
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
    double log_val = log2(1024);
    
    // Step 1: Compute power
    int powered = pow(base, exp);
    
    // Step 2: Bitwise operations
    int bitwise_and = matrix[1][1] & static_cast<int>(log_val);
    int bitwise_or = matrix[0][2] | powered;
    int xor_result = bitwise_and ^ bitwise_or;
    
    // Step 3: Trigonometric adjustment
    double sin_val = sin(M_PI / 6); // 0.5
    int adjusted_xor = static_cast<int>(round(xor_result * sin_val));
    
    // Step 4: String manipulation
    string s1 = "hello";
    string s2 = "world";
    string combined = s1 + s2;
    int str_length = combined.length();
    
    // Step 5: Matrix diagonal sum
    int diag_sum = 0;
    for(int i=0; i<3; ++i) {
        diag_sum += matrix[i][i];
    }
    
    // Step 6: Final computation
    int final_result = (adjusted_xor + str_length) % diag_sum;
    
    cout << "Result: " << final_result << endl;
    return 0;
}