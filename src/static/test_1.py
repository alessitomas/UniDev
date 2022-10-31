import pytest
from math import pi
import solution



@pytest.mark.parametrize("raio, area", [
    pytest.param(n, fatorial, id=f'Raio: {n}')
    for n, fatorial in [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320)
    ]])
def test_vários_raios(n, fatorial):
    dica = ''
    saida = solution.calcula_fatorial(n)
    if type(saida) != type(fatorial):
        dica += f'O tipo da resposta esperado é {type(fatorial)}, mas sua função devolve {type(saida)}.'
    assert fatorial == saida, f'Algo deu errado. \nAo calcular a área para o raio {n}, esperava {fatorial} mas obteve {saida}.\n{dica}'
