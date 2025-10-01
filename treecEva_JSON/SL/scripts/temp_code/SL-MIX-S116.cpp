#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<pair<int, string>>> data = {
        {{2, "alpha"}, {3, "beta"}},
        {{5, "gamma"}, {7, "delta"}, {11, "epsilon"}},
        {{13, "zeta"}, {17, "eta"}}
    };
    
    // Mathematical computation chain
    double x = 2.5;
    double y = pow(x, 3) + sqrt(16) - log(2.71828); // e ≈ 2.71828
    int z = static_cast<int>(y) & 15; // Bitwise AND with 15 (0b1111)
    
    // String manipulation
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + s2;
    reverse(s3.begin(), s3.end());
    
    // Complex calculation using data structure values
    int sum = 0;
    for (const auto& row : data) {
        for (const auto& p : row) {
            sum += p.first * z;
        }
    }
    
    // Apply trigonometric function
    double trig_result = sin(M_PI / 2); // Should be 1.0
    int trig_int = static_cast<int>(round(trig_result));
    
    // Final computation
    int result = (sum >> 2) + s3.length() - trig_int; // Right shift by 2 is equivalent to integer division by 4
    
    cout << "Result: " << result << endl;
    
    return 0;
}