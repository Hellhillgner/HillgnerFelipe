from reverter_inteiro import reverter_inteiro
print("Olá! Tudo bem coleguinha?")
while True:
    opcao = input("Se você deseja ver a função do Hillgner digite 1, se deseja ver a função do Felipe digite 2, digite 3 para encerrar o programa\n")
    match opcao:
        case "1":
            continue #atualizar com a função do Hillgner
        case "2":
            reverter_inteiro()
        case "3":
            break
        case "_":
            print("Por favor digite uma opção válida")
print("Obrigado por usar esse programa maneiro, até a próxima!")