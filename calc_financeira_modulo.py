def calcular_total(venda):
    total = sum(produto['preco'] * produto['quantidade'] for produto in venda['produtos'])
    return total

def calcular_receita(vendas):
    receita = sum(calcular_total(venda) for venda in vendas)
    return receita

def calcular_lucro(receita, custo):
    lucro = receita - custo
    return lucro