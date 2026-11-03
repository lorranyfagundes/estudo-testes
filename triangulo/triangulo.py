def classificar(a, b, c):
    # essa regra ja barra lados zero ou negativos
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalido"
    if a == b and b == c:
        return "equilatero"
    if a == b or a == c or b == c:
        return "isosceles"
    return "escaleno"


if __name__ == "__main__":
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    print(classificar(a, b, c))