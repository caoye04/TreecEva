#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double complexFunction(int a, double b, vector<int>& data) {
    double sum = 0.0;
    for (int i = 0; i < data.size(); i++) {
        if (i % 2 == 0) {
            sum += sqrt(abs(data[i] * a));
        } else {
            sum -= pow(b, i % 3);
        }
    }
    return sum;
}

int bitwiseOperation(int x, int y) {
    int step1 = x << 2;  // Left shift by 2
    int step2 = step1 & (y | 0xF);  // AND with (y OR 15)
    int step3 = step2 ^ (x >> 1);   // XOR with right shift of x
    return step3;
}

int main() {
    vector<int> numbers = {4, -9, 16, -25, 36, -49, 64};
    int base = 3;
    double exponent = 2.5;
    
    // Process the numbers vector
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] < 0) {
            numbers[i] = abs(numbers[i]);
        }
        numbers[i] = static_cast<int>(sqrt(numbers[i])) + bitwiseOperation(i, base);
    }
    
    // Calculate complex function result
    double funcResult = complexFunction(base, exponent, numbers);
    
    // Perform additional mathematical operations
    int bitwiseResult = bitwiseOperation(static_cast<int>(funcResult), 7);
    double trigResult = sin(funcResult) * cos(bitwiseResult) + tan(funcResult / 2);
    
    // Conditional logic with multiple branches
    double intermediate;
    if (trigResult > 0) {
        intermediate = pow(trigResult, 1.5) + log(abs(bitwiseResult) + 1);
    } else if (trigResult < 0) {
        intermediate = pow(abs(trigResult), 2.0) - exp(bitwiseResult % 5);
    } else {
        intermediate = sqrt(abs(funcResult)) * 3.14159;
    }
    
    // Final calculation step
    double result = (intermediate * 100) - (static_cast<int>(intermediate) % 17) + ceil(funcResult);
    
    cout << "Result: " << static_cast<long long>(result) << endl;
    return 0;
}