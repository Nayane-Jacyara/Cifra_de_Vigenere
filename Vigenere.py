class CifraBase(object):
    # Retorna text em maiúsculas
    def format_str(self, text):
        return text.upper() 
    
    # Retorna alphabet com deslocamento de valor shift
    def shift_alphabet(self, alphabet, shift):
        return alphabet[shift % len(alphabet):] + alphabet[:shift % len(alphabet)]

class Vigenere(CifraBase):
    def __init__(self):
        # Alfabeto usado na cifra de Vigenère
        self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,;_ '

    def repeat_password(self, chave, texto):
        # Repete a chave até que seu comprimento seja igual ou maior que o texto de entrada
        new_chave = ''
        i = 0
        while len(new_chave) < len(texto):
            new_chave += chave[i % len(chave)]
            i += 1
        return new_chave

    def encrypt(self, texto, chave, decrypt=False):
        # Repete a chave para ter o mesmo comprimento do texto
        chave = self.repeat_password(chave, texto)
        texto_cifrado = ''
        for idx, char in enumerate(texto):
            # Índice da letra da chave no alfabeto
            idx_key = self.plain.find(chave[idx])
            # Gera o alfabeto cifrado
            c_alphabet = self.shift_alphabet(self.plain, idx_key)

            if decrypt:
                # Se está decifrando, encontra a letra no alfabeto cifrado
                idx_p = c_alphabet.find(char)
                texto_cifrado += self.plain[idx_p]
            else:
                # Se está cifrando, encontra a letra no alfabeto original
                if char in self.plain:
                    idx_p = self.plain.find(char)
                    texto_cifrado += c_alphabet[idx_p]
                else:
                    # Se o caractere não está no alfabeto original, mantém inalterado
                    texto_cifrado += char

        return texto_cifrado
    
    def decrypt(self, texto_cifrado, chave):
        # Decifra o texto cifrado
        return self.encrypt(texto_cifrado, chave, True)


if __name__ == "__main__":
    texto = input('Texto a ser cifrado: ')
    chave = input('Chave: ')
 
    cifra = Vigenere()
    texto_cifrado = cifra.encrypt(texto, chave)
    print('Texto cifrado: {0}'.format(texto_cifrado))
    print('Texto plano: {0}'.format(cifra.decrypt(texto_cifrado, chave)))
