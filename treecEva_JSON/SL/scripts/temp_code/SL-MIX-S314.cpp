#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>

using namespace std;

double recursive_transform(int n, double base) {
    if (n <= 1) return base;
    double val = recursive_transform(n - 1, base);
    if (n % 3 == 0) {
        return val * log(val + 1);
    } else if (n % 3 == 1) {
        return sqrt(val) + sin(val);
    } else {
        return pow(val, 1.0/3.0) + cos(val);
    }
}

int bitwise_chain(int x) {
    x = x << 2;
    x = x ^ 0xF;
    x = x & 0xFF;
    x = x >> 1;
    return x | 0x1;
}

struct DataPack {
    vector<int> indices;
    double value;
    int flag;
};

int main() {
    vector<DataPack> packs(3);
    
    // Initialize first pack
    packs[0].indices = {2, 4, 6};
    packs[0].value = 3.5;
    packs[0].flag = 1;
    
    // Initialize second pack
    packs[1].indices = {1, 3, 5, 7};
    packs[1].value = 2.0;
    packs[1].flag = 0;
    
    // Initialize third pack
    packs[2].indices = {0, 8, 9};
    packs[2].value = 5.0;
    packs[2].flag = 1;
    
    double accumulator = 0.0;
    for (int i = 0; i < 3; i++) {
        int sum_indices = 0;
        for (int idx : packs[i].indices) {
            sum_indices += idx;
        }
        
        int transformed_index = bitwise_chain(sum_indices);
        
        if (packs[i].flag) {
            double temp = recursive_transform(transformed_index, packs[i].value);
            accumulator += floor(temp * 1000) / 1000;
        } else {
            accumulator -= ceil(packs[i].value * transformed_index);
        }
    }
    
    int final_int = static_cast<int>(accumulator);
    bitset<16> bits(final_int);
    int bit_count = bits.count();
    
    double final_result = accumulator * bit_count;
    
    cout << "Result: " << final_result << endl;
    return 0;
}