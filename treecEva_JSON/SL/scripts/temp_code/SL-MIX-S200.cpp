#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + 1));
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int n = s.length();
    
    int a = matrix[1][2]; // 13
    int b = static_cast<int>(s[n - 1]) ^ 0xFF; // XOR with 255
    double c = compute_expression(a % 5, b >> 2); // Right shift b by 2
    
    bool flag1 = (a > 10) && (b < 200);
    bool flag2 = !((c < 50) || (s.find("World") != string::npos));
    
    int d = (flag1 ? a : b) & (flag2 ? 0xF0 : 0x0F); // Bitwise AND with mask
    
    vector<pair<string, double>> data = {{s.substr(0, 5), c}, {s.substr(5), static_cast<double>(d)}};
    
    double e = data[0].second * data[1].second;
    int f = static_cast<int>(floor(e / 100.0));
    
    int g = (f << 3) | (f >> 1); // Bitwise operations
    
    int h = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            if ((val & 1) == 1) { // Check if odd
                h += val;
            }
        }
    }
    
    int result = (g + h) % 256;
    cout << "Result: " << result << endl;
    return 0;
}