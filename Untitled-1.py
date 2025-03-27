def main():
    ##definir tipos após atribuição, float, int, str
    var_A = float(input("First"))
    var_B =  float(input("Second"))

    add = var_A + var_B
    sub = var_A - var_B
    mult= var_A * var_B
    div = var_A/var_B
    ##format podemos formatar uma frase adicionando os elementos dentro do parentese 
    print("valor da adição{}, valor da subtração{}".format(add,sub))

main()