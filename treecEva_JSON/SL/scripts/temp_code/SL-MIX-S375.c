#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct DataPoint {
    int values[4];
    double weight;
};

struct ComplexStructure {
    struct DataPoint points[3];
    char tag[16];
    int* ref_ptr;
};

int compute_weighted_sum(struct DataPoint* dp) {
    int sum = 0;
    for(int i = 0; i < 4; i++) {
        sum += (int)(dp->values[i] * dp->weight);
    }
    return sum;
}

int main() {
    struct ComplexStructure cs;
    int base_values[] = {10, 20, 30, 40};
    int aux_value = 7;
    
    // Initialize first DataPoint
    for(int i = 0; i < 4; i++) {
        cs.points[0].values[i] = base_values[i] ^ (i << 2);
    }
    cs.points[0].weight = 1.5;
    
    // Initialize second DataPoint
    memcpy(cs.points[1].values, cs.points[0].values, sizeof(cs.points[0].values));
    for(int i = 0; i < 4; i++) {
        cs.points[1].values[i] = cs.points[1].values[i] & ~(1 << i);
    }
    cs.points[1].weight = sqrt(2.0);
    
    // Initialize third DataPoint
    for(int i = 0; i < 4; i++) {
        cs.points[2].values[i] = cs.points[0].values[i] | cs.points[1].values[i];
    }
    cs.points[2].weight = log( cs.points[1].values[0] > 0 ? cs.points[1].values[0] : 1 );
    
    // String manipulation
    strcpy(cs.tag, "DATA_");
    char suffix[8];
    sprintf(suffix, "%d", (int)(cs.points[2].weight * 10));
    strcat(cs.tag, suffix);
    
    // Pointer operations
    int intermediate = compute_weighted_sum(&cs.points[1]);
    cs.ref_ptr = &intermediate;
    
    // Complex calculation chain
    int stage1 = (*cs.ref_ptr) >> 2;
    int stage2 = stage1 * (cs.points[0].values[2] % 7);
    int stage3 = stage2 + (int)strlen(cs.tag);
    
    // Conditional manipulation
    int selector = (cs.points[2].values[1] & 0xF) > 8 ? 3 : 1;
    int final_adjustment = cs.points[selector].values[3] ^ (int)floor(cs.points[2].weight);
    
    // POINT_X
    int final_result = (stage3 << 1) - final_adjustment + (cs.tag[5] - '0');
    
    printf("Result: %d\n", final_result);
    return 0;
}