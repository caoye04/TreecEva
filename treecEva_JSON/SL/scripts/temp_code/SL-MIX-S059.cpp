#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double computeExpression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c;
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int x = 10;
    int y = 20;
    double z = 2.5;
    
    // Step 1: Modify x using bitwise operations
    x = (x << 2) ^ (y >> 1);
    
    // Step 2: Update y based on matrix values
    y += matrix[1][2] - matrix[0][0];
    
    // Step 3: Compute z using the function
    z = computeExpression(matrix[2][1], matrix[0][2], z);
    
    // Step 4: Manipulate string and use its length
    s = s.substr(5) + to_string(matrix[1][0]);
    int len = static_cast<int>(s.length());
    
    // Step 5: Perform complex arithmetic
    int temp = (x & 0xF) * (y | 0x3) + len;
    
    // Step 6: Final calculation involving all variables
    double result = (temp / 3.0) + z - (static_cast<double>(matrix[2][2]) / matrix[0][1]);
    
    cout << "Result: " << result << endl;
    return 0;
}