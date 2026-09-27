# ENTRADA

Valor_total = float(input("Infome aqui o valor total da sua compra em R$: "))

# PROCESSAMENTO

if Valor_total >300:
    print("Parabéns! Nessa compra você receberá um desconto de 15% 🤩")
    Novo_preco = Valor_total*0.85

elif Valor_total >= 200:
    print("Parabéns! Nessa compra você receberá um desconto de 10% 🤩")
    Novo_preco = Valor_total*0.90

elif Valor_total <200:
    print("Parabens! Nessa compra você receberá um desconto de 5% 🤩")
    Novo_preco = (Valor_total*0.95)


# SAIDA

print("O valor a ser pago em sua conta agora é R$ ",Novo_preco)
print("Dica: Quanto MAIS você compra, MAIOR o seu desconto 😍")
print("Boas compras!! 🎁🛒")