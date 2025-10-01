#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

double compute_recursive(double base, int exp) {
    if (exp <= 1) return base;
    return base * compute_recursive(base, exp - 1);
}

struct DataPack {
    double values[3][3];
    int flags[4];
};

union MixedData {
    long long integer_val;
    double float_val;
};

int main() {
    DataPack dp;
    MixedData md;
    
    // Initialize dp.values with powers of indices
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            dp.values[i][j] = pow(i+1, j+1);
        }
    }
    
    // Set flags based on bitwise logic
    dp.flags[0] = 0b1100 & 0b1010;
    dp.flags[1] = 0b1100 | 0b0011;
    dp.flags[2] = 0b1100 ^ 0b0101;
    dp.flags[3] = ~0b0011 & 0b1111;
    
    // Manipulate mixed data union
    md.integer_val = (dp.flags[0] << 4) + dp.flags[1];
    
    // Perform complex calculation using struct data
    double accumulator = 0.0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if((i*j)%2 == 0) {
                accumulator += dp.values[i][j] / (i+j+1);
            } else {
                accumulator -= sqrt(dp.values[i][j]);
            }
        }
    }
    
    // Apply bitwise shifts and masks
    int shifted_flags = (dp.flags[2] << 2) >> 1;
    int masked_value = shifted_flags & 0xF;
    
    // Recursive computation
    double recursive_result = compute_recursive(accumulator / 10.0, 3);
    
    // Final combination using all computed values
    long long intermediate = md.integer_val;
    double sin_component = sin(recursive_result);
    double cos_component = cos(masked_value / 10.0);
    
    double final_result = (intermediate * sin_component) + (masked_value * cos_component) + recursive_result;
    
    // Round to nearest integer as per problem requirement
    final_result = round(final_result);
    
    cout << "Result: " << final_result << endl;
    return 0;
}