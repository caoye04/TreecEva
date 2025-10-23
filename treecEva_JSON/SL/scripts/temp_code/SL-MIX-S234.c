#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int is_prime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
    return 1;
}

int main() {
    volatile int packet_id = 12345;
    int prime_factors = 0;
    int temp_id = packet_id;
    
    // Count distinct prime factors
    for (int i = 2; i <= temp_id; i++) {
        if (is_prime(i) && temp_id % i == 0) {
            prime_factors++;
            while (temp_id % i == 0) {
                temp_id /= i;
            }
        }
    }
    
    struct packet_data {
        int id;
        int factors;
        char pattern[];  // flexible array member
    };
    
    struct packet_data *pkt = malloc(sizeof(struct packet_data) + 10);
    pkt->id = packet_id;
    pkt->factors = prime_factors;
    
    // Simulate pattern matching with regex-like logic
    char pattern_match = 0;
    if ((pkt->id & 0xF) == 0x9) {  // Check if last 4 bits are 1001
        pattern_match = 1;
    }
    
    int security_score = 0;
    if (pattern_match) {
        security_score = gcd(pkt->id, pkt->factors * 100);
    } else {
        security_score = (pkt->id >> 2) ^ (pkt->factors << 3);
    }
    
    if (is_prime(security_score)) {
        security_score += 1000;
    }
    
    printf("Result: %d\n", security_score);
    free(pkt);
    return 0;
}