def calcular_total(venda):
    total = sum(produto['preco'] * produto['quantidade'] for produto in venda['produtos'])
    return total

def calcular_receita(vendas):
    receita = sum(calcular_total(venda) for venda in vendas)
    return receita

def imprimir_receita(receita):
    print("Receita total:", receita)


    # Exemplo de dados de vendas
venda1 = {'produtos': [{'nome': 'Celular', 'preco': 1000, 'quantidade': 2}, 
                        {'nome': 'Fone de ouvido', 'preco': 100, 'quantidade': 5},
                        {'nome': 'Laptop', 'preco': 2000, 'quantidade': 1},
                        {'nome': 'Teclado', 'preco': 50, 'quantidade': 3}]}
    
    # Calcula a receita total das vendas
vendas = [venda1]
receita_total = calcular_receita(vendas)

    # Imprime a receita total apenas quando o arquivo é executado como um programa principal
imprimir_receita(receita_total)
    
