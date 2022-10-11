def selection_sort(string):
    n = len(string)
    for index in range(n - 1):
        min_index = index
        for search_index in range(index + 1, n):
            if string[search_index] < string[min_index]:
                min_index = search_index

        current_element = string[index]
        string[index] = string[min_index]
        string[min_index] = current_element

    return string


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    else:
        first_string_sorted = selection_sort(list(first_string.lower()))
        second_string_sorted = selection_sort(list(second_string.lower()))
        if first_string_sorted != second_string_sorted:
            return False
        return True
