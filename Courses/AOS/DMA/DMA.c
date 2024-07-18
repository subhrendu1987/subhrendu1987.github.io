#include <stdio.h>
#include <stdlib.h>

int main() {
    int *array;
    int n, i;
    int sum = 0;

    // Input the number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Dynamically allocate memory for n integers
    array = (int *)malloc(n * sizeof(int));
    if (array == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Input the elements of the array
    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // Calculate the sum of the elements
    for (i = 0; i < n; i++) {
        sum += array[i];
    }

    // Print the sum
    printf("Sum of the elements: %d\n", sum);

    // Free the dynamically allocated memory
    free(array);

    return 0;
}
