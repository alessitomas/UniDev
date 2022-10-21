import pytest
from math import pi
import solution

TESTE = [
        (1, pi*1**2),
        (2, pi*2**2),
        (3, pi*3**2),

    ]

@pytest.mark.parametrize("raio, area", [
    pytest.param(raio, area, id=f'Raio: {raio}')  
    for raio, area in TESTE])
def test_vários_raios(raio, area):
    dica = ''
    saida = solution.calcula_area_do_circulo(raio)
    if type(saida) != type(area):
        dica += f'O tipo da resposta esperado é {type(area)}, mas sua função devolve {type(saida)}.'
    assert area == saida, f'Algo deu errado. \nAo calcular a área para o raio {raio}, esperava {area} mas obteve {saida}.\n{dica}'
