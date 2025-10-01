#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base = 2;
    int exp = 4;
    double trig_arg = M_PI / 4.0;
    
    // Step 1: Compute power
    int power_result = pow(base, exp);
    
    // Step 2: Bitwise operations
    int bitwise = (power_result & 15) | 3;
    
    // Step 3: Trigonometric operation
    double sin_val = sin(trig_arg);
    int sin_scaled = static_cast<int>(round(sin_val * 100));
    
    // Step 4: Matrix diagonal sum
    int diag_sum = 0;
    for(int i=0; i<3; i++) {
        diag_sum += matrix[i][i];
    }
    
    // Step 5: Logical evaluation
    bool cond1 = (bitwise > 10);
    bool cond2 = (sin_scaled < 75);
    int logical_result = (cond1 && cond2) ? 1 : 0;
    
    // Step 6: Final calculation
    int result = (diag_sum * logical_result) + ((bitwise ^ sin_scaled) & 0xFF);
    
    cout << "Result: " << result << endl;
    return 0;
}