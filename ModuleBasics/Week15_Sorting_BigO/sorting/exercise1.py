def bubble_sort(elements):
    num_elements = len(elements)
    for index in range(num_elements):
        swapped = False
        for inner_index in range(0, num_elements - index - 1):
            current_value = elements[inner_index]
            next_value = elements[inner_index + 1]
            if current_value > next_value:
                elements[inner_index] = next_value
                elements[inner_index + 1] = current_value
                swapped = True
        if not swapped:
            break


def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted elements:", data)
    bubble_sort(data)
    print("Sorted elements:", data)


# Example usage:
if __name__ == "__main__":
    main()
