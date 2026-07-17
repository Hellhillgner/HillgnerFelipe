from reverter_inteiro import reverter_inteiro
from area import calcular_area_triangulo  
print("Olá! Tudo bem coleguinha?")
while True:
    opcao = input("Se você deseja ver a função do Hillgner digite 1, se deseja ver a função do Felipe digite 2, digite 3 para encerrar o programa\n")
    match opcao:
        case "1":
            calcular_area_triangulo()
        case "2":
            reverter_inteiro()
        case "3":
            break
print("Obrigado por usar esse programa maneiro, até a próxima!")
