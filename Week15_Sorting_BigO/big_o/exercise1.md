# Bubble Sort Big O Analysis

## Time Complexity

### Worst Case: **O(n²)**
- Occurs when the list is in reverse order.
- For each element, the algorithm compares it with every other element, resulting in roughly n * (n-1) / 2 comparisons and swaps.

### Best Case: **O(n)**
- Occurs when the list is already sorted.
- The algorithm makes one pass through the list and finds no swaps are needed, so it terminates early.

## Space Complexity

### Space: **O(1)**
- Bubble sort is an in-place sorting algorithm.
- It only requires a constant amount of additional memory space for variables like `swapped`, `current_value`, and `next_value`.

## Summary Table

| Case        | Time Complexity | Space Complexity |
|-------------|----------------|------------------|
| Best        | O(n)           | O(1)             |
| Worst       | O(n²)          | O(1)             |
