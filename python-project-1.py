print('Bem-vindo a loja do Gabriel Peixoto de Campos') # mensagem de boas-vindas

valor = float(input('Entre com o valor do produto: '))   # recebe o preço do produto
quantidade = int(input('Entre com a quantidade do produto: '))   # recebe a quantidade do produto



preco = valor * quantidade   # calcula o preco



# não recebe desconto se a quantidade for menor que 200
if (quantidade < 200):
    print('O valor SEM desconto: R${}'.format(preco))   # mostra o valor sem desconto



# se a quantidade for igual ou maior que 200 ou menor que 1000 o desconto sera de 5%
elif (quantidade >= 200 and quantidade < 1000):
    desconto = preco * (5 / 100)   # aplica o desconto de 5%
    precoFinal = preco - desconto   # preço com desconto



# se a quantidade for igual ou maior que 1000 ou menor que 2000 o desconto sera de 10%
elif (quantidade >= 1000 and quantidade < 2000):
    desconto = preco * (10 / 100)   # aplica o desconto de 10%
    precoFinal = preco - desconto   # preço com desconto



# se a quantidade for igual ou maior que 2000 o desconto sera de 15%
else:
    desconto = preco * (15 / 100)   # aplica o desconto de 15%
    precoFinal = preco - desconto   # preço com desconto



print('O valor SEM desconto: R${}'.format(preco))   # mostra o valor sem desconto
print('O valor COM desconto: R${}'.format(precoFinal))   # mostra o valor com desconto