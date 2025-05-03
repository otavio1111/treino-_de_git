import datetime

ano = "s"
while ano == "s":
    ano_nascimento = int(input("Digite o ano de nascimento do usuario "))
    ano_atual = datetime.date.today().year 
    idade = ano_atual - ano_nascimento
    print("A idade do usuario é:", idade)
    ano = input("Você quer continuar s ou n ").lower()
    break
print("Obrigado")