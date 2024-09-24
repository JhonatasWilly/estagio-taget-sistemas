# Questão 2
string = input(str("Digite uma palava para verificar se contem a letra A: "))


contA = 0
conta = 0

for caractere in string:
    if(caractere == "A"):
        contA += 1
    if(caractere == "a"):
        conta += 1


# Poderia ter deixado todas as letras Maiúsculas e facilitaria a busca, mas optei por fazer assim para informar a quantidade de As Maiúsculas e Minúsculas. 
print(f"A quantiade de a: {conta} \nA quantidade de A: {contA}. \nTotal: {conta + contA}")
