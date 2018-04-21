def ConfereEstoque(*args, **kwargs):
    if "macas" in kwargs:
        print("Temos macas")
    else:
        print("Comprar macas")
    
    n = len(args)
    print("Precisamos comprar:",n,"tipos de fruta")


lista = ['banana', 'pera']
estoque = {'macas':10,'laranjas':15,'abacaxi':1}
ConfereEstoque(*lista,**estoque)

l = ['banana', 'pera','uva']
e = {'laranjas':15,'abacaxi':1}
ConfereEstoque(*l, **e)