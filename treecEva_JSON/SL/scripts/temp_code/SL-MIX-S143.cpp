#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double complex_calculation(int a, int b) {
    return pow(a, 2) + sqrt(b) - (a & b) + (a << 1);
}

int main() {
    vector<vector<int>> matrix = {{12, 7, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<int> flat;
    
    // Flatten matrix
    for (const auto& row : matrix) {
        for (int val : row) {
            flat.push_back(val);
        }
    }
    
    // Sort in descending order
    sort(flat.begin(), flat.end(), greater<int>());
    
    // Bitwise operations and mathematical calculations
    int x = flat[0] ^ flat[2];
    int y = flat[1] | flat[3];
    
    double result1 = complex_calculation(x, y);
    double result2 = complex_calculation(y, x);
    
    // Trigonometric operations
    double trig_result = sin(result1) * cos(result2) + tan(result1/result2);
    
    // Final complex calculation
    int a = static_cast<int>(trunc(result1));
    int b = static_cast<int>(trunc(result2));
    int c = static_cast<int>(trunc(trig_result * 100));
    
    int final_result = ((a + b) * c) % 1000;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}