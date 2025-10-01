#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <bitset>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    // Initialize variables
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string text = "HELLO";
    int x = 10;
    int y = 6;
    double z = 1.57;
    
    // Perform nested operations
    int sum_diag = matrix[0][0] + matrix[1][1] + matrix[2][2];
    x = x << 2;  // Left shift x by 2 bits
    y = y & 3;   // Bitwise AND with 3
    
    // Update z using a mathematical expression
    z = compute_expression(x, sum_diag, z);
    
    // Manipulate string and convert to numeric value
    int char_sum = 0;
    for(char c : text) {
        char_sum += static_cast<int>(c);
    }
    
    // Final computation combining all values
    int result = static_cast<int>(z) ^ char_sum;
    cout << "Result: " << result << endl;
    
    return 0;
}