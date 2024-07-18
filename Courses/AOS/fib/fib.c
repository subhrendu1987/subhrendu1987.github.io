#include <stdio.h>

// Function to generate Fibonacci numbers
void generateFibonacci(int limit) {
    int a = 0, b = 1, next;

    printf("Fibonacci Series: %d, %d", a, b);

    next = a + b;
    while (next <= limit) {
        printf(", %d", next);
        a = b;
        b = next;
        next = a + b;
    }
    printf("\n");
}

int main() {
    int limit;

    // Input from user
    printf("Enter the limit for Fibonacci series: ");
    scanf("%d", &limit);

    // Generate and print Fibonacci series up to the given limit
    generateFibonacci(limit);

    return 0;
}
