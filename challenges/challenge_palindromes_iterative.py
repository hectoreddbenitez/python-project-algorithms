def is_palindrome_iterative(word):
    # start = 0
    # end = len(word) - 1
    # if not word:
    #     return False
    # while start <= end:
    #         if word[start] != word[end]:
    #             return False
    #         else:
    #             start = start + 1
    #             end = end - 1
    # return True

    # Pythonic way!!
    if not word:
        return False
    else:
        if word == word[::-1]:
            return True
    return False
