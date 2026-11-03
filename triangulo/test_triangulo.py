from triangulo import classificar


def test_equilatero():
    assert classificar(3, 3, 3) == "equilatero"


def test_isosceles():
    assert classificar(3, 3, 2) == "isosceles"
    assert classificar(3, 2, 3) == "isosceles"
    assert classificar(2, 3, 3) == "isosceles"


def test_escaleno():
    assert classificar(3, 4, 5) == "escaleno"


def test_lado_zero_ou_negativo():
    assert classificar(0, 3, 3) == "invalido"
    assert classificar(3, 0, 3) == "invalido"
    assert classificar(3, 3, 0) == "invalido"
    assert classificar(-1, 3, 3) == "invalido"


def test_nao_forma_triangulo():
    assert classificar(1, 2, 5) == "invalido"
    assert classificar(1, 5, 2) == "invalido"
    assert classificar(5, 1, 2) == "invalido"


def test_soma_igual_ao_terceiro_lado():
    # 1 + 2 == 3 -> "triangulo achatado", não vale
    assert classificar(1, 2, 3) == "invalido"
    assert classificar(1, 3, 2) == "invalido"
    assert classificar(3, 1, 2) == "invalido"


def test_lado_pequeno_mas_valido():
    # pega mutações tipo "<= 0" virar "<= 1"
    assert classificar(1, 1, 1) == "equilatero"