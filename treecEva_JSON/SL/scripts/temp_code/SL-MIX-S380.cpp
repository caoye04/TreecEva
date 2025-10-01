#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    int a = 3, b = 4;
    double x = 2.5, y = 3.7;
    string s1 = "hello", s2 = "world";
    
    // Step 1: Perform nested loop operations on matrix
    int sum = 0;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            sum += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    // Step 2: Perform bitwise and arithmetic operations
    int bitwise_result = (a << 2) & (b | 6);
    
    // Step 3: Perform mathematical operations
    double math_result = pow(x, 3) + sqrt(y * 4) - sin(M_PI / 4);
    
    // Step 4: String manipulation
    string combined = s1 + s2;
    int str_length = combined.length();
    
    // Step 5: Complex conditional assignment
    int conditional_value;
    if ((sum % 2 == 0) && (bitwise_result > 5)) {
        conditional_value = static_cast<int>(math_result) * str_length;
    } else {
        conditional_value = static_cast<int>(math_result) + str_length;
    }
    
    // Step 6: Final calculation involving all previous results
    int final_result = (sum / 10) + (bitwise_result * 2) + static_cast<int>(math_result) + str_length + conditional_value;
    
    cout << "Result: " << final_result << endl;
    return 0;
}