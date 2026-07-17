def reverter_inteiro():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            if num < 0:
                raise ValueError
            break
        except ValueError:
            print("Número inválido.")
            continue
    num_invertido = ""
    for char in str(num):
        num_invertido = char + num_invertido
    print(int(num_invertido))