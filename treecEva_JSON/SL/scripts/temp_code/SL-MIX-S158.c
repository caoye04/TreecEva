#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdbool.h>

#define ARRAY_SIZE 12

union DataPun {
    unsigned int as_uint;
    float as_float;
};

struct BitFieldConfig {
    unsigned int flag1 : 3;
    unsigned int flag2 : 5;
    unsigned int flag3 : 4;
};

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}

int count_valid_bit_patterns(struct BitFieldConfig cfg) {
    int count = 0;
    for (int f1 = 0; f1 < (1 << 3); f1++) {
        for (int f2 = 0; f2 < (1 << 5); f2++) {
            for (int f3 = 0; f3 < (1 << 4); f3++) {
                struct BitFieldConfig test = {f1, f2, f3};
                if ((test.flag1 & cfg.flag1) && (test.flag2 & cfg.flag2) && (test.flag3 & cfg.flag3)) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    unsigned int sensor_data[ARRAY_SIZE] = {0x1F2E3D4C, 0x5A6B7C8D, 0x9E0F1A2B, 0x3C4D5E6F, 0x7A8B9C0D, 0xBECFD0E1,
                                            0x2F3A4B5C, 0x6D7E8F9A, 0xAF0B1C2D, 0xE3F4A5B6, 0xC7D8E9FA, 0x0B1C2D3E};
    
    union DataPun converter;
    struct BitFieldConfig config = {5, 17, 9};
    
    int primes_selected[ARRAY_SIZE];
    int prime_count = 0;
    
    for (int i = 0; i < ARRAY_SIZE; i++) {
        converter.as_uint = sensor_data[i];
        if (is_prime(i)) {
            primes_selected[prime_count++] = (int)converter.as_float;
        }
    }
    
    int cumulative_lcm = 1;
    for (int i = 0; i < prime_count; i++) {
        cumulative_lcm = lcm(cumulative_lcm, primes_selected[i] > 0 ? primes_selected[i] : 1);
    }
    
    int pattern_count = count_valid_bit_patterns(config);
    
    int final_metric = cumulative_lcm + pattern_count;
    
    printf("Result: %d\n", final_metric);
    return 0;
}