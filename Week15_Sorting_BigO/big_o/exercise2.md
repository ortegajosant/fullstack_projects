# Big O Analysis of Algorithms

Below are four algorithms, their code, and an analysis of their time complexity using Big O notation.

---

## 1. print_numbers_times_2

```python
def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)
```
**Time Complexity**
The function iterates once over `numbers_list`, performing a constant-time operation for each element.
The time complexity is O(n).

**Space Complexity:**  
The function does not create any new data structures that grow with the input size. It only uses a constant amount of extra space for the loop variable.
Thus, the space complexity is O(1).

## 2. check_if_lists_have_an_equal

```python
def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False
```

**Time Complexity**
The function uses two nested loops: the outer loop iterates over list_a (length n), and the inner loop iterates over list_b (length m).
So the time complexity is O(n * m) in the worst case.

**Space Complexity**
The space complexity is O(1) because the function only uses a constant amount of extra memory for loop variables, regardless of the size of the input lists.


## 3. print_10_or_less_elements

```python
def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])
```

**Time Complexity**
The function's loop runs at most 10 times, regardless of the size of list_to_print.
Thus, the time complexity is O(1), indicating constant time performance.

**Space Complexity:**  
The function uses only a constant amount of extra space (for variables like `list_len` and `index`), regardless of the input list size.  
Therefore, the space complexity is O(1).

## 4. generate_list_trios

```python
def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
    return result_list
```

The function has three nested loops, each iterating over one of the input lists (list_a, list_b, list_c).
If the lengths of the lists are n, m, and p respectively, the time complexity is O(n * m * p).

**Space Complexity**
The space complexity is also O(n * m * p), since result_list stores every possible trio as a string, resulting in n * m * p elements in memory.

## Summary Table

| Algorithm Name                  | Time Complexity | Space Complexity   |
|---------------------------------|----------------|-------------------|
| print_numbers_times_2           | O(n)           | O(1)              |
| check_if_lists_have_an_equal    | O(n * m)       | O(1)              |
| print_10_or_less_elements       | O(1)           | O(1)              |
| generate_list_trios             | O(n * m * p)   | O(n * m * p)      |
