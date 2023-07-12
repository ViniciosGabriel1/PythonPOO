import calc_financeira_modulo

# Exemplo de dados de vendas
venda1 = {'produtos': [{'nome': 'Celular', 'preco': 1000, 'quantidade': 2}, {'nome': 'Fone de ouvido', 'preco': 100, 'quantidade': 5}]}
venda2 = {'produtos': [{'nome': 'Laptop', 'preco': 2000, 'quantidade': 1}, {'nome': 'Teclado', 'preco': 50, 'quantidade': 3}]}

# Calcula a receita total das vendas
vendas = [venda1, venda2]
receita_total =calc_financeira_modulo.calcular_receita(vendas)

# Calcula o custo total dos produtos
custo_total = 1500

# Calcula o lucro
lucro = calc_financeira_modulo.calcular_lucro(receita_total, custo_total)

# Imprime os resultados
print("Receita total:", receita_total)
print("Lucro:", lucro)
