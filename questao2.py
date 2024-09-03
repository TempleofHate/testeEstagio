def contar_letras_a(string):
    string = string.lower()
    contagem = string.count('a')
    
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

string = input("Informe uma string: ")
resultado = contar_letras_a(string)
print(resultado)
