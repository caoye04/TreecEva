#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX_LEN 100

int custom_sequence(int n) {
    if (n <= 1) return n;
    return custom_sequence(n - 1) + 2 * custom_sequence(n - 2) + 3;
}

int extract_number(const char* str) {
    int num = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            num = num * 10 + (str[i] - '0');
        }
    }
    return num;
}

int main() {
    char data[MAX_LEN] = "Level5Data123";
    int base_value = extract_number(data);
    int seq_index = (int)(sqrt(base_value) + 0.5);
    int sequence_result = custom_sequence(seq_index);
    int mask = 0xF0;
    int shifted = (sequence_result << 2) & mask;
    int final_result = (shifted ^ 0xAA) + (base_value % 7);
    printf("Result: %d\n", final_result);
    return 0;
}