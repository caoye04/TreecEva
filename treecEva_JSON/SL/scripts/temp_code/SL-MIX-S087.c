#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct packet_header {
    unsigned int version : 4;
    unsigned int ihl : 4;
    unsigned int tos : 8;
    unsigned int tot_len : 16;
};

struct packet_stats {
    int count;
    double sum;
    double sum_sq;
};

void update_stats(struct packet_stats* stats, double value) {
    stats->count++;
    stats->sum += value;
    stats->sum_sq += value * value;
}

double compute_variance(struct packet_stats* stats) {
    if (stats->count <= 1) return 0.0;
    double mean = stats->sum / stats->count;
    return (stats->sum_sq / stats->count) - (mean * mean);
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    struct packet_header packets[4] = {
        {4, 5, 0, 40},
        {4, 6, 8, 64},
        {6, 5, 16, 52},
        {4, 5, 0, 48}
    };
    
    struct packet_stats stats = {0, 0.0, 0.0};
    int composite_field = 0;
    
    for (int i = 0; i < 4; i++) {
        int field_value = (packets[i].version << 12) | 
                         (packets[i].ihl << 8) | 
                         packets[i].tos;
        update_stats(&stats, (double)field_value);
        composite_field += packets[i].tot_len;
    }
    
    double variance = compute_variance(&stats);
    int checksum_base = (int)floor(variance);
    int final_checksum = gcd(checksum_base, composite_field);
    
    printf("Result: %d\n", final_checksum);
    return 0;
}