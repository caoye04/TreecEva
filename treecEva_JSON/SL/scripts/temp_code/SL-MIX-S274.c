#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define FIRMWARE_SEGMENTS 4
#define SEGMENT_SIZE 3

int add_op(int a, int b) { return a + b; }
int xor_op(int a, int b) { return a ^ b; }
int mul_op(int a, int b) { return a * b; }

int (*ops[])(int, int) = {add_op, xor_op, mul_op};

int process_segment(int *data, int size, int op_index) {
    if (size <= 0) return 0;
    int result = data[0];
    for (int i = 1; i < size; i++) {
        result = ops[op_index](result, data[i]);
    }
    return result;
}

int recursive_checksum(int **segments, int *op_indices, int count) {
    if (count <= 0) return 0;
    int segment_result = process_segment(segments[0], SEGMENT_SIZE, op_indices[0]);
    return segment_result + recursive_checksum(segments + 1, op_indices + 1, count - 1);
}

int main() {
    int seg0[] = {12, 25, 6};
    int seg1[] = {8, 15, 3};
    int seg2[] = {7, 19, 4};
    int seg3[] = {11, 22, 5};
    
    int *firmware_segments[] = {seg0, seg1, seg2, seg3};
    int operation_indices[] = {0, 1, 2, 0}; // 0=add, 1=xor, 2=mul
    
    int final_checksum = recursive_checksum(firmware_segments, operation_indices, FIRMWARE_SEGMENTS);
    printf("Result: %d\n", final_checksum);
    return 0;
}