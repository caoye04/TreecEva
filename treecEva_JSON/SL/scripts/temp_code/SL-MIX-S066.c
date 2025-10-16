#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define FIB_STEPS 6

typedef struct DigitWheel {
    int position;
    int history[];  // flexible array member
} DigitWheel;

typedef struct WheelNode {
    DigitWheel* wheel;
    int (*step_func)(int pos, int step_val);
    struct WheelNode* next;
} WheelNode;

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int step_operation(int pos, int step_val) {
    return (pos + step_val) % 10;
}

int main() {
    int final_torque = 0;
    int num_wheels = 4;
    
    // Create linked list of wheels
    WheelNode* head = NULL;
    WheelNode* current = NULL;
    
    for (int i = 0; i < num_wheels; i++) {
        WheelNode* node = (WheelNode*)malloc(sizeof(WheelNode));
        size_t wheel_size = sizeof(DigitWheel) + FIB_STEPS * sizeof(int);
        node->wheel = (DigitWheel*)malloc(wheel_size);
        node->wheel->position = i + 1;
        node->step_func = step_operation;
        node->next = NULL;
        
        if (head == NULL) {
            head = node;
            current = node;
        } else {
            current->next = node;
            current = node;
        }
    }
    
    // Apply Fibonacci-based stepping
    current = head;
    int wheel_index = 0;
    while (current != NULL) {
        for (int step = 1; step <= FIB_STEPS; step++) {
            int fib_val = fibonacci(step);
            current->wheel->history[step-1] = current->wheel->position;
            current->wheel->position = current->step_func(current->wheel->position, fib_val);
        }
        final_torque += current->wheel->position * (wheel_index + 1);
        current = current->next;
        wheel_index++;
    }
    
    printf("Result: %d\n", final_torque);
    return 0;
}