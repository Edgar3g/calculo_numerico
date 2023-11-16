# f(x) = x^3 - 9x +3 (minha função)


import math, time

a = int(input("Digite o intervalo de A: "))
b = int(input("Digite o intervalo de B: "))
E = float(input("Digite o limite de E: "))

time.sleep(1)
print("\n\...Calculando, \t Aguarde...")

time.sleep(1)
print("\n")
Xk = 0
k = 0
K_max = 20
A = a
B = b


def validateIntervalo(x):
    f = math.pow(x, 3) - (9 * x) + 3
    return f


def validateProduct(a1, b1):
    return a1 * b1


def deff(x):
    # derivada da função = 3x² - 9
    return 3 * math.pow(x, 2) - 9


f_A = validateIntervalo(a)
f_B = validateIntervalo(b)
deff_a = deff(a)
deff_b = deff(b)

productoF = validateProduct(f_A, f_B)
productoDeff = validateProduct(deff(a), deff(b))

time.sleep(2)

"""

 3) Tabela Maluca

 --------------------------------------------------
 ' k ' a ' b ' xk = (a+b)/2 ' f(xk) ' |b - a| <= E' 
 --------------------------------------------------
 ' 0 ' 0 ' 1 '              '       '             '
 '   '   '   '              '       '             '
 '   '   '   '              '       '             '
 --------------------------------------------------


"""
if productoF < 0:
    print(f" Existe Raiz, Aproximada nesse intervalo [{a}, {b}] ")

    if productoDeff < 0:
        print(f"A Raiz é única para esse intervalo [{a}, {b}]")
    else:
        print(f"A Raiz não é única para esse intervalo [{a}, {b}]")

    # Code the tabela maluca
    for k in range(K_max):
        Xk = (A + B) / 2
        f_Xk = validateIntervalo(Xk)  # Se f (a) · f (x k ) < 0 então
        if f_Xk < 0:  # se o producto da função Xk for menor que 0, ou seja NEGATIVO
            B = Xk
        else:
            A = Xk

        # # saídas para test
        print(
            "-------------------------------------------------------------------------------"
        )
        print(f"k = {k} \t a = {A}   \t  b = {B}  \t Xk = {Xk} \t  |b - a| = {B - A} ")

        if b - a <= E:
            print(f"A Raiz aproximada encontrada é {f_Xk}")

            break


else:
    print(f" Não Existe Raiz, Aproximada nesse intervalo [{a}, {b}] ")
