def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""

    if not word or word[low_index] != word[high_index]:
       return  False
    else:
        low_index += 1
        high_index -= 1
        if low_index <= high_index:
            # com ajuda da Maravilhosa MARIA CAROLINA!
            return is_palindrome_recursive(word, low_index, high_index)
        return True

        
        

