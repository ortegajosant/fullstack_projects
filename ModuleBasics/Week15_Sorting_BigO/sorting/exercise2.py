def bubble_sort_right_to_left(elements):
    num_elements = len(elements)
    for index in range(num_elements):
        swapped = False
        for inner_index in range(num_elements - 1, index, -1):
            current_value = elements[inner_index]
            prev_value = elements[inner_index - 1]
            if current_value < prev_value:
                elements[inner_index] = prev_value
                elements[inner_index - 1] = current_value
                swapped = True
        if not swapped:
            break


def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted elements:", data)
    bubble_sort_right_to_left(data)
    print("Sorted elements:", data)


if __name__ == "__main__":
    main()
