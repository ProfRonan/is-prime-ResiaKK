def primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i <= numero ** 0.5:
        if numero % i == 0:
            return False
        i += 1
    return True

numero = int(input("Digite um número inteiro: "))

if numero <= 0:
    print("Número inválido")
else:
    if primo(numero):
        print("Primo")
    else:
        print("Não primo")
