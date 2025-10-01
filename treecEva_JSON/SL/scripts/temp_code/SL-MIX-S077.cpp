#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string text = "AdvancedProgramming";
    int x = 10;
    int y = 6;
    int z = x & y;
    
    // Step 1: Perform bitwise shift and update z
    z <<= 2;
    
    // Step 2: Update x using XOR with matrix element
    x ^= matrix[1][2];
    
    // Step 3: Modify y based on string length
    y += static_cast<int>(text.length());
    
    // Step 4: Nested loop to modify matrix values
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if ((i + j) % 2 == 0) {
                matrix[i][j] *= 2;
            } else {
                matrix[i][j] -= 1;
            }
        }
    }
    
    // Step 5: Compute intermediate value using function call
    double temp = compute_expression(matrix[0][1], matrix[2][0], 1.5);
    
    // Step 6: Final calculation involving multiple variables
    int result = (z | x) + y + static_cast<int>(temp);
    
    cout << "Result: " << result << endl;
    return 0;
}