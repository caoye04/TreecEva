#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

double recursive_power_sum(int base, int exp, int depth) {
    if (depth <= 0) return 1.0;
    return pow(base, exp) + recursive_power_sum(base, exp - 1, depth - 1);
}

int main() {
    int values[4][4] = {{2, 3, 5, 7}, {11, 13, 17, 19}, {23, 29, 31, 37}, {41, 43, 47, 53}};
    double temp = 0.0;
    int mask = 0xF0;  // 11110000 in binary
    char buffer[256];
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if ((i * j) & (mask >> 4)) {
                temp += sqrt(values[i][j]);
            } else {
                temp -= cbrt(values[i][j]);
            }
        }
    }
    
    int x = static_cast<int>(temp) % 100;
    int y = (x << 2) ^ 0xAA;
    double z = recursive_power_sum(2, y % 10, 3);
    
    snprintf(buffer, sizeof(buffer), "Value: %f", z);
    int len = strlen(buffer);
    int result = (len * y) & 0xFF;
    
    cout << "Result: " << result << endl;
    return 0;
}