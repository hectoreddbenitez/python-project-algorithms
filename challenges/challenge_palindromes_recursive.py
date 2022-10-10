def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # condisão de parada
    if not word or word[low_index] != word[high_index]:
       return  False
    else:
        low_index += 1
        high_index -= 1
        # confere que os inidices não tenham se cruzado, deixando chegar até a letra central.
        if low_index <= high_index:
            # com ajuda da Maravilhosa MARIA CAROLINA!
            # chamada de si mesma
            return is_palindrome_recursive(word, low_index, high_index)
            # quando a condição não é mais verdadeira, significa que a palavra foi interada por completo, sem erros
            # então, a palavra é palindromo, e retorna True
        return True

        
        

