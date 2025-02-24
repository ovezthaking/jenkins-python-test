import operations as ops


def test_add():
    assert ops.add(2, 2) == 4


def test_sub():
    assert ops.sub(5, 7) == -2


def test_div():
    assert ops.div(8, 4) == 2


def test_mul():
    assert ops.mul(6, 9) == 54


def test_pow():
    assert ops.pow(10, 2) == 100


def test_sqrt():
    assert ops.sqrt(9, 3) == 3
