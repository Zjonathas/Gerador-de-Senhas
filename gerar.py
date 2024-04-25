from random import choice
from string import ascii_letters, digits, punctuation


def gerar_senha(tamanho):
    caracteres = ascii_letters + digits + punctuation
    senha = ''.join(choice(caracteres) for i in range(tamanho))
    return senha
