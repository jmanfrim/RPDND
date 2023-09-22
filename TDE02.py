#Codigo feito por Felipe Ribas, Igor Mamus e Joao Vitor Manfrim
def f(x, var_dict):
    var_dict['x'] = x
    return eval(expressao_f, var_dict)

def g(x, var_dict):
    var_dict['x'] = x
    return eval(expressao_g, var_dict)

def composicao_g_f(x, f, g, var_dict):
    resultado_g = g(f(x, var_dict), var_dict)
    return resultado_g

def composicao_g_g(x, g, var_dict):
    resultado_g = g(g(x, var_dict), var_dict)
    return resultado_g

def composicao_f_f(x, f, var_dict):
    resultado_f = f(f(x, var_dict), var_dict)
    return resultado_f

def composicao_f_g(x, f, g, var_dict):
    resultado_f = f(g(x, var_dict), var_dict)
    return resultado_f

expressao_f = input("Insira a expressão de f(x): ")
expressao_g = input("Insira a expressão de g(x): ")

x = float(input("Insira um valor para x: "))

var_dict = {'x': x}

resultado_g_f = composicao_g_f(x, f, g, var_dict)
resultado_g_g = composicao_g_g(x, g, var_dict)
resultado_f_f = composicao_f_f(x, f, var_dict)
resultado_f_g = composicao_f_g(x, f, g, var_dict)

print("(g ∘ f)(", x, ") =", resultado_g_f)
print("(g ∘ g)(", x, ") =", resultado_g_g)
print("(f ∘ f)(", x, ") =", resultado_f_f)
print("(f ∘ g)(", x, ") =", resultado_f_g)

