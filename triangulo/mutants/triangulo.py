

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classificar__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_classificar__mutmut)
def classificar(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_orig(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_1(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b and b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_2(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c and a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_3(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a - b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_4(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b < c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_5(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a - c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_6(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c < b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_7(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b - c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_8(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c < a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_9(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "XXinvalidoXX"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_10(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "INVALIDO"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_11(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b or b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_12(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a != b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_13(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b != c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_14(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "XXequilateroXX"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_15(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "EQUILATERO"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_16(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c and b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_17(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b and a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_18(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a != b or a == c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_19(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a != c or b == c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_20(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b != c:
        return "isosceles"
    return "escaleno"
def x_classificar__mutmut_21(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "XXisoscelesXX"
    return "escaleno"
def x_classificar__mutmut_22(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "ISOSCELES"
    return "escaleno"
def x_classificar__mutmut_23(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "XXescalenoXX"
def x_classificar__mutmut_24(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "ESCALENO"

mutants_x_classificar__mutmut['_mutmut_orig'] = x_classificar__mutmut_orig # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_1'] = x_classificar__mutmut_1 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_2'] = x_classificar__mutmut_2 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_3'] = x_classificar__mutmut_3 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_4'] = x_classificar__mutmut_4 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_5'] = x_classificar__mutmut_5 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_6'] = x_classificar__mutmut_6 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_7'] = x_classificar__mutmut_7 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_8'] = x_classificar__mutmut_8 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_9'] = x_classificar__mutmut_9 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_10'] = x_classificar__mutmut_10 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_11'] = x_classificar__mutmut_11 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_12'] = x_classificar__mutmut_12 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_13'] = x_classificar__mutmut_13 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_14'] = x_classificar__mutmut_14 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_15'] = x_classificar__mutmut_15 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_16'] = x_classificar__mutmut_16 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_17'] = x_classificar__mutmut_17 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_18'] = x_classificar__mutmut_18 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_19'] = x_classificar__mutmut_19 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_20'] = x_classificar__mutmut_20 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_21'] = x_classificar__mutmut_21 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_22'] = x_classificar__mutmut_22 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_23'] = x_classificar__mutmut_23 # type: ignore # mutmut generated
mutants_x_classificar__mutmut['x_classificar__mutmut_24'] = x_classificar__mutmut_24 # type: ignore # mutmut generated


if __name__ == "__main__":
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    print(classificar(a, b, c))