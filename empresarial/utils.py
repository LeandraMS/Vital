from random import choice, shuffle
import string

def gerar_senha_aleatoria(tamanho):

    caracteres_especiais = string.punctuation   
    caracteres = string.ascii_letters
    numeros_list = string.digits

    
    sobra = 0
    qtd = tamanho // 3
    if not tamanho % 3 == 0:
        sobra = tamanho - qtd

    letras = ''
    for i in range(0, qtd + sobra):
        letras += choice(caracteres)

    numeros = ''
    for i in range(0, qtd):
        numeros += choice(numeros_list)

    especiais = ''
    for i in range(0, qtd):
        especiais += choice(caracteres_especiais)

    
    senha = list(letras + numeros + especiais)
    shuffle(senha)

    return ''.join(senha)