

nome= input("Insira seu nome: ")

while True:
    idade_input = input ("Qual a sua idade? ")
    try:
        idade = int(idade_input)
        break #sai do loop se a conversão der certo.
    except ValueError:
        print("Digite apenas números inteiros para a idade")

print(f"Nome: {nome} ")
print(f"Idade: {idade}")

