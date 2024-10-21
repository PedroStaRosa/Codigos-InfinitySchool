def invert_string(txt):
    
    # texto_invertido = ""
    # for i in range(len(txt) - 1, -1, -1):
    #     texto_invertido += txt[i]
    # return texto_invertido

    return txt[::-1]

def count_works(txt):
    result = txt.split()
    
    return len(result)

def palindrome(txt):
    
    result = invert_string(txt)
    
    if result == txt:
        return f"é um palíndromo"
    
    return f"não é um palíndromo"
