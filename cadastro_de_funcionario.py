from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome completo: '))
while len(dados['nome']) <= 6:
    dados['nome'] = input("Seu nome deve ter mais que 6 caracteres: ")

nasc = int(input("Ano de Nascimento: "))
while (nasc >= (datetime.now().year - 14)):
    nasc = float(input("ERRO! A idade permitida é a partir de 14 anos .\n \
    Tente novamente:"))
dados['idade'] = datetime.now().year - nasc

dados['genero'] = int(input('Gênero (1 - Feminino, 2- Masculino): '))
while (dados['genero'] > 2):
    dados['genero'] = float(input("ERRO! Digite um número inteiro valido. Por favor, escolha 1 para Feminino ou 2 para Masculino\n \
    Tente novamente:"))

dados['ctps'] = int(input('Número da Carteira de Trabalho sem pontos ou traços (Digite 0 caso não tenha): '))

if dados['ctps'] != 0 and dados['genero'] == 1:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratação'] + 30 - nasc
elif dados['ctps'] != 0 and dados['genero'] == 2:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratação'] + 35 - nasc

print(' -=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')