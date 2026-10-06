# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de 

salario = float(input('Digite o salário do funcionário: R$ '))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f'Seu salário é de R${salario},e com o aumento de 15% seu salário ficará de R${novo_salario}.')