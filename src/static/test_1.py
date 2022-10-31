import pytest
from math import pi
import solution



@pytest.mark.parametrize("raio, area", [
    pytest.param(raio, area, id=f'Raio: {raio}')
    for raio, area in [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320)
    ]])
def test_vários_raios(raio, area):
    dica = ''
    saida = solution.calcula_fatorial(raio)
    if type(saida) != type(area):
        dica += f'O tipo da resposta esperado é {type(area)}, mas sua função devolve {type(saida)}.'
    assert area == saida, f'Algo deu errado. \nAo calcular a área para o raio {raio}, esperava {area} mas obteve {saida}.\n{dica}'
