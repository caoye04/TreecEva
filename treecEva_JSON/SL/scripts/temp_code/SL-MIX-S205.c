#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

struct rule {
    int mask;
    int value;
    int (*eval)(int current, int mask, int value);
};

int match_exact(int current, int mask, int value) {
    return (current & mask) == value;
}

int match_any(int current, int mask, int value) {
    return (current & mask) != 0;
}

int main() {
    volatile int packet_flags = 0b11010110;
    int decision_flag = 0b00000001;
    
    struct rule rules[3];
    
    rules[0].mask = 0b11110000;
    rules[0].value = 0b11010000;
    rules[0].eval = match_exact;
    
    rules[1].mask = 0b00001111;
    rules[1].value = 0b00000110;
    rules[1].eval = match_any;
    
    rules[2].mask = 0b11111111;
    rules[2].value = 0b11010110;
    rules[2].eval = match_exact;
    
    for (int i = 0; i < 3; i++) {
        if (rules[i].eval(packet_flags, rules[i].mask, rules[i].value)) {
            decision_flag |= (1 << (i + 1));
        } else {
            decision_flag &= ~(1 << (i + 1));
        }
    }
    
    int final_acceptance = 0;
    if (decision_flag & 0b00000100) {
        final_acceptance += 10;
    }
    if (decision_flag & 0b00001000) {
        final_acceptance *= 2;
    }
    if (decision_flag & 0b00010000) {
        final_acceptance -= 5;
    }
    
    printf("Result: %d\n", final_acceptance);
    return 0;
}