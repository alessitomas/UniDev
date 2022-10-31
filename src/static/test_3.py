import pytest
from math import pi
import solution



@pytest.mark.parametrize("raio, area", [
    pytest.param(raio, area, id=f'Raio: {raio}')
    for raio, area in [
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False)
    ]])
def test_vários_raios(raio, area):
    dica = ''
    saida = solution.calcula_primo(raio)
    if type(saida) != type(area):
        dica += f'O tipo da resposta esperado é {type(area)}, mas sua função devolve {type(saida)}.'
    assert area == saida, f'Algo deu errado. \nAo calcular a área para o raio {raio}, esperava {area} mas obteve {saida}.\n{dica}'
