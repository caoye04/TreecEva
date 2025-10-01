#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double computeExpression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - log(c + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string text = "AdvancedProgramming";
    int x = 0b11010 & 0b10111;
    int y = matrix[1][2] << 1;
    double z = computeExpression(matrix[0][1], matrix[2][0], 2.5);
    
    // Manipulate string to get numeric value
    int charSum = 0;
    for(char ch : text.substr(0, 6)) {
        charSum += static_cast<int>(ch);
    }
    
    // Perform bit rotation simulation
    int rotated_x = ((x >> 2) | (x << 3)) & 0b11111;
    
    // Calculate final result using all derived values
    double intermediate = (y * z) / (charSum % 100);
    int result = static_cast<int>(intermediate) ^ rotated_x;
    
    cout << "Result: " << result << endl;
    return 0;
}