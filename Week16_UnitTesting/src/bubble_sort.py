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
