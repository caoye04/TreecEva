#define _USE_MATH_DEFINES
#include <stdio.h>
#define STACK_SIZE 100

int main() {
    int command_stack[STACK_SIZE];
    int *top = command_stack - 1;  // Pointer to top of stack
    int final_position = 0;
    
    // Simulate pushing commands onto the stack
    for (int i = 1; i <= 5; i++) {
        *(++top) = i * 2;  // Push even numbers: 2, 4, 6, 8, 10
    }
    
    // Process commands with nested loops
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            if (top >= command_stack) {
                final_position += *top;  // Add top command to position
                top--;  // Pop from stack
            }
        }
    }
    
    printf("Result: %d\n", final_position);
    return 0;
}