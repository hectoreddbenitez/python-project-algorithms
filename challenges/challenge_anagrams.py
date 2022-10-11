# def selection_sort(string):
#     n = len(string)
#     for index in range(n - 1):
#         min_index = index
#         for search_index in range(index + 1, n):
#             if string[search_index] < string[min_index]:
#                 min_index = search_index

#         current_element = string[index]
#         string[index] = string[min_index]
#         string[min_index] = current_element

#     return string
def quick_sort(string_list, start, end):
    if start < end:
        p = partition(string_list, start, end)
        quick_sort(string_list, start, p - 1)
        quick_sort(string_list, p + 1, end)


def partition(string_list, start, end):
    pivot = string_list[end]
    delimiter = start - 1

    for index in range(start, end):
        if string_list[index] <= pivot:
            delimiter = delimiter + 1
            string_list[index], string_list[delimiter] = (
                string_list[delimiter],
                string_list[index],
            )

    string_list[delimiter + 1], string_list[end] = (
        string_list[end],
        string_list[delimiter + 1],
    )

    return delimiter + 1


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    else:
        string_1_low = list(first_string.lower())
        string_2_low = list(second_string.lower())
        quick_sort(string_1_low, 0, len(string_1_low) - 1)
        quick_sort(string_2_low, 0, len(string_2_low) - 1)
        if string_1_low == string_2_low:
            return True
        return False
