#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c;
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    
    int x = matrix[1][2] & 15; // Bitwise AND
    int y = matrix[0][1] << 2; // Left shift
    
    double z = compute_expression(x, y, 1.5);
    
    int sum_indices = 0;
    for (size_t i = 0; i < s.length(); ++i) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum_indices += static_cast<int>(i);
        }
    }
    
    int bitwise_xor = (x ^ y) | 6; // XOR then OR
    
    double sin_component = sin(static_cast<double>(bitwise_xor % 10));
    
    int final_result = static_cast<int>(z + sum_indices + sin_component * 100);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}